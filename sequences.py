"""
                        Common Sequence Operations
                        (list, tuple, str, range)

Supported Operators:
    x in s          : True if item x is found in s.
    x not in s      : True if item x is NOT found in s.
    s + t           : Concatenation (joins two sequences).
    s * n           : Repetition (adds s to itself n times).
    s[i]            : Indexing (get item at position i).
    s[i:j:k]        : Slicing (get items from i to j with step k).
    len(s)          : Length of s.
    min(s), max(s)  : Smallest and largest item.
    s.index(x)      : Index of the first occurrence of x.
    s.count(x)      : Total number of occurrences of x.

Note:
    - Concatenation (+) and Repetition (*) create NEW objects; they do not modify the original.
    - Indexing is 0-based. Negative indices count from the end (-1 is the last item).
"""

print("\n---------------- Common Sequence Operations ----------------")

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

print("Earth" in planets)
print("Pluto" in planets)
print("Mars" not in planets)

print(planets + ("Pluto",))
print(planets * 2)

print(planets[2])
print(planets[-1])
print(planets[1:5:2])

print(len(planets))
print(min(planets))
print(max(planets))

print(planets.index("Earth"))
print(planets.count("Mars"))


print("\n------------------------------------------------------------")
