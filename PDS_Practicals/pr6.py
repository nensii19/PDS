# Aim: To demonstrate try, except, else, finally,
# raise and custom exceptions.

class NegativeNumberError(Exception):
    pass

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    if a < 0 or b < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")

    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

except NegativeNumberError as e:
    print("Custom Error:", e)

else:
    print("Division result:", result)

finally:
    print("Exception handling completed.")