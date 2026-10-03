# Aim: To connect Python with MySQL and perform
# Create, Read, Update and Delete operations.

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="college"
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")
con.commit()

while True:
    print("\n1. Create  2. Read  3. Update  4. Delete  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        sid = int(input("Enter student ID: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        cur.execute(
            "INSERT INTO students VALUES (%s, %s, %s)",
            (sid, name, age)
        )
        con.commit()
        print("Student inserted successfully.")

    elif choice == "2":
        cur.execute("SELECT * FROM students")
        for row in cur.fetchall():
            print(row)

    elif choice == "3":
        sid = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))

        cur.execute(
            "UPDATE students SET name=%s, age=%s WHERE id=%s",
            (name, age, sid)
        )
        con.commit()
        print("Student updated.")

    elif choice == "4":
        sid = int(input("Enter student ID to delete: "))
        cur.execute("DELETE FROM students WHERE id=%s", (sid,))
        con.commit()
        print("Student deleted.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

cur.close()
con.close()
print("Database connection closed.")