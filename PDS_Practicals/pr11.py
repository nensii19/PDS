# Aim: To create Pandas Series and DataFrames and perform
# selection, filtering, grouping and aggregation.

import pandas as pd

# Series
n = int(input("Enter number of values for Series: "))
values = []

for i in range(n):
    values.append(float(input("Enter value: ")))

series = pd.Series(values)
print("\nSeries:")
print(series)

# DataFrame
rows = int(input("\nEnter number of records: "))
data = []

for i in range(rows):
    print("\nRecord", i + 1)
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    data.append([name, department, salary])

df = pd.DataFrame(
    data,
    columns=["Name", "Department", "Salary"]
)

print("\nDataFrame:")
print(df)

# Selection
print("\nName Column:")
print(df["Name"])

# Filtering
minimum = float(input("Show salaries greater than: "))
print(df[df["Salary"] > minimum])

# Grouping and aggregation
if not df.empty:
    print("\nDepartment-wise Average Salary:")
    print(df.groupby("Department")["Salary"].mean())

    print("\nDepartment-wise Summary:")
    print(df.groupby("Department")["Salary"].agg(
        ["count", "sum", "mean", "max", "min"]
    ))