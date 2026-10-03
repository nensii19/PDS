# Aim: To perform read, write and append operations on
# text, CSV and binary files.

import csv
import pickle

# Text file: Write
with open("data.txt", "w") as file:
    file.write(input("Enter text to save: ") + "\n")

# Text file: Append
with open("data.txt", "a") as file:
    file.write(input("Enter additional text: ") + "\n")

# Text file: Read
with open("data.txt", "r") as file:
    print("\nText File Content:")
    print(file.read())

# CSV file: Write
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    n = int(input("\nHow many people? "))

    for i in range(n):
        name = input("Enter name: ")
        age = input("Enter age: ")
        writer.writerow([name, age])

# CSV file: Append
with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        input("Enter one more name: "),
        input("Enter age: ")
    ])

# CSV file: Read
with open("data.csv", "r") as file:
    print("\nCSV File Content:")
    print(file.read())

# Binary file: Write
data = input("\nEnter data for binary file: ")
with open("data.bin", "wb") as file:
    pickle.dump(data, file)

# Binary file: Append
with open("data.bin", "ab") as file:
    pickle.dump(input("Enter more binary data: "), file)

# Binary file: Read all saved objects
print("\nBinary File Content:")
with open("data.bin", "rb") as file:
    while True:
        try:
            print(pickle.load(file))
        except EOFError:
            break