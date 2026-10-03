# Aim: To detect and handle missing values, remove duplicate
# records and treat outliers in a dataset using Pandas.

import pandas as pd

n = int(input("Enter number of records: "))
data = []

for i in range(n):
    print("\nRecord", i + 1)
    name = input("Enter name (or leave blank): ")
    value = input("Enter numerical value (or leave blank): ")

    if value.strip() == "":
        value = None
    else:
        value = float(value)

    data.append([name, value])

df = pd.DataFrame(data, columns=["Name", "Value"])

print("\nOriginal Dataset:")
print(df)

# Detect missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["Name"] = df["Name"].replace("", pd.NA)
df["Name"] = df["Name"].fillna("Unknown")
df["Value"] = df["Value"].fillna(df["Value"].median())

# Remove duplicate records
df = df.drop_duplicates()

# Detect outliers using IQR
q1 = df["Value"].quantile(0.25)
q3 = df["Value"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[
    (df["Value"] < lower) | (df["Value"] > upper)
]

print("\nDetected Outliers:")
print(outliers)

# Handle outliers by capping them
df["Value"] = df["Value"].clip(lower, upper)

print("\nCleaned Dataset:")
print(df)

df.to_csv("cleaned_data.csv", index=False)
print("Cleaned data saved to cleaned_data.csv")# Aim: To detect and handle missing values, remove duplicate
# records and treat outliers in a dataset using Pandas.

import pandas as pd

n = int(input("Enter number of records: "))
data = []

for i in range(n):
    print("\nRecord", i + 1)
    name = input("Enter name (or leave blank): ")
    value = input("Enter numerical value (or leave blank): ")

    if value.strip() == "":
        value = None
    else:
        value = float(value)

    data.append([name, value])

df = pd.DataFrame(data, columns=["Name", "Value"])

print("\nOriginal Dataset:")
print(df)

# Detect missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["Name"] = df["Name"].replace("", pd.NA)
df["Name"] = df["Name"].fillna("Unknown")
df["Value"] = df["Value"].fillna(df["Value"].median())

# Remove duplicate records
df = df.drop_duplicates()

# Detect outliers using IQR
q1 = df["Value"].quantile(0.25)
q3 = df["Value"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[
    (df["Value"] < lower) | (df["Value"] > upper)
]

print("\nDetected Outliers:")
print(outliers)

# Handle outliers by capping them
df["Value"] = df["Value"].clip(lower, upper)

print("\nCleaned Dataset:")
print(df)

df.to_csv("cleaned_data.csv", index=False)
print("Cleaned data saved to cleaned_data.csv")