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
    <div class="custom-title">Malnutrition Data Visualization</div>
""", unsafe_allow_html=True)

# Dropdown to select the question
question = st.selectbox("Select a Question", malnutrition_questions)

# Each question visualization
if question == malnutrition_questions[0]:
    # Group by age group and calculate average malnutrition
    age_avg_mal = df_malnutrition.groupby("age_group")["Mean_Estimate"].mean().reset_index()

    # Sort for better visual clarity
    age_avg_mal = age_avg_mal.sort_values(by="Mean_Estimate", ascending=False)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=age_avg_mal,
        x="age_group",
        y="Mean_Estimate",
        palette="Oranges"
    )

    plt.title("Average Malnutrition by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Average Malnutrition (%)")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[1]:
    # Calculate average malnutrition per country
    country_avg_mal = df_malnutrition.groupby("Country")["Mean_Estimate"].mean().reset_index()

    # Sort and get top 5
    top5_mal = country_avg_mal.sort_values(by="Mean_Estimate", ascending=False).head(5)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=top5_mal,
        x="Mean_Estimate",
        y="Country",
        palette="Reds"
    )

    plt.title("Top 5 Countries with Highest Average Malnutrition")
    plt.xlabel("Average Malnutrition (%)")
    plt.ylabel("Country")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[2]:
    # Filter for African region
    africa_df = df_malnutrition[df_malnutrition["Region"] == "Africa"]

    # Group by year and calculate average malnutrition
    africa_trend = africa_df.groupby("Year")["Mean_Estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=africa_trend,
        x="Year",
        y="Mean_Estimate",
        marker="o",
        color="darkred"
    )

    plt.title("Malnutrition Trend in African Region Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Average Malnutrition (%)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[3]:
    # Group by gender and calculate average malnutrition
    gender_avg = df_malnutrition.groupby("Gender")["Mean_Estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=gender_avg,
        x="Gender",
        y="Mean_Estimate",
        palette="Set2"
    )

    plt.title("Average Malnutrition by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Malnutrition (%)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[4]:
    # Group by age group and calculate average CI_Width
    ci_by_age = df_malnutrition.groupby("age_group")["CI_Width"].mean().reset_index()

    # Sort for better visual clarity
    ci_by_age = ci_by_age.sort_values(by="CI_Width", ascending=False)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=ci_by_age,
        x="age_group",
        y="CI_Width",
        palette="Blues_r"
    )

    plt.title("Average CI_Width by Age Group (Malnutrition Estimates)")
    plt.xlabel("Age Group")
    plt.ylabel("Average Confidence Interval Width")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[5]:
    # Filter for the selected countries
    selected_countries = ["India", "Nigeria", "Brazil"]
    subset = df_malnutrition[df_malnutrition["Country"].isin(selected_countries)]

    # Group by country and year
    trend = subset.groupby(["Country", "Year"])["Mean_Estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(9, 5))
    sns.lineplot(
        data=trend,
        x="Year",
        y="Mean_Estimate",
        hue="Country",
        marker="o",
        palette="Set1"
    )

    plt.title("Yearly Malnutrition Change: India, Nigeria, Brazil")
    plt.xlabel("Year")
    plt.ylabel("Average Malnutrition (%)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[6]:
    # Group by Region and calculate average malnutrition
    region_avg = df_malnutrition.groupby("Region")["Mean_Estimate"].mean().reset_index()

    # Sort by lowest malnutrition
    region_avg = region_avg.sort_values(by="Mean_Estimate", ascending=True)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=region_avg,
        x="Mean_Estimate",
        y="Region",
        palette="Greens"
    )

    plt.title("Regions with Lowest Average Malnutrition")
    plt.xlabel("Average Malnutrition (%)")
    plt.ylabel("Region")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[7]:
    # Group by country and find earliest and latest estimates
    min_max_df = df_malnutrition.groupby('Country').agg(Start_Year=('Year', 'min'),
                                                        End_Year=('Year', 'max')).reset_index()

    # Merge to get start and end year mean estimates
    start = df_malnutrition.merge(min_max_df[['Country', 'Start_Year']], left_on=['Country', 'Year'],
                                  right_on=['Country', 'Start_Year'])
    end = df_malnutrition.merge(min_max_df[['Country', 'End_Year']], left_on=['Country', 'Year'],
                                right_on=['Country', 'End_Year'])

    # Aggregate by country to get average of all entries in that year
    start_mean = start.groupby("Country")["Mean_Estimate"].mean().reset_index(name="Start_Estimate")
    end_mean = end.groupby("Country")["Mean_Estimate"].mean().reset_index(name="End_Estimate")

    # Merge and compute change
    change_df = pd.merge(start_mean, end_mean, on="Country")
    change_df["Change"] = change_df["End_Estimate"] - change_df["Start_Estimate"]

    # Filter only increasing malnutrition
    increased = change_df[change_df["Change"] > 0].sort_values("Change", ascending=False).head(10)

    # Plot
    plt.figure(figsize=(10, 5))
    sns.barplot(data=increased, x="Change", y="Country", color="brown")
    plt.title("Top 10 Countries with Increasing Malnutrition Over Time")
    plt.xlabel("Increase in Malnutrition (%)")
    plt.ylabel("Country")
    plt.grid(axis="x", linestyle="--", alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[8]:
    # Group by year and calculate min and max of mean estimates
    yearly_min_max = df_malnutrition.groupby("Year")["Mean_Estimate"].agg(["min", "max"]).reset_index()

    # Melt the DataFrame for side-by-side plotting
    yearly_min_max_melted = pd.melt(
        yearly_min_max,
        id_vars="Year",
        value_vars=["min", "max"],
        var_name="Statistic",
        value_name="Mean_Estimate"
    )

    # Plot
    plt.figure(figsize=(8, 4))
    sns.lineplot(
        data=yearly_min_max_melted,
        x="Year",
        y="Mean_Estimate",
        hue="Statistic",
        marker="o",
        palette={"min": "skyblue", "max": "crimson"}
    )

    plt.title("Year-wise Min and Max Malnutrition Estimates Across Countries")
    plt.xlabel("Year")
    plt.ylabel("Malnutrition (%)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[9]:
    # Filter rows where CI_Width > 5
    high_ci = df_malnutrition[df_malnutrition["CI_Width"] > 5]

    # Count occurrences per country
    flagged_countries = high_ci["Country"].value_counts().reset_index()
    flagged_countries.columns = ["Country", "Flag_Count"]

    # Get top 10 countries with the most CI_Width > 5 entries
    top_flags = flagged_countries.head(10)

    # Create interactive bar plot using Plotly
    fig = px.bar(
        top_flags,
        x="Flag_Count",
        y="Country",
        orientation='h',
        color="Flag_Count",
        color_continuous_scale="viridis",  # Changed here
        title="Top 10 Countries with Most High CI_Width Entries (Malnutrition)"
    )

    # Update layout for better appearance
    fig.update_layout(
        xaxis_title="Number of Entries with CI_Width > 5",
        yaxis_title="Country",
        yaxis=dict(autorange="reversed"),  # Keep highest at the top
        plot_bgcolor='white'
    )

    # Render the Plotly chart in Streamlit
    st.plotly_chart(fig)

st.markdown("---")
st.caption("Developed using Streamlit, Seaborn, and Matplotlib")