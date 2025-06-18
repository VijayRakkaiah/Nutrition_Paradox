import streamlit as st


st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <style>
    .custom-title {
        font-family: 'Caveat', cursive;
        font-size: 40px;
        color: #50C878	;
        text-align: center;
    }
    </style>
    <div class="custom-title">🥗 About This Project 🌍</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style="text-align: justify; font-size: 16px;">
This project explores the <strong>Nutrition Paradox</strong> — the coexistence of <strong>obesity</strong> and <strong>malnutrition</strong> in different parts of the world.  
Using <strong>WHO public datasets</strong>, we investigate global health trends by analyzing factors like <strong>gender, age, region, and time</strong>.  
The goal is to uncover insights that can support data-driven decisions in public health planning.
</div>
""", unsafe_allow_html=True)


st.markdown("""
---

### 🧭 What You Can Do:
- 🔍 **Analyze obesity and malnutrition** across regions, genders, and age groups  
- 📈 **Visualize trends** using interactive charts and SQL-driven insights  
- 🗃️ **Explore 25 SQL queries** powering this dashboard  
- 📊 **Compare data** between countries and demographics  

---

### 🛠️ Tools & Tech Stack:
- 🐍 **Python**
- 📦 **Pandas**, **Matplotlib**, **Seaborn**, **Plotly**
- 🖥️ **Streamlit** (for the dashboard interface)
- 🗄️ **MySQL** (for structured data storage and queries)
- 🔌 **PyMySQL** (connecting Python to MySQL)
- 📊 **Power BI** (for report building)
- 🎨 **HTML/CSS** (for styling and layout)

---

### 👨‍💻 About Me
Hi! I'm **Vijay Rakkaiah**, a data analyst and design engineer passionate about turning data into meaningful solutions.  
This project is part of my learning journey in data science, focusing on global nutrition and public health.

📫 **Contact Me**  
✉️ Email: [vijay.rakkaiah@gmail.com](mailto:vijay.rakkaiah@gmail.com)

🔗 **Connect With Me**  
[GitHub](https://github.com/VijayRakkaiah) | [LinkedIn](https://www.linkedin.com/in/vijay-rakkaiah-79a8b21b1/)

---

<div style="text-align: center;">
  ✨ <i>Thank you for exploring the Nutrition Paradox with me!</i> ✨<br>
  <i>Let’s use data to drive better health outcomes worldwide.</i>
</div>
""", unsafe_allow_html=True)
