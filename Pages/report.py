visualize_distributions = """
1. Obesity Distribution by Gender
    - Most obesity values fall between 5 and 20, with the highest number around 10.
    - Males generally have slightly higher obesity levels than females.
---
2. Malnutrition Distribution by Gender
    - Most malnutrition values are between 2 and 6, peaking around 3 to 4.
    - Males also show slightly higher malnutrition levels compared to females.
---
3. Key Observations
    - Both obesity and malnutrition are more common at lower values, meaning most people fall into the mild to moderate range.
    - Males have higher counts in both obesity and malnutrition categories compared to females.
    - Very high values of both malnutrition and obesity are rare, but they do exist."""

time_trends = """
1. Obesity Trend Over Years
    - The chart shows a steady and sharp increase in the average obesity estimates over the decade.
    - The average obesity rate grew from approximately 11.2 in 2012 to nearly 15.0 in 2022.
    - The growth is consistent and almost linear, indicating a worsening obesity problem year after year.
    - This rise reflects a global health concern, possibly linked to urbanization, lifestyle changes, and dietary shifts.
---
2. Malnutrition Trend Over Years
    - In contrast, the average malnutrition estimate has been gradually declining from 5.37 in 2012 to about 5.08 in 2022.
    - The decline is slow and subtle, with the curve flattening more in the later years.
    - While it's a positive sign that malnutrition is reducing, the pace is much slower than the rise in obesity.
    - This might suggest that efforts to combat undernutrition are working, but not strongly enough, especially when compared to the rapid obesity trend.
---
3. Key Observations
    - The decline in malnutrition is a positive sign, but the rapid rise in obesity is a major concern.
    - This reflects a nutrition paradox: while undernutrition issues are improving, overnutrition (obesity) is increasing significantly."""

regional_comparison = """
1. Obesity by Top 5 Regions
    - The Western Pacific and Americas show higher obesity levels with wide variation in values, including many high outliers.
    - Africa has the lowest obesity estimates, showing a tighter distribution with fewer outliers.
---
2. Malnutrition by Top 5 Regions
    - Africa has the highest malnutrition levels, with a broad spread and many extreme values.
    - Europe and the Americas show the lowest malnutrition levels, with most data clustered toward the lower end.
---
3. Key Observations
    - Obesity and malnutrition vary greatly by region, highlighting the global nutrition paradox: some regions struggle with excess while others face deficiency.
    - Regions like Africa show high malnutrition and low obesity, while regions like the Western Pacific show high obesity and lower malnutrition — indicating different public health priorities."""

gender_wise_comparison = """
1. Obesity by Gender
    - The obesity levels for Male, Female, and Both genders are very similar, with median values and spreads almost the same.
    - There are many outliers in each group, especially with high values, indicating some countries or cases with very high obesity rates.
---
2. Malnutrition by Gender
    - Male group shows a slightly higher median malnutrition level compared to Female and Both.
    - All gender categories have wider spread with many extreme outliers, especially in the Male category.
---
3. Key Observations
    - Gender doesn’t significantly impact obesity levels—the distributions are almost identical across groups.
    - For malnutrition, males appear slightly more affected on average, but the difference is small
"""

Gender_vs_Region = """
1. Obesity by Gender and Region
    - Eastern Mediterranean and Western Pacific regions show higher obesity levels across all genders, especially in the "Both" and "Female" categories.
    - Africa and South-East Asia have the lowest obesity estimates, consistently across Male, Female, and Both genders.
---
2. Malnutrition by Gender and Region
    - Africa and South-East Asia regions show higher malnutrition values in all gender categories, indicating they are most affected.
    - Europe and Americans have lower malnutrition levels across all genders, with most values clustered at the bottom.
---
3. Key Observations
    - There is a clear regional influence on both obesity and malnutrition. Some regions (like Africa) struggle more with malnutrition, while others (like Eastern Mediterranean) face obesity issues.
    - Gender alone doesn’t cause big differences, but region combined with gender reveals important health patterns.
"""

age_group_wise_comparison = """
1. Obesity by Age Group
    - Adults have clearly higher obesity estimates than children.
    - Children have lower and more consistent obesity levels with fewer extreme values.
---
2. Malnutrition by Age Group
    - Adults have slightly higher malnutrition estimates on average compared to children, as shown by a slightly higher median line in the boxplot.
    - It indicating that some children are facing more severe malnutrition.
---
3. Key Observations
    - Obesity is much more prevalent in adults, both in terms of average and variability.
    - Malnutrition affects adults slightly more on average, but children still experience notable extreme cases.
"""
Compare_Obesity_vs_Malnutrition = """
1. Key Observations
    - Malnutrition estimates are highly concentrated at lower values (mostly between 0–10), indicating it is generally present at lower levels across populations.
    - Obesity estimates have a wider distribution and extend to much higher values, showing greater variability and suggesting that some populations experience significantly higher obesity rates.
"""

CI_Width_vs_Mean_Estimate = """
- This chart shows how two numbers are related: the average value and its confidence interval (CI width).

- The color shows if they go up or down together (dark = strong relation, light = weak).

- In both obesity and malnutrition, the connection is weak, so we can trust the average values more.
"""

top_10 = """
1. Top 10 Countries – Obesity
    - American Samoa and Tonga have the highest average obesity rates, both close to 80%.
    - These countries significantly exceed global obesity levels.
---
2. Top 10 Countries – Malnutrition
    - Eritrea has the highest average malnutrition rate at approximately 35%.
---
3. Key Observations
    - Obesity is highly concentrated in Pacific Island nations like American Samoa and Tonga, suggesting regional lifestyle and dietary factors.
    - Malnutrition remains severe in low-income African nations such as Eritrea, pointing to ongoing issues with food insecurity and poverty.
"""

Nutrition_Trends = """
1. Obesity Trend Over Years by Region
    - Obesity has been increasing steadily in all regions from 2012 to 2022.
    - Africa and Western Pacific show the highest rise in obesity levels over time.
    - Regions like Europe and Eastern Mediterranean have moderate growth, but the trend is still going up.
---
2. Obesity Trend Over Years by Gender
    - All genders (Male, Female, Both) show a steady increase in obesity over time.
    - Female group has a slightly lesser obesity rate compared to males and both genders combined.
    - The increase is consistent and clear, with not much difference between genders, but still showing growth.
---
3. Obesity by Region and Gender
    - Americas and Western Pacific regions have higher obesity rates across all genders.
    - Africa and South-East Asia show lower obesity rates, regardless of gender.
    - Differences between Male, Female, and Both groups are small within each region but visible in some areas.
---
4. Obesity vs Malnutrition by Region
    - In most regions, obesity rates are higher than malnutrition (e.g., Americas, Europe, Western Pacific).
    - South-East Asia and Africa show higher malnutrition compared to obesity, which is a sign of the nutrition paradox.
    - This chart clearly shows how some regions struggle with both obesity and malnutrition at the same time, just in different groups or countries.
"""

Malnutrition_Patterns = """"
1. Malnutrition Trend Over Years by Region
    - South-East Asia has the highest malnutrition levels over time, but it is slowly decreasing.
    - Africa and Eastern Mediterranean also show higher levels, though slightly lower than South-East Asia.
    - Europe and Americas have consistently low malnutrition levels over the years.
---
2. Malnutrition Trend Over Years by Gender
    - All genders show a decreasing trend in malnutrition levels from 2012 to 2022.
    - Males have slightly higher malnutrition levels than females.
---
3. Malnutrition by Region and Gender
    - South-East Asia has high malnutrition across all genders, especially in males.
    - Africa also shows high levels, with males having the highest values.
    - Europe and Americas have the lowest malnutrition levels across genders.
---
4. Malnutrition by Region and Age Group
    - In most regions, adults have higher malnutrition levels than children.
    - South-East Asia and Africa show very high adult malnutrition compared to others.
    - Europe again shows very low levels of malnutrition for both age groups.
"""

South_Asia = """
1. Adult Obesity Trend in South Asia (Line Plot - Left Top)
    - All South Asian countries show a consistent rise in adult obesity rates from 2012 to 2022.
    - Maldives and Afghanistan have the highest obesity rates in recent years.
    - India’s Position: India shows a moderate but growing obesity trend, staying below 6% by 2022.
---
2. Adult Malnutrition Trend in South Asia (Line Plot - Right Top)
    - Adult malnutrition is decreasing steadily across all South Asian countries over time.
    - Bangladesh and Pakistan started with the highest malnutrition rates, though showing gradual improvement.
    - India’s Position: India’s malnutrition rate is reducing slowly, but it remains among the middle group in the region.
---
3. Obesity Distribution by Country (Box Plot - Bottom Left)
    - Pakistan shows the widest range and most variation in obesity values.
    - India’s obesity levels are relatively low and less varied, indicating a consistent pattern.
    - These countries have higher average obesity rates, possibly due to urban lifestyle changes.
---
4. Malnutrition Distribution by Country (Box Plot - Bottom Right)
    - India shows a wide range of malnutrition, with some extremely high cases.
    - Bhutan has the lowest levels and least variation in adult malnutrition.
    - Countries like Afghanistan and Nepal display steady mid-range levels without extreme outliers.
---
5. **About India**
    - India shows a gradual increase in adult obesity but remains below many other South Asian nations.
    - Malnutrition is decreasing over time, though it still exists significantly, especially in some regions.
    - Compared to others, India lies in the middle range for both obesity and malnutrition rates.
    - The dual burden (both obesity and malnutrition) coexists, indicating a need for balanced health interventions.
"""




