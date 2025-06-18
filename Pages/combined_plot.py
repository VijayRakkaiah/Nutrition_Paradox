import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from Pages.questions import *

# loading the data into data frame
df_obesity = pd.read_csv("df_obesity.csv")
df_malnutrition = pd.read_csv("df_malnutrition.csv")

# Title
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <style>
    .custom-title {
        font-family: 'Pacifico', cursive;
        font-size: 40px;
        color: #50C878	;
        text-align: center;
    }
    </style>
    <div class="custom-title">Combined Table Data Visualization</div>
""", unsafe_allow_html=True)

# Dropdown to select the question
question = st.selectbox("Select a Question", combined_questions)

# Each question visualization
if question == combined_questions[0]:
    # Choose 5 sample countries (you can modify these)
    countries = ["India", "United States", "Brazil", "Nigeria", "Bangladesh"]

    # Filter and compute average estimates
    obesity_avg = df_obesity[df_obesity["Country"].isin(countries)].groupby("Country")[
        "Mean_Estimate"].mean().reset_index()
    obesity_avg.rename(columns={"Mean_Estimate": "Obesity"}, inplace=True)

    malnutrition_avg = df_malnutrition[df_malnutrition["Country"].isin(countries)].groupby("Country")[
        "Mean_Estimate"].mean().reset_index()
    malnutrition_avg.rename(columns={"Mean_Estimate": "Malnutrition"}, inplace=True)

    # Merge the two
    combined = pd.merge(obesity_avg, malnutrition_avg, on="Country")

    # Melt for side-by-side bars
    combined_melted = pd.melt(combined, id_vars="Country", value_vars=["Obesity", "Malnutrition"],
                              var_name="Indicator", value_name="Estimate")

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(data=combined_melted, x="Country", y="Estimate", hue="Indicator", palette="Set2")

    plt.title("Obesity vs Malnutrition Comparison (Selected Countries)")
    plt.ylabel("Average Estimate (%)")
    plt.xlabel("Country")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == combined_questions[1]:
    # Group by gender and compute global average
    obesity_gender = df_obesity.groupby("Gender")["Mean_Estimate"].mean().reset_index()
    obesity_gender.rename(columns={"Mean_Estimate": "Obesity"}, inplace=True)

    malnutrition_gender = df_malnutrition.groupby("Gender")["Mean_Estimate"].mean().reset_index()
    malnutrition_gender.rename(columns={"Mean_Estimate": "Malnutrition"}, inplace=True)

    # Merge on Gender
    gender_combined = pd.merge(obesity_gender, malnutrition_gender, on="Gender")

    # Melt for plotting
    gender_melted = pd.melt(gender_combined, id_vars="Gender", value_vars=["Obesity", "Malnutrition"],
                            var_name="Indicator", value_name="Estimate")

    # Plot
    plt.figure(figsize=(8, 6))
    sns.barplot(data=gender_melted, x="Gender", y="Estimate", hue="Indicator", palette="pastel")

    plt.title("Gender-Based Disparity in Obesity and Malnutrition")
    plt.ylabel("Average Estimate (%)")
    plt.xlabel("Gender")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == combined_questions[2]:
    # Filter only Africa and America
    regions_of_interest = ["Africa", "Americas"]
    ob_region = df_obesity[df_obesity["Region"].isin(regions_of_interest)]
    mal_region = df_malnutrition[df_malnutrition["Region"].isin(regions_of_interest)]

    # Group and calculate averages
    ob_avg = ob_region.groupby("Region")["Mean_Estimate"].mean().reset_index()
    ob_avg.rename(columns={"Mean_Estimate": "Obesity"}, inplace=True)

    mal_avg = mal_region.groupby("Region")["Mean_Estimate"].mean().reset_index()
    mal_avg.rename(columns={"Mean_Estimate": "Malnutrition"}, inplace=True)

    # Merge both
    combined = pd.merge(ob_avg, mal_avg, on="Region")

    # Melt for grouped bar plot
    melted = pd.melt(combined, id_vars="Region", value_vars=["Obesity", "Malnutrition"],
                     var_name="Indicator", value_name="Estimate")

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(data=melted, x="Region", y="Estimate", hue="Indicator", palette="Set2")

    plt.title("Obesity vs Malnutrition in Africa and America")
    plt.xlabel("Region")
    plt.ylabel("Average Estimate (%)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == combined_questions[3]:
    # OBESITY: Start vs End Year
    ob_min = df_obesity.groupby("Country")["Year"].min().reset_index()
    ob_max = df_obesity.groupby("Country")["Year"].max().reset_index()

    ob_start = pd.merge(df_obesity, ob_min, on=["Country", "Year"])
    ob_end = pd.merge(df_obesity, ob_max, on=["Country", "Year"])

    ob_change = pd.merge(ob_start[["Country", "Mean_Estimate"]],
                         ob_end[["Country", "Mean_Estimate"]],
                         on="Country", suffixes=("_start", "_end"))
    ob_change["Obesity_Change"] = ob_change["Mean_Estimate_end"] - ob_change["Mean_Estimate_start"]

    # MALNUTRITION: Start vs End Year
    mal_min = df_malnutrition.groupby("Country")["Year"].min().reset_index()
    mal_max = df_malnutrition.groupby("Country")["Year"].max().reset_index()

    mal_start = pd.merge(df_malnutrition, mal_min, on=["Country", "Year"])
    mal_end = pd.merge(df_malnutrition, mal_max, on=["Country", "Year"])

    mal_change = pd.merge(mal_start[["Country", "Mean_Estimate"]],
                          mal_end[["Country", "Mean_Estimate"]],
                          on="Country", suffixes=("_start", "_end"))
    mal_change["Malnutrition_Change"] = mal_change["Mean_Estimate_start"] - mal_change["Mean_Estimate_end"]

    # COMBINE & FILTER
    combined = pd.merge(ob_change[["Country", "Obesity_Change"]],
                        mal_change[["Country", "Malnutrition_Change"]],
                        on="Country")

    # Filter countries where obesity increased and malnutrition decreased
    paradox = combined[
        (combined["Obesity_Change"] > 0) &
        (combined["Malnutrition_Change"] > 0)
        ]

    # Sort by obesity change and take top 5
    top_5 = paradox.sort_values(by="Obesity_Change", ascending=False).head(5)

    # PLOT
    melted = top_5.melt(id_vars="Country",
                        value_vars=["Obesity_Change", "Malnutrition_Change"],
                        var_name="Indicator", value_name="Change")

    fig = px.bar(melted,
                 x="Country",
                 y="Change",
                 color="Indicator",
                 barmode="group",
                 text_auto=".2f",
                 title="Top 5 Countries with Obesity Rising & Malnutrition Falling")

    fig.update_layout(xaxis_title="Country",
                      yaxis_title="Change in Estimate (%)",
                      template="plotly_white")

    # Render the Plotly chart in Streamlit
    st.plotly_chart(fig)

elif question == combined_questions[4]:
    # Group by age group and calculate average mean estimate
    ob_age = df_obesity.groupby("age_group")["Mean_Estimate"].mean().reset_index()
    ob_age.rename(columns={"Mean_Estimate": "Obesity"}, inplace=True)

    mal_age = df_malnutrition.groupby("age_group")["Mean_Estimate"].mean().reset_index()
    mal_age.rename(columns={"Mean_Estimate": "Malnutrition"}, inplace=True)

    # Merge both
    age_combined = pd.merge(ob_age, mal_age, on="age_group")

    # Melt for plotting
    melted = pd.melt(age_combined, id_vars="age_group",
                     value_vars=["Obesity", "Malnutrition"],
                     var_name="Indicator", value_name="Estimate")

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(data=melted, x="age_group", y="Estimate", hue="Indicator", palette="Set1")

    plt.title("Obesity vs Malnutrition by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Average Estimate (%)")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

st.markdown("---")

st.caption("Developed using Streamlit, Seaborn, and Matplotlib")