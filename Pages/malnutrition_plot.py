import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pymysql
from Pages.questions import *
from Pages.sql_queries import *

# MySQL database connection establish
my_connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'nutrition_paradox'
)

# creating pandas dataframe using MySQL query
def data_frame(que):
    df = pd.read_sql_query(que, my_connection)
    return df

# loading the data into data frame
df_obesity = pd.read_sql_query("SELECT * FROM obesity", my_connection)
df_malnutrition = pd.read_sql_query("SELECT * FROM malnutrition", my_connection)

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
    st.dataframe(data_frame(query_11))
    # Group by age group and calculate average malnutrition
    age_avg_mal = df_malnutrition.groupby("age_group")["mean_estimate"].mean().reset_index()

    # Sort for better visual clarity
    age_avg_mal = age_avg_mal.sort_values(by="mean_estimate", ascending=False)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=age_avg_mal,
        x="age_group",
        y="mean_estimate",
        palette="Oranges"
    )

    plt.title("Average Malnutrition by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Average Malnutrition (%)")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[1]:
    st.dataframe(data_frame(query_12))
    # Calculate average malnutrition per country
    country_avg_mal = df_malnutrition.groupby("country")["mean_estimate"].mean().reset_index()

    # Sort and get top 5
    top5_mal = country_avg_mal.sort_values(by="mean_estimate", ascending=False).head(5)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=top5_mal,
        x="mean_estimate",
        y="country",
        palette="Reds"
    )

    plt.title("Top 5 Countries with Highest Average Malnutrition")
    plt.xlabel("Average Malnutrition (%)")
    plt.ylabel("Country")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[2]:
    st.dataframe(data_frame(query_13))
    # Filter for African region
    africa_df = df_malnutrition[df_malnutrition["region"] == "Africa"]

    # Group by year and calculate average malnutrition
    africa_trend = africa_df.groupby("year")["mean_estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        data=africa_trend,
        x="year",
        y="mean_estimate",
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
    st.dataframe(data_frame(query_14))
    # Group by gender and calculate average malnutrition
    gender_avg = df_malnutrition.groupby("gender")["mean_estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=gender_avg,
        x="gender",
        y="mean_estimate",
        palette="Set2"
    )

    plt.title("Average Malnutrition by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Malnutrition (%)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[4]:
    st.dataframe(data_frame(query_15))
    # Group by age group and calculate average CI_Width
    ci_by_age = df_malnutrition.groupby("age_group")["CI_width"].mean().reset_index()

    # Sort for better visual clarity
    ci_by_age = ci_by_age.sort_values(by="CI_width", ascending=False)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=ci_by_age,
        x="age_group",
        y="CI_width",
        palette="Blues_r"
    )

    plt.title("Average CI_Width by Age Group (Malnutrition Estimates)")
    plt.xlabel("Age Group")
    plt.ylabel("Average Confidence Interval Width")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[5]:
    st.dataframe(data_frame(query_16))
    # Filter for the selected countries
    selected_countries = ["India", "Nigeria", "Brazil"]
    subset = df_malnutrition[df_malnutrition["country"].isin(selected_countries)]

    # Group by country and year
    trend = subset.groupby(["country", "year"])["mean_estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(9, 5))
    sns.lineplot(
        data=trend,
        x="year",
        y="mean_estimate",
        hue="country",
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
    st.dataframe(data_frame(query_17))
    # Group by Region and calculate average malnutrition
    region_avg = df_malnutrition.groupby("region")["mean_estimate"].mean().reset_index()

    # Sort by lowest malnutrition
    region_avg = region_avg.sort_values(by="mean_estimate", ascending=True)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=region_avg,
        x="mean_estimate",
        y="region",
        palette="Greens"
    )

    plt.title("Regions with Lowest Average Malnutrition")
    plt.xlabel("Average Malnutrition (%)")
    plt.ylabel("Region")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[7]:
    st.dataframe(data_frame(query_18))
    # Group by country and find earliest and latest estimates
    min_max_df = df_malnutrition.groupby('country').agg(Start_Year=('year', 'min'),
                                                        End_Year=('year', 'max')).reset_index()

    # Merge to get start and end year mean estimates
    start = df_malnutrition.merge(min_max_df[['country', 'Start_Year']], left_on=['country', 'year'],
                                  right_on=['country', 'Start_Year'])
    end = df_malnutrition.merge(min_max_df[['country', 'End_Year']], left_on=['country', 'year'],
                                right_on=['country', 'End_Year'])

    # Aggregate by country to get average of all entries in that year
    start_mean = start.groupby("country")["mean_estimate"].mean().reset_index(name="Start_Estimate")
    end_mean = end.groupby("country")["mean_estimate"].mean().reset_index(name="End_Estimate")

    # Merge and compute change
    change_df = pd.merge(start_mean, end_mean, on="country")
    change_df["Change"] = change_df["End_Estimate"] - change_df["Start_Estimate"]

    # Filter only increasing malnutrition
    increased = change_df[change_df["Change"] > 0].sort_values("Change", ascending=False).head(10)

    # Plot
    plt.figure(figsize=(10, 5))
    sns.barplot(data=increased, x="Change", y="country", color="brown")
    plt.title("Top 10 Countries with Increasing Malnutrition Over Time")
    plt.xlabel("Increase in Malnutrition (%)")
    plt.ylabel("Country")
    plt.grid(axis="x", linestyle="--", alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == malnutrition_questions[8]:
    st.dataframe(data_frame(query_19))
    # Group by year and calculate min and max of mean estimates
    yearly_min_max = df_malnutrition.groupby("year")["mean_estimate"].agg(["min", "max"]).reset_index()

    # Melt the DataFrame for side-by-side plotting
    yearly_min_max_melted = pd.melt(
        yearly_min_max,
        id_vars="year",
        value_vars=["min", "max"],
        var_name="Statistic",
        value_name="mean_estimate"
    )

    # Plot
    plt.figure(figsize=(8, 4))
    sns.lineplot(
        data=yearly_min_max_melted,
        x="year",
        y="mean_estimate",
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
    st.dataframe(data_frame(query_20))
    # Filter rows where CI_Width > 5
    high_ci = df_malnutrition[df_malnutrition["CI_width"] > 5]

    # Count occurrences per country
    flagged_countries = high_ci["country"].value_counts().reset_index()
    flagged_countries.columns = ["country", "Flag_Count"]

    # Get top 10 countries with the most CI_Width > 5 entries
    top_flags = flagged_countries.head(10)

    # Create interactive bar plot using Plotly
    fig = px.bar(
        top_flags,
        x="Flag_Count",
        y="country",
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