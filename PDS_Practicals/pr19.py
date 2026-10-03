# Aim: To perform slicing, filtering, sorting, concatenating,
# aggregation and normalization using Pandas.

import pandas as pd

n = int(input("Enter number of records: "))
data = []

for i in range(n):
    print("\nRecord", i + 1)
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    data.append([name, marks])

df = pd.DataFrame(data, columns=["Name", "Marks"])

print("\nOriginal Data:")
print(df)

# Slicing
print("\nFirst Three Records:")
print(df.iloc[:3])

# Filtering
minimum = float(input("\nEnter minimum marks: "))
print("\nFiltered Data:")
print(df[df["Marks"] >= minimum])

# Sorting
print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# Concatenating
extra = pd.DataFrame(
    [["Extra Student", 50.0]],
    columns=["Name", "Marks"]
)

combined = pd.concat([df, extra], ignore_index=True)
print("\nConcatenated Data:")
print(combined)

# Aggregation
print("\nTotal Marks:", combined["Marks"].sum())
print("Average Marks:", combined["Marks"].mean())
print("Maximum Marks:", combined["Marks"].max())
print("Minimum Marks:", combined["Marks"].min())

# Min-Max Normalization
minimum_value = combined["Marks"].min()
maximum_value = combined["Marks"].max()

if maximum_value != minimum_value:
    combined["Normalized"] = (
        (combined["Marks"] - minimum_value)
        / (maximum_value - minimum_value)
    )
else:
    combined["Normalized"] = 0.0

print("\nNormalized Data:")
print(combined)# Aim: To perform slicing, filtering, sorting, concatenating,
# aggregation and normalization using Pandas.

import pandas as pd

n = int(input("Enter number of records: "))
data = []

for i in range(n):
    print("\nRecord", i + 1)
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    data.append([name, marks])

df = pd.DataFrame(data, columns=["Name", "Marks"])

print("\nOriginal Data:")
print(df)

# Slicing
print("\nFirst Three Records:")
print(df.iloc[:3])

# Filtering
minimum = float(input("\nEnter minimum marks: "))
print("\nFiltered Data:")
print(df[df["Marks"] >= minimum])

# Sorting
print("\nSorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

# Concatenating
extra = pd.DataFrame(
    [["Extra Student", 50.0]],
    columns=["Name", "Marks"]
)

combined = pd.concat([df, extra], ignore_index=True)
print("\nConcatenated Data:")
print(combined)

# Aggregation
print("\nTotal Marks:", combined["Marks"].sum())
print("Average Marks:", combined["Marks"].mean())
print("Maximum Marks:", combined["Marks"].max())
print("Minimum Marks:", combined["Marks"].min())

# Min-Max Normalization
minimum_value = combined["Marks"].min()
maximum_value = combined["Marks"].max()

if maximum_value != minimum_value:
    combined["Normalized"] = (
        (combined["Marks"] - minimum_value)
        / (maximum_value - minimum_value)
    )
else:
    combined["Normalized"] = 0.0

print("\nNormalized Data:")
print(combined)