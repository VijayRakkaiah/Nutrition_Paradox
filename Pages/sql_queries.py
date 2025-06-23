query_1 = """
SELECT Region, AVG(Mean_Estimate) AS Avg_Obesity
FROM obesity
WHERE Year = 2022
GROUP BY Region
ORDER BY Avg_Obesity DESC
LIMIT 5
"""

query_2 = """
SELECT Country, MAX(Mean_Estimate) AS Max_Obesity
FROM obesity
GROUP BY Country
ORDER BY Max_Obesity DESC
LIMIT 5
"""

query_3 = """
SELECT Year, AVG(Mean_Estimate) AS Avg_Obesity
FROM obesity
WHERE Country = 'India'
GROUP BY Year
ORDER BY Year
"""

query_4 = """
SELECT Gender, AVG(Mean_Estimate) AS Avg_Obesity
FROM obesity
GROUP BY Gender
"""

query_5 = """
SELECT Obesity_level, age_group, COUNT(DISTINCT Country) AS country_count
FROM obesity
GROUP BY Obesity_level, age_group
"""

query_6_1 = """
SELECT Country, AVG(CI_Width) AS Avg_CI
FROM obesity
GROUP BY Country
ORDER BY Avg_CI DESC
LIMIT 5
"""

query_6_2 = """
SELECT Country, AVG(CI_Width) AS Avg_CI
FROM obesity
GROUP BY Country
ORDER BY Avg_CI ASC
LIMIT 5
"""

query_7 = """
SELECT age_group, AVG(Mean_Estimate) AS Avg_Obesity
FROM obesity
GROUP BY age_group
"""

query_8 = """
SELECT Country, AVG(Mean_Estimate) AS Avg_Obesity, AVG(CI_Width) AS Avg_CI
FROM obesity
GROUP BY Country
HAVING Avg_Obesity < 10 AND Avg_CI < 5
ORDER BY Avg_Obesity ASC
LIMIT 10
"""

query_9 = """
SELECT o1.Country,
       AVG(o1.Mean_Estimate - o2.Mean_Estimate) AS Avg_Difference
FROM obesity o1
JOIN obesity o2
  ON o1.Country = o2.Country
     AND o1.Year = o2.Year
     AND o1.age_group = o2.age_group
WHERE o1.Gender = 'Female' AND o2.Gender = 'Male'
GROUP BY o1.Country
ORDER BY Avg_Difference DESC
LIMIT 10
"""

query_10 = """
SELECT Year, AVG(Mean_Estimate) AS Global_Avg_Obesity
FROM obesity
GROUP BY Year
ORDER BY Year
"""

query_11 = """
SELECT age_group, AVG(Mean_Estimate) AS Avg_Malnutrition
FROM malnutrition
GROUP BY age_group
"""

query_12 = """
SELECT Country, MAX(Mean_Estimate) AS Max_Malnutrition
FROM malnutrition
GROUP BY Country
ORDER BY Max_Malnutrition DESC
LIMIT 5
"""

query_13 = """
SELECT Year, AVG(Mean_Estimate) AS Avg_Malnutrition
FROM malnutrition
WHERE Region = 'Africa'
GROUP BY Year
ORDER BY Year
"""

query_14 = """
SELECT Gender, AVG(Mean_Estimate) AS Avg_Malnutrition
FROM malnutrition
GROUP BY Gender
"""

query_15 = """
SELECT Malnutrition_Level, age_group, AVG(CI_Width) AS Avg_CI_Width
FROM malnutrition
GROUP BY Malnutrition_Level, age_group
"""

query_16 = """
SELECT Country, Year, AVG(Mean_Estimate) AS Avg_Malnutrition
FROM malnutrition
WHERE Country IN ('India', 'Nigeria', 'Brazil')
GROUP BY Country, Year
ORDER BY Country, Year
"""

query_17 = """
SELECT Region, AVG(Mean_Estimate) AS Avg_Malnutrition
FROM malnutrition
GROUP BY Region
ORDER BY Avg_Malnutrition ASC
"""

query_18 = """
SELECT Country,
       MIN(Mean_Estimate) AS Min_Malnutrition,
       MAX(Mean_Estimate) AS Max_Malnutrition
FROM malnutrition
GROUP BY Country
HAVING MAX(Mean_Estimate) - MIN(Mean_Estimate) > 0
"""

query_19 = """
SELECT Year,
       MIN(Mean_Estimate) AS Min_Level,
       MAX(Mean_Estimate) AS Max_Level
FROM malnutrition
GROUP BY Year
ORDER BY Year
"""

query_20 = """
SELECT *
FROM malnutrition
WHERE CI_Width > 5
"""

query_21 = """
SELECT o.Country, o.Year, o.Mean_Estimate AS Obesity, m.Mean_Estimate AS Malnutrition
FROM obesity o
JOIN malnutrition m
  ON o.Country = m.Country AND o.Year = m.Year AND o.Gender = m.Gender AND o.age_group = m.age_group
WHERE o.Country IN ('India', 'Brazil', 'Nigeria', 'Sri Lanka', 'Bangladesh')
"""

query_22 = """
SELECT o.Gender,
       AVG(o.Mean_Estimate) AS Avg_Obesity,
       AVG(m.Mean_Estimate) AS Avg_Malnutrition
FROM obesity o
JOIN malnutrition m
  ON o.Country = m.Country AND o.Year = m.Year AND o.Gender = m.Gender AND o.age_group = m.age_group
GROUP BY o.Gender
"""

query_23 = """
SELECT o.Region,
       AVG(o.Mean_Estimate) AS Avg_Obesity,
       AVG(m.Mean_Estimate) AS Avg_Malnutrition
FROM obesity o
JOIN malnutrition m
  ON o.Country = m.Country AND o.Year = m.Year AND o.Gender = m.Gender AND o.age_group = m.age_group
WHERE o.Region IN ('Africa', 'Americas')
GROUP BY o.Region
"""

query_24 = """
SELECT o.Country,
       MAX(o.Mean_Estimate) - MIN(o.Mean_Estimate) AS Obesity_Increase,
       MAX(m.Mean_Estimate) - MIN(m.Mean_Estimate) AS Malnutrition_Change
FROM obesity o
JOIN malnutrition m
  ON o.Country = m.Country AND o.Year = m.Year AND o.Gender = m.Gender AND o.age_group = m.age_group
GROUP BY o.Country
"""

query_25 = """
SELECT o.Year, o.age_group,
       AVG(o.Mean_Estimate) AS Avg_Obesity,
       AVG(m.Mean_Estimate) AS Avg_Malnutrition
FROM obesity o
JOIN malnutrition m
  ON o.Country = m.Country AND o.Year = m.Year AND o.Gender = m.Gender AND o.age_group = m.age_group
GROUP BY o.Year, o.age_group
ORDER BY o.Year, o.age_group
"""





