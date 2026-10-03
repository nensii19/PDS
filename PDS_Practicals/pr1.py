# Aim: To demonstrate variables, data types and all Python operators.

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
x = float(input("Enter a decimal number: "))
name = input("Enter your name: ")
flag = bool(int(input("Enter 1 for True or 0 for False: ")))

print("\nData Types:")
print(a, type(a))
print(x, type(x))
print(name, type(name))
print(flag, type(flag))

# Arithmetic Operators
print("\nArithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division by zero is not allowed.")
print("Power:", a ** b)

# Assignment Operators
c = a
c += b
print("\nAssignment += :", c)
c -= b
print("Assignment -= :", c)
c *= b
print("Assignment *= :", c)

# Comparison Operators
print("\nComparison Operators:")
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# Logical Operators
print("\nLogical Operators:")
print(a > 0 and b > 0)
print(a > 0 or b > 0)
print(not (a > 0))

# Membership Operators
text = input("\nEnter text: ")
word = input("Enter word to search: ")
print(word in text)
print(word not in text)

# Identity Operators
p = [1, 2]
q = p
r = [1, 2]
print("\nIdentity Operators:")
print(p is q)
print(p is r)
print(p is not r)

# Bitwise Operators
print("\nBitwise Operators:")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)