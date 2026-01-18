"""
                        List Comprehension  [ ... ]

Syntax:
    [expression for item in iterable if condition]

    1. expression: The value to add to the new list (e.g., x, x*2, x.upper()).
    2. item:       The variable representing the current element.
    3. iterable:   The collection being looped over (list, range, str).
    4. condition:  (Optional) A filter; only items returning True are included.

Use Cases:
    1. Transforming data (mapping).
    2. Filtering data (selecting specific items).
    3. Flattening nested lists.
"""

print("\n---------------- List Comprehension ----------------")

squared_list_1 = []
for x in range(10):
    if x % 2 == 0:
        squared_list_1.append(x**2)

squared_list_2 = [x**2 for x in range(10) if x % 2 == 0]

print("regular loop:", squared_list_1)
print("comprehension:", squared_list_2)


"""
                    Dictionary Comprehension  { k: v ... }

Syntax:
    {key_expression : value_expression for item in iterable}

Use Cases:
    1. Inverting a dictionary (swapping keys and values).
    2. creating a lookup table from a list.
"""
print("\n---------------- Dictionary Comprehension ----------------")

people = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

bio_data = {person: age for person, age in zip(people, ages)}
print(f"bio data dict:   {bio_data}")

inverse_dict = {v: k for k, v in bio_data.items()}
print(f"inverted dict:    {inverse_dict}")


"""
                        Set Comprehension  { ... }

Syntax:
    {expression for item in iterable}

Use Cases:
    1. Finding unique values in a list.
    2. creating a set of transformed items (e.g., unique lengths of words).
"""
print("\n---------------- Set Comprehension ----------------")

fruits = ["apple", "banana", "apple", "orange", "banana", "kiwi"]

unique_fruits = {fruit for fruit in fruits}

print(f"unique fruits set: {unique_fruits}")
