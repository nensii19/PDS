# Aim: To demonstrate NumPy arrays, indexing, slicing,
# reshaping, broadcasting and mathematical operations.

import numpy as np

n = int(input("Enter number of elements: "))
values = []

for i in range(n):
    values.append(float(input("Enter number: ")))

arr = np.array(values)

print("\nArray:", arr)
print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("Slicing:", arr[0:min(3, n)])
print("Array Shape:", arr.shape)
print("Number of Dimensions:", arr.ndim)

# Reshape if the element count allows it
if n > 0 and n % 2 == 0:
    matrix = arr.reshape(2, n // 2)
    print("\nReshaped Array:\n", matrix)

    # Broadcasting
    print("Array + 10:\n", matrix + 10)
    print("Array * 2:\n", matrix * 2)

# Mathematical operations
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Square:", np.square(arr))
print("Square Root of Absolute Values:", np.sqrt(np.abs(arr)))# Aim: To demonstrate NumPy arrays, indexing, slicing,
# reshaping, broadcasting and mathematical operations.

import numpy as np

n = int(input("Enter number of elements: "))
values = []

for i in range(n):
    values.append(float(input("Enter number: ")))

arr = np.array(values)

print("\nArray:", arr)
print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("Slicing:", arr[0:min(3, n)])
print("Array Shape:", arr.shape)
print("Number of Dimensions:", arr.ndim)

# Reshape if the element count allows it
if n > 0 and n % 2 == 0:
    matrix = arr.reshape(2, n // 2)
    print("\nReshaped Array:\n", matrix)

    # Broadcasting
    print("Array + 10:\n", matrix + 10)
    print("Array * 2:\n", matrix * 2)

# Mathematical operations
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Square:", np.square(arr))
print("Square Root of Absolute Values:", np.sqrt(np.abs(arr)))