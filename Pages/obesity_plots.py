import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Pages.questions import *

# loading the data into data frame
df_obesity = pd.read_csv("df_obesity.csv")
df_malnutrition = pd.read_csv("df_malnutrition.csv")

# Title
st.title("Obesity Data Visualization")

# Dropdown to select the question
question = st.selectbox("Select a Question", obesity_questions)

# Each question visualization
if question == obesity_questions[0]:
    df_2022 = df_obesity[df_obesity["Year"] == 2022]

    # Group by Region and compute mean obesity
    region_avg = (
        df_2022.groupby("Region")["Mean_Estimate"]
        .mean()
        .nlargest(5)
        .reset_index()
    )

    # Plot using seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(data=region_avg, x="Mean_Estimate", y="Region", palette="Reds_r")

    plt.title("Top 5 Regions with Highest Average Obesity Levels (2022)")
    plt.xlabel("Average Obesity (%)")
    plt.ylabel("Region")
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[1]:
    top5_max = df_obesity.groupby("Country")["Mean_Estimate"].max().reset_index()
    top5_max = top5_max.sort_values(by="Mean_Estimate", ascending=False).head(5)

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(data=top5_max, x="Country", y="Mean_Estimate", palette="Oranges")

    plt.title("Top 5 Countries with Maximum Recorded Obesity")
    plt.ylabel("Max Obesity (%)")
    plt.xlabel("Country")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

# Add similar blocks for Q3 to Q25. For example:

elif question == obesity_questions[2]:
    india_data = df_obesity[df_obesity["Country"] == "India"]

    # Group by year and compute mean estimate
    india_trend = india_data.groupby("Year")["Mean_Estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(8, 4))
    sns.lineplot(
        data=india_trend,
        x="Year",
        y="Mean_Estimate",
        marker="o",
        color="blue"
    )

    plt.title("Obesity Trend in India Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Average Obesity (%)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[3]:
    # Group by Gender and calculate average obesity
    gender_avg = df_obesity.groupby("Gender")["Mean_Estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(8, 4))
    sns.barplot(
        data=gender_avg,
        x="Gender",
        y="Mean_Estimate",
        palette="Blues"
    )

    plt.title("Average Obesity by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Obesity (%)")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[4]:
    # Count of countries by category and age group
    country_count = df_obesity.groupby(["Obesity_level", "age_group"])["Country"].nunique().reset_index()
    country_count.rename(columns={"Country": "Country_Count"}, inplace=True)

    # Plot
    plt.figure(figsize=(10, 5))
    sns.barplot(
        data=country_count,
        x="Obesity_level",
        y="Country_Count",
        hue="age_group",
        palette="Set2"
    )

    plt.title("Country Count by Obesity Level Category and Age Group")
    plt.xlabel("Obesity Level Category")
    plt.ylabel("Number of Unique Countries")
    plt.legend(title="Age Group")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[5]:
    # Group by country and get average CI_Width
    ci_width_avg = df_obesity.groupby("Country")["CI_Width"].mean().reset_index()

    # Top 5 highest (least reliable)
    top_wide = ci_width_avg.sort_values(by="CI_Width", ascending=False).head(5)
    top_wide["Type"] = "Least Reliable"

    # Top 5 lowest (most consistent)
    top_narrow = ci_width_avg.sort_values(by="CI_Width", ascending=True).head(5)
    top_narrow["Type"] = "Most Consistent"

    # Combine
    ci_compare = pd.concat([top_wide, top_narrow])

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=ci_compare,
        x="CI_Width",
        y="Country",
        hue="Type",
        palette={"Least Reliable": "salmon", "Most Consistent": "lightgreen"}
    )

    plt.title("Top 5 Most and Least Reliable Countries (Average CI Width)")
    plt.xlabel("Average CI Width")
    plt.ylabel("Country")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[6]:
    # Group by age group and compute average obesity
    age_avg = df_obesity.groupby("age_group")["Mean_Estimate"].mean().reset_index()

    # Sort for consistent ordering
    age_avg = age_avg.sort_values(by="Mean_Estimate", ascending=False)

    # Plot
    plt.figure(figsize=(10, 5))
    sns.barplot(data=age_avg, x="age_group", y="Mean_Estimate", palette="Purples")

    plt.title("Average Obesity by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Average Obesity (%)")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[7]:
    # Group by country and compute average obesity and CI width
    country_summary = df_obesity.groupby("Country")[["Mean_Estimate", "CI_Width"]].mean().reset_index()

    # Filter for countries with low obesity and low CI_Width
    low_risk = country_summary.sort_values(by=["Mean_Estimate", "CI_Width"], ascending=[True, True]).head(10)

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=low_risk,
        x="Mean_Estimate",
        y="Country",
        palette="Greens"
    )

    plt.title("Top 10 Countries with Consistently Low Obesity (Low Mean & CI)")
    plt.xlabel("Average Obesity (%)")
    plt.ylabel("Country")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[8]:
    # Separate female and male data
    female = df_obesity[df_obesity["Gender"] == "Female"]
    male = df_obesity[df_obesity["Gender"] == "Male"]

    # Merge on country, year, and age_group to ensure same context
    merged = pd.merge(female, male, on=["Country", "Year", "age_group"], suffixes=('_female', '_male'))

    # Calculate difference
    merged["Difference"] = merged["Mean_Estimate_female"] - merged["Mean_Estimate_male"]

    # Filter for large differences (e.g., > 10%)
    large_gap = merged[merged["Difference"] > 10]

    # Group by Country and get average difference
    country_diff = large_gap.groupby("Country")["Difference"].mean().sort_values(ascending=False).reset_index().head(10)

    # Plot
    plt.figure(figsize=(10, 5))
    sns.barplot(data=country_diff, x="Difference", y="Country", palette="coolwarm")

    plt.title("Top 10 Countries Where Female Obesity Exceeds Male by Large Margin")
    plt.xlabel("Average % Difference (Female - Male)", )
    plt.ylabel("Country")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(plt.gcf())

elif question == obesity_questions[9]:
    # Group by year and calculate global average obesity
    global_trend = df_obesity.groupby("Year")["Mean_Estimate"].mean().reset_index()

    # Plot
    plt.figure(figsize=(6, 4))
    sns.lineplot(
        data=global_trend,
        x="Year",
        y="Mean_Estimate",
        marker="o",
        color="darkgreen"
    )

    plt.title("Global Average Obesity Percentage per Year")
    plt.xlabel("Year")
    plt.ylabel("Average Obesity (%)")
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    st.pyplot(plt.gcf())

st.markdown("---")
st.caption("Developed using Streamlit, Seaborn, and Matplotlib")