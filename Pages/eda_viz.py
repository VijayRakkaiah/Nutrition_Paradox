import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
from Pages.questions import *
from Pages.report import *

# MySQL database connection establish
my_connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'nutrition_paradox'
)

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
    <div class="custom-title">Exploratory Data Analysis</div>
""", unsafe_allow_html=True)

# Dropdown to select the question
analysis = st.selectbox("Select a Question", eda_analysis)

# Each question visualization
if analysis == eda_analysis[0]:
    # Visualize Distributions
    # Histogram for Mean_Estimate
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.histplot(data=df_obesity, x="mean_estimate", kde=True, hue="gender", multiple="stack", bins=20, ax=axes[0])
    axes[0].set_title("Obesity Distribution by Gender")
    axes[0].set_xlabel("Mean Estimate")

    sns.histplot(data=df_malnutrition, x="mean_estimate", kde=True, hue="gender", multiple="stack", bins=20, ax=axes[1])
    axes[1].set_title("Malnutrition Distribution by Gender")
    axes[1].set_xlabel("Mean Estimate")

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(visualize_distributions)

elif analysis == eda_analysis[1]:
    # Time Trends
    # Line Plot: Mean Estimate over Year (aggregated)

    # Calculate trends
    obesity_trend = df_obesity.groupby("year")["mean_estimate"].mean().reset_index()
    malnutrition_trend = df_malnutrition.groupby("year")["mean_estimate"].mean().reset_index()

    # Subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Obesity trend
    sns.lineplot(data=obesity_trend, x="year", y="mean_estimate", marker="o", ax=axes[0])
    axes[0].set_title("Obesity Trend Over Years")
    axes[0].set_ylabel("Avg Mean Estimate")

    # Malnutrition trend
    sns.lineplot(data=malnutrition_trend, x="year", y="mean_estimate", marker="o", color='green', ax=axes[1])
    axes[1].set_title("Malnutrition Trend Over Years")
    axes[1].set_ylabel("Avg Mean Estimate")

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(time_trends)

elif analysis == eda_analysis[2]:
    # Regional Comparison
    # Box Plot: Mean Estimate by Region
    top_regions_obesity = df_obesity['region'].value_counts().nlargest(5).index
    top_regions_mal = df_malnutrition['region'].value_counts().nlargest(5).index

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(data=df_obesity[df_obesity['region'].isin(top_regions_obesity)],
                x="region", y="mean_estimate", ax=axes[0])
    axes[0].set_title("Obesity by Top 5 Regions")
    axes[0].tick_params(axis='x', rotation=45)

    sns.boxplot(data=df_malnutrition[df_malnutrition['region'].isin(top_regions_mal)],
                x="region", y="mean_estimate", ax=axes[1], color='lightblue')
    axes[1].set_title("Malnutrition by Top 5 Regions")
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(regional_comparison)

elif analysis == eda_analysis[3]:
    # Gender-wise Comparison
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(data=df_obesity, x="gender", y="mean_estimate", ax=axes[0])
    axes[0].set_title("Obesity by Gender")

    sns.boxplot(data=df_malnutrition, x="gender", y="mean_estimate", ax=axes[1], color='lightgreen')
    axes[1].set_title("Malnutrition by Gender")

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(gender_wise_comparison)


elif analysis == eda_analysis[4]:
    # Gender vs Region
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(data=df_obesity, x="gender", y="mean_estimate", hue="region", ax=axes[0])
    axes[0].set_title("Obesity by Gender and Region")

    sns.stripplot(data=df_malnutrition, x="gender", y="mean_estimate", hue="region",
                  dodge=True, alpha=0.6, jitter=True, ax=axes[1])
    axes[1].set_title("Malnutrition by Gender and Region")

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(Gender_vs_Region)

elif analysis == eda_analysis[5]:
    # Age group wise comparison
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Chart 1: Obesity by Age Group
    sns.boxplot(data=df_obesity, x='age_group', y='mean_estimate', ax=axes[0], palette='Blues')
    axes[0].set_title('Obesity by Age Group')
    axes[0].set_ylabel('Mean Estimate')
    axes[0].set_xlabel('age group')
    axes[0].tick_params(axis='x', rotation=45)

    # Chart 2: Malnutrition by Age Group
    sns.boxplot(data=df_malnutrition, x='age_group', y='mean_estimate', ax=axes[1], palette='Greens')
    axes[1].set_title('Malnutrition by Age Group')
    axes[1].set_ylabel('Mean Estimate')
    axes[1].set_xlabel('age group')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(age_group_wise_comparison)

elif analysis == eda_analysis[6]:
    # Compare Obesity vs Malnutrition
    # Overlay Distributions

    sns.kdeplot(df_obesity["mean_estimate"], label='Obesity', shade=True)
    sns.kdeplot(df_malnutrition["mean_estimate"], label='Malnutrition', shade=True)
    plt.title("Obesity vs Malnutrition Distribution")
    plt.legend()
    st.pyplot(plt.gcf())
    st.markdown(Compare_Obesity_vs_Malnutrition)

elif analysis == eda_analysis[7]:
    # Heatmap of CI Width vs Mean Estimate (Correlation)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Correlation heatmap for obesity
    sns.heatmap(df_obesity[["mean_estimate", "CI_width"]].corr(), annot=True, cmap="coolwarm", ax=axes[0])
    axes[0].set_title("Obesity Correlation Heatmap")

    # # Correlation heatmap for malnutrition
    sns.heatmap(df_malnutrition[["mean_estimate", "CI_width"]].corr(), annot=True, cmap="YlGnBu", ax=axes[1])
    axes[1].set_title("Malnutrition Correlation Heatmap")

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(CI_Width_vs_Mean_Estimate)

elif analysis == eda_analysis[8]:
    # Identify Top/Bottom Countries

    top_obesity = df_obesity.sort_values(by="mean_estimate", ascending=False).head(10)
    top_malnutrition = df_malnutrition.sort_values(by="mean_estimate", ascending=False).head(10)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Top 10 Countries with Highest Obesity
    sns.barplot(data=top_obesity, x="mean_estimate", y="country", palette="Reds_r", ax=axes[0])
    axes[0].set_title("Top 10 Countries - Obesity")

    # Bottom 10 Countries with Highest Malnutrition
    sns.barplot(data=top_malnutrition, x="mean_estimate", y="country", palette="Blues_r", ax=axes[1])
    axes[1].set_title("Top 10 Countries - Malnutrition")

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(top_10)

elif analysis == eda_analysis[9]:
    # Create 2x2 subplot figure
    fig, axs = plt.subplots(2, 2, figsize=(16, 10))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)

    # 1. Obesity Trend Over Years by Region
    sns.lineplot(data=df_obesity, x='year', y='mean_estimate', hue='region', ax=axs[0, 0], marker="o")
    axs[0, 0].set_title('Obesity Trend Over Years by Region')

    # 2. Obesity Trend Over Years by Gender
    sns.lineplot(data=df_obesity, x='year', y='mean_estimate', hue='gender', ax=axs[0, 1], marker="o")
    axs[0, 1].set_title('Obesity Trend Over Years by Gender')

    # 3. Obesity by Region and Gender
    sns.barplot(data=df_obesity, x='region', y='mean_estimate', hue='gender', ax=axs[1, 0], ci='sd')
    axs[1, 0].set_title('Obesity by Region and Gender')
    axs[1, 0].tick_params(axis='x', rotation=45)

    # 4. Obesity vs Malnutrition by Region
    # Prepare combined data
    df_obesity_temp = df_obesity[['region', 'mean_estimate', 'CI_width']].copy()
    df_obesity_temp['Type'] = 'Obesity'

    df_malnutrition_temp = df_malnutrition[['region', 'mean_estimate', 'CI_width']].copy()
    df_malnutrition_temp['Type'] = 'Malnutrition'

    df_combined = pd.concat([df_obesity_temp, df_malnutrition_temp])

    sns.barplot(data=df_combined, x='region', y='mean_estimate', hue='Type', ax=axs[1, 1], ci='sd')
    axs[1, 1].set_title('Obesity vs Malnutrition by Region')
    axs[1, 1].tick_params(axis='x', rotation=45)

    # Final layout and show
    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(Nutrition_Trends)

elif analysis == eda_analysis[10]:
    # Create figure and axes
    fig, axs = plt.subplots(2, 2, figsize=(16, 10))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)

    # 1. Malnutrition Trend Over Years by Region
    sns.lineplot(data=df_malnutrition, x='year', y='mean_estimate', hue='region', ax=axs[0, 0], marker='o')
    axs[0, 0].set_title('Malnutrition Trend Over Years by Region')

    # 2. Malnutrition Trend Over Years by Gender
    sns.lineplot(data=df_malnutrition, x='year', y='mean_estimate', hue='gender', ax=axs[0, 1], marker='o')
    axs[0, 1].set_title('Malnutrition Trend Over Years by Gender')

    # 3. Malnutrition by Region and Gender
    sns.barplot(data=df_malnutrition, x='region', y='mean_estimate', hue='gender', ax=axs[1, 0], ci='sd')
    axs[1, 0].set_title('Malnutrition by Region and Gender')
    axs[1, 0].tick_params(axis='x', rotation=45)

    # 4. Malnutrition by Region and Age Group
    sns.barplot(data=df_malnutrition, x='region', y='mean_estimate', hue='age_group', ax=axs[1, 1], ci='sd')
    axs[1, 1].set_title('Malnutrition by Region and Age Group')
    axs[1, 1].tick_params(axis='x', rotation=45)

    # Final adjustments
    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(Malnutrition_Patterns)

elif analysis == eda_analysis[11]:
    # Define South Asian countries
    south_asia_countries = [
        "India", "Bangladesh", "Pakistan", "Nepal", "Sri Lanka", "Bhutan", "Maldives", "Afghanistan"
    ]

    # Filter for South Asia
    obesity_sa = df_obesity[df_obesity["country"].isin(south_asia_countries)]
    malnutrition_sa = df_malnutrition[df_malnutrition["country"].isin(south_asia_countries)]

    fig, axs = plt.subplots(2, 2, figsize=(18, 12))

    # Plot 1: Adult Obesity Trend
    sns.lineplot(data=obesity_sa, x="year", y="mean_estimate", hue="country", ax=axs[0, 0])
    axs[0, 0].set_title("Adult Obesity Trend in South Asia")
    axs[0, 0].set_ylabel("Obesity (%)")

    # Plot 2: Adult Malnutrition Trend
    sns.lineplot(data=malnutrition_sa, x="year", y="mean_estimate", hue="country", ax=axs[0, 1])
    axs[0, 1].set_title("Adult Malnutrition Trend in South Asia")
    axs[0, 1].set_ylabel("Malnutrition (%)")

    # Plot 3: Boxplot of Obesity Distribution
    sns.boxplot(data=obesity_sa, x="country", y="mean_estimate", ax=axs[1, 0])
    axs[1, 0].set_title("Obesity Distribution by Country")
    axs[1, 0].set_ylabel("Obesity (%)")
    axs[1, 0].tick_params(axis='x', rotation=45)

    # Plot 4: Boxplot of Malnutrition Distribution
    sns.boxplot(data=malnutrition_sa, x="country", y="mean_estimate", ax=axs[1, 1])
    axs[1, 1].set_title("Malnutrition Distribution by Country")
    axs[1, 1].set_ylabel("Malnutrition (%)")
    axs[1, 1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    st.pyplot(plt.gcf())
    st.markdown(South_Asia)



st.markdown("---")

st.caption("Developed using Streamlit, Seaborn, and Matplotlib")