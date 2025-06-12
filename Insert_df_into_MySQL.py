import pandas as pd
import pymysql

# Connect to MySQL Server (not a specific database yet)
my_connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root'
)

cursor = my_connection.cursor()

# Create the database
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS nutrition_paradox;")
    my_connection.commit()  # Commit database creation
except pymysql.Error as e:
    print(f"Error creating database: {e}")

# Select the database
try:
    cursor.execute("USE nutrition_paradox;")
except pymysql.Error as e:
    print(f"Error selecting database: {e}")

# Create tables
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS obesity (
            region VARCHAR(100),
            gender VARCHAR(10),
            year INT,
            lower_bound FLOAT,
            upper_bound FLOAT,
            mean_estimate FLOAT,
            country VARCHAR(100),
            age_group VARCHAR(50),
            CI_width FLOAT,
            obesity_level VARCHAR(50))'''
        )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS malnutrition (
            region VARCHAR(100),
            gender VARCHAR(10),
            year INT,
            lower_bound FLOAT,
            upper_bound FLOAT,
            mean_estimate FLOAT,
            country VARCHAR(100),
            age_group VARCHAR(50),
            CI_width FLOAT,
            malnutrition_level VARCHAR(50))'''
        )
    my_connection.commit()  # Commit table creation
except pymysql.Error as e:
    print(f"Error creating tables: {e}")

# Load the data from CSV
try:
    df_obesity = pd.read_csv('df_obesity.csv')
    df_malnutrition = pd.read_csv('df_malnutrition.csv')
except FileNotFoundError as e:
    print(f"Error loading CSV files: {e}")

# Insert Data using .iterrows()
# 1. Insert into obesity table
try:
    for _, row in df_obesity.iterrows():
        cursor.execute("""
            INSERT INTO obesity (region, gender, year, lower_bound, upper_bound, 
            mean_estimate, country, age_group, CI_width, obesity_level)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Region'], row['Gender'], row['Year'], row['LowerBound'], row['UpperBound'],
            row['Mean_Estimate'], row['Country'], row['age_group'], row['CI_Width'], row['Obesity_level']
        ))

# 2. Insert into malnutrition table
    for _, row in df_malnutrition.iterrows():
        cursor.execute("""
                INSERT INTO malnutrition (region, gender, year, lower_bound, upper_bound, 
                mean_estimate, country, age_group, CI_width, malnutrition_level)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
            row['Region'], row['Gender'], row['Year'], row['LowerBound'], row['UpperBound'],
            row['Mean_Estimate'], row['Country'], row['age_group'], row['CI_Width'], row['Malnutrition_Level']
        ))
except pymysql.Error as e:
    print(f"Insert Error: {e}")

my_connection.commit()

# Close Connection
cursor.close()
my_connection.close()




