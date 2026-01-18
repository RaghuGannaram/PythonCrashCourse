"""
                        Set Types
                    (set, frozenset)

Description:
    Unordered collections of distinct hashable objects.
    - set       : Mutable (can add/remove). Unhashable.
    - frozenset : Immutable (read-only). Hashable (can be dict key).

1. Common Operations (set & frozenset):
    len(s)          : Cardinality (number of elements).
    x in s          : Membership testing.
    s.copy()        : Shallow copy.
    s.isdisjoint(t) : True if no common elements.
    s.issubset(t)   : True if all elements of s are in t (s <= t).
    s.issuperset(t) : True if all elements of t are in s (s >= t).

    Math Operators (Require both sides to be sets):
    s | t   : Union (OR)
    s & t   : Intersection (AND)
    s - t   : Difference
    s ^ t   : Symmetric Difference (XOR)

    Math Methods (Accept any iterable as argument):
    s.union(t), s.intersection(t), s.difference(t), s.symmetric_difference(t)

2. Mutable Operations (set ONLY):
    s.add(x)        : Add element x.
    s.remove(x)     : Remove x (Raises KeyError if missing).
    s.discard(x)    : Remove x (No error if missing).
    s.pop()         : Remove and return arbitrary element.
    s.clear()       : Remove all elements.

    In-Place Updates:
    s |= t, s &= t, s -= t, s ^= t

Note:
    - Sets do not support indexing (s[0]) or slicing.
    - Elements must be hashable (no lists inside sets).
    - {} creates an empty DICT, not a set. Use set() for empty set.
"""

print("\n---------------- 1. Common Set Operations (set & frozenset) ----------------")
# We use frozenset for the demo to prove these work on IMMUTABLE types too.

fruits = frozenset({"apple", "banana", "cherry", "kiwi"})
fiber_rich = frozenset(
    {
        "banana",
    }
)
vegetables = frozenset({"carrot", "lettuce"})

print(f"Membership (in):      {'apple' in fruits}")

# --- Comparisons ---
print(f"Is Disjoint (method):  {fruits.isdisjoint(vegetables)}")
print(f"Is Subset (method):    {fiber_rich.issubset(fruits)}")
print(f"Is Subset (<=):        {fiber_rich <= fruits}")
print(f"Is Superset (method):  {fruits.issuperset(fiber_rich)}")
print(f"Is Superset (>=):      {fruits >= fiber_rich}")

A = frozenset({1, 2, 3, 4})
B = frozenset({3, 4, 5, 6})

# --- Mathematical Logic ---
print(f"Union (method):        {A.union(B)}")
print(f"Union (|):             {A | B}")
print(f"Intersection (method): {A.intersection(B)}")
print(f"Intersection (&):      {A & B}")
print(f"Difference (method):   {A.difference(B)}")
print(f"Difference (-):        {A - B}")
print(f"Sym. Diff (method):    {A.symmetric_difference(B)}")
print(f"Sym. Diff (^):         {A ^ B}")

print(fruits | vegetables)
try:
    print(fruits | ["kiwi", "spinach"])  # '|' requires both operands to be sets
except TypeError as error:
    print(f"Error: {error} (Operator requires both operands to be sets)")

print(fruits.union(["kiwi", "spinach"]))  # math method accepts any iterable

# --- Operator vs Method Nuance ---
# Operator: Requires both to be sets
# print(A & [3, 4])  <-- TypeError

# Method: Accepts any iterable (list, tuple, range)
print(f"Method (with list):    {A.intersection([3, 4])}")


print("\n---------------- 2. Mutable Operations (set ONLY) ----------------")

stars = {"Sirius", "Canopus", "Arcturus"}
print(f"Original Set:          {stars}")
stars.add("Vega")
print(f"After Add:             {stars}")
stars.remove("Canopus")
print(f"After Remove:          {stars}")
try:
    stars.remove("Betelgeuse")  # Raises KeyError
except KeyError as error:
    print(f"Error: {error} (Cannot remove missing element)")
stars.discard("Betelgeuse")  # No error
print(f"After Discard:         {stars}")
popped_star = stars.pop()
print(f"Popped Star:           {popped_star}")
print(f"After Pop:             {stars}")
stars.clear()
print(f"After Clear:           {stars}")


print("\n---------------- 3. Edge Cases & Type Nuances ----------------")

# 1. The Empty Set Trap
empty_dict = {}  # This is a dict!
empty_set = set()  # This is a set.
print(f"Type of {{}}:       {type(empty_dict)}")

# 2. Mixed Type Operations
# The result type matches the Left Operand.
s = {1, 2}
f = frozenset({3, 4})

print(f"set | frozenset:     {type(s | f)}")  # <class 'set'>
print(f"frozenset | set:     {type(f | s)}")  # <class 'frozenset'>

# 3. Hashability (Why frozenset exists)
# Sets cannot contain mutable items (like lists or other sets).
try:
    nested = {{1, 2}, {3, 4}}
except TypeError as e:
    print(f"Error: {e} (Cannot nest mutable sets)")

# Solution: Use frozenset for nested sets
valid_nested = {frozenset({1, 2}), frozenset({3, 4})}
print(f"Valid Nested:    {valid_nested}")


# Mutable list: NO hash method
try:
    print(hash([1, 2]))
except TypeError as e:
    print(f"List error: {e}")
    # Output: unhashable type: 'list'

# Immutable frozenset: HAS hash method
print(f"Frozenset hash: {hash(frozenset([1, 2]))}")
# Output: Some integer (e.g., -684523...)
