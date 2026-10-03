# Aim: To demonstrate user-defined functions with different
# arguments and the math, random and statistics modules.

import math
import random
import statistics

# No arguments
def greet():
    print("Hello! Welcome to Python.")

# Positional arguments
def add(a, b):
    return a + b

# Default argument
def greet_user(name="Student"):
    print("Hello", name)

# Keyword arguments
def introduce(name, age):
    print("Name:", name, "Age:", age)

# Variable-length arguments
def total(*numbers):
    return sum(numbers)

greet()

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
print("Sum:", add(a, b))

name = input("Enter your name: ")
greet_user(name)
introduce(age=18, name=name)

values = input("Enter numbers separated by spaces: ")
numbers = [float(v) for v in values.split()]
print("Total:", total(*numbers))

print("\nMath Module:")
print("Square root:", math.sqrt(abs(a)))
print("Ceiling:", math.ceil(a))
print("Floor:", math.floor(a))

print("\nRandom Module:")
print("Random number:", random.randint(1, 100))
print("Random choice:", random.choice(numbers))

print("\nStatistics Module:")
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))

if len(numbers) >= 2:
    print("Standard deviation:", statistics.stdev(numbers))