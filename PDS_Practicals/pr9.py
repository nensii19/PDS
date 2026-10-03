# Aim: To demonstrate the data science life cycle and perform
# univariate, bivariate and multivariate analysis.

import pandas as pd

# 1. Data collection
n = int(input("Enter number of students: "))
records = []

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    hours = float(input("Enter study hours: "))
    attendance = float(input("Enter attendance percentage: "))

    records.append([name, marks, hours, attendance])

# 2. Data preparation
df = pd.DataFrame(
    records,
    columns=["Name", "Marks", "StudyHours", "Attendance"]
)

print("\nDataset:")
print(df)

# 3. Data cleaning
df = df.drop_duplicates()
df = df.dropna()

# 4. Univariate analysis: one variable
print("\nUnivariate Analysis - Marks:")
print(df["Marks"].describe())

# 5. Bivariate analysis: two variables
print("\nBivariate Analysis:")
print(df[["StudyHours", "Marks"]].corr())

# 6. Multivariate analysis: multiple variables
print("\nMultivariate Analysis:")
print(df[["Marks", "StudyHours", "Attendance"]].describe())
print(df[["Marks", "StudyHours", "Attendance"]].corr())

# 7. Interpretation
if len(df) >= 2:
    correlation = df["StudyHours"].corr(df["Marks"])
    print("\nStudy Hours and Marks Correlation:", correlation)

    if correlation > 0:
        print("The variables have a positive relationship.")
    elif correlation < 0:
        print("The variables have a negative relationship.")
    else:
        print("No linear correlation was found.")

# 8. Save results
df.to_csv("student_analysis.csv", index=False)
print("Cleaned dataset saved to student_analysis.csv")