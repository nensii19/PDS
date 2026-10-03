# Aim: To demonstrate if, if-else, elif, while, for,
# nested loops and break, continue and pass statements.

num = int(input("Enter a number: "))

# if
if num > 0:
    print("Number is positive")

# if-else
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-elif-else
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# while loop
print("\nWhile Loop:")
i = 1
while i <= abs(num):
    print(i, end=" ")
    i += 1

# for loop
print("\n\nFor Loop:")
for i in range(1, abs(num) + 1):
    print(i, end=" ")

# Nested loop
print("\n\nNested Loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()

# break
print("\nBreak Example:")
for i in range(1, 6):
    if i == 4:
        break
    print(i, end=" ")

# continue
print("\nContinue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")

# pass
print("\nPass Example:")
if num >= 0:
    pass
print("Program completed")