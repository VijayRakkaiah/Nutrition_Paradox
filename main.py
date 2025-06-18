import streamlit as st

st.set_page_config(
    page_title="Nutrition Paradox",
    page_icon="assets/logo.png",
    layout="centered",                  # Options: "centered" (default), "wide"
    initial_sidebar_state="expanded"    # Options: "expanded" or "collapsed"
)

about_page = st.Page(
    page="pages/about.py",
    title='About This Project',
    icon="ℹ",
    default=True
)

eda = st.Page(
    page="pages/eda_viz.py",
    title='Exploratory Data Analysis',
    icon="🔎",
)

obesity_plot = st.Page(
    page="pages/obesity_plots.py",
    title='Obesity Table Plots',
    icon="📈",
)

malnutrition_plot = st.Page(
    page="pages/malnutrition_plot.py",
    title='Malnutrition Table Plots',
    icon="📉",
)

combined_plot = st.Page(
    page="pages/combined_plot.py",
    title='Combined Table Plots',
    icon="💹",
)

pg = st.navigation(
    {
        "Info": [about_page],
        "Visualization": [eda, obesity_plot, malnutrition_plot, combined_plot]
    }
)

st.logo("assets/inside_logo.png", size="large")
st.sidebar.text("One World, Two Problems: Malnutrition and Obesity")

pg.run()