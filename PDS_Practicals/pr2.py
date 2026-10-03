# Aim: To demonstrate creation and manipulation of Python
# lists, tuples, sets, dictionaries and strings.

# List
n = int(input("How many list elements? "))
my_list = []

for i in range(n):
    my_list.append(input("Enter element: "))

print("\nList:", my_list)
my_list.append("New")
print("After append:", my_list)
my_list.insert(0, "First")
print("After insert:", my_list)
my_list.pop()
print("After pop:", my_list)
print("Length:", len(my_list))

# Tuple
my_tuple = tuple(my_list)
print("\nTuple:", my_tuple)
print("Count of First:", my_tuple.count("First"))
print("Index of first element:", my_tuple.index(my_tuple[0]))

# Set
my_set = set(my_list)
print("\nSet:", my_set)
my_set.add("Extra")
print("After add:", my_set)
my_set.discard("Extra")
print("After discard:", my_set)

# Dictionary
my_dict = {}
key = input("\nEnter dictionary key: ")
value = input("Enter dictionary value: ")
my_dict[key] = value
my_dict["course"] = "Python"

print("Dictionary:", my_dict)
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
my_dict.update({"status": "Active"})
print("After update:", my_dict)
my_dict.pop(key, None)
print("After pop:", my_dict)

# String
text = input("\nEnter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())
print("Capitalized:", text.capitalize())
print("Replace spaces:", text.replace(" ", "-"))
print("Split:", text.split())
print("Strip:", text.strip())
print("Length:", len(text))