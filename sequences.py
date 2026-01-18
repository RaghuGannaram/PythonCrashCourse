"""
                        Common Sequence Operations
            (list, tuple, str, range, bytes, bytearray)

Description:
    These operations work on both mutable and immutable sequences.
    They generally return a new value or information without modifying the original object.

Supported Operators:
    x in s           : True if item x is found in s.
    x not in s       : True if item x is NOT found in s.
    s + t            : Concatenation (joins two sequences of the SAME type).
    s * n            : Repetition (adds s to itself n times).
    s[i]             : Indexing (get item at position i).
    s[i:j]           : Slicing (get items from i to j).
    s[i:j:k]         : Slicing (get items from i to j with step k).
    len(s)           : Returns the number of items.
    min(s)           : Returns the smallest item (items must be comparable).
    max(s)           : Returns the largest item.
    s.index(x)       : Returns index of the first occurrence of x.
    s.count(x)       : Returns total number of occurrences of x.

Edge Cases / Notes:
    1. Concatenation (+): You cannot add different types (e.g., list + tuple raises TypeError).
    2. Slicing ([i:j]): Indexes out of bounds are handled gracefully (no error), unlike direct Indexing.
    3. Indexing ([i]): Raises IndexError if i is out of bounds.
    4. Repetition (*): n <= 0 results in an empty sequence.
"""

print("\n---------------- Common Sequence Operations ----------------")

# Demo using a Tuple (The "Universal" Sequence)
planets = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
)

print(f"Planets Tuple:     {planets}\n")
# --- Membership ---
print(f"Contains 'Earth'?  {'Earth' in planets}")
print(f"Missing 'Pluto'?   {'Pluto' not in planets}")

# --- Concatenation & Repetition ---
# Note: Creates NEW objects. Original 'planets' is unchanged.
print(f"Concatenation:     {planets + ('Pluto',)}")
print(f"Repetition (*2):   {planets * 2}")

# --- Indexing & Slicing ---
print(f"Index [2]:         {planets[2]}")
print(f"Negative [-1]:     {planets[-1]}")
print(f"Slice [1:5:2]:     {planets[1:5:2]}")
print(f"Reverse [::-1]:    {planets[::-1]}")

# --- Statistics ---
print(f"Length:            {len(planets)}")
print(f"Min (Lexical):     {min(planets)}")  # Alphabetically first ('Earth')
print(f"Max (Lexical):     {max(planets)}")  # Alphabetically last ('Venus')

# --- Methods ---
print(f"Index of 'Mars':   {planets.index('Mars')}")
print(f"Count of 'Earth':  {planets.count('Earth')}")

print("\n[Edge Case: Out of bounds slicing]")
# Slicing is forgiving; it just returns what it can find.
print(f"Slice [100:200]:   {planets[100:200]} (Returns empty, no error)")

print("\n[Edge Case: Concatenation Type Mismatch]")
try:
    print(planets + ["Pluto"])  # Tuple + List
except TypeError as e:
    print(f"Error: {e} (Cannot concatenate list to tuple)")


"""
                    Immutable Sequence Operations
                    (tuple, str, range, bytes)

Unique Feature: Hashing
    Immutable sequences support the hash() built-in function (provided their contents are also hashable).

Use Case:
    Because they are hashable, they can be used as:
    1. Keys in a dictionary.
    2. Members of a set.
    
    (Lists cannot be used for either of these).
"""
print("\n---------------- 2. Immutable Sequence Operations ----------------")

# Tuple (Immutable)
coordinate = (10, 20)
print(f"Tuple Hash:      {hash(coordinate)}")

# Using Tuple as a Dict Key
locations = {(10, 20): "Home", (30, 40): "Work"}
print(f"Dict Lookup:     {locations[(10, 20)]}")

# Edge Case: Immutable container holding Mutable data
# A tuple is only hashable if ALL its items are hashable.
bad_tuple = (1, 2, [3, 4])  # Contains a list
try:
    print(hash(bad_tuple))
except TypeError as e:
    print(f"Edge Case Error: {e}")
    print("(Tuple became unhashable because it contains a mutable list)")


"""
                    Mutable Sequence Operations
                        (list, bytearray)

Description:
    Operations that change the content of the sequence directly.

Supported Operators:
    s[i] = x         : Item assignment (replace value).
    s[i:j] = t       : Slice assignment (replace a range with an iterable).
    del s[i]         : Delete item at index.
    del s[i:j]       : Delete slice.
    s += t           : In-place concatenation (same as extend).
    s *= n           : In-place repetition.

Methods:
    s.append(x)      : Add item to end.
    s.clear()        : Remove all items.
    s.copy()         : Return shallow copy.
    s.extend(t)      : Add contents of iterable t to end.
    s.insert(i, x)   : Insert x at index i.
    s.pop(i)         : Remove and return item at i (default last).
    s.remove(x)      : Remove first occurrence of x.
    s.reverse()      : Reverse in place.
"""
print("\n---------------- 3. Mutable Sequence Operations ----------------")

# Demo using a List
my_list = ["alpha", "beta", "gamma", "delta"]
print(f"Original:        {my_list}")

# --- Item & Slice Assignment ---
my_list[1] = "BRAVO"
my_list[2:] = ["charlie", "echo"]
print(f"After Assign:    {my_list}")

# --- Deletion ---
del my_list[0]
print(f"After Delete:    {my_list}")

# --- Methods ---
my_list.append("foxtrot")
my_list.insert(0, "start")
print(f"After Add:       {my_list}")

popped = my_list.pop()
print(f"Popped Item:     '{popped}'")

my_list.reverse()
print(f"Reversed:        {my_list}")

print("\n[Edge Case: Remove missing item]")
try:
    my_list.remove("ZULU")
except ValueError as e:
    print(f"Error: {e} (Cannot remove item that doesn't exist)")


"""
--------------------------- List Nuances ---------------------------
1. Sorting:
   - list.sort(): Sorts IN-PLACE. Returns None. 
   - sorted(list): Creates a NEW list.
   
2. Reference Trap:
   - [[]] * 3 creates references to the SAME object.
"""
print("\n---------------- 4A. List Specifics ----------------")

# Sorting
nums = [3, 1, 2]
nums.sort()
print(f"In-Place Sort:   {nums}")

# The Reference Trap (Edge Case)
trap = [[]] * 3
trap[0].append(99)
print(f"Reference Trap:  {trap} (All items changed!)")


"""
--------------------------- Tuple Nuances ---------------------------
1. Construction:
   - A single item requires a comma: (1,) is a tuple, (1) is an int.
   - Parentheses are often optional.
"""
print("\n---------------- 4B. Tuple Specifics ----------------")

not_tuple = "hello"  # This is a String
real_tuple = ("hello",)  # This is a Tuple
print(f"('hello') type:  {type(not_tuple)}")
print(f"('hello',) type: {type(real_tuple)}")


"""
--------------------------- Range Nuances ---------------------------
1. Efficiency:
   - Ranges are lazy. range(1000000) takes the same memory as range(1).
2. Equality:
   - Ranges are equal if they generate the same sequence, even if params differ.
3. Restrictions:
   - No concatenation (+) or repetition (*).
"""
print("\n---------------- 4C. Range Specifics ----------------")

# Equality Logic
r1 = range(0)  # Empty
r2 = range(10, 5, 2)  # Empty (start > stop with pos step)
print(f"Empty Ranges Eq: {r1 == r2} (Both represent empty sequences)")

# Concatenation Error
try:
    print(range(10) + range(10))
except TypeError as e:
    print(f"Error: {e} (Ranges cannot be concatenated)")
