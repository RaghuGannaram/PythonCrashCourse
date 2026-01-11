s1 = {1, 2, 3}
s2 = set([3, 4, 5])
print(s1, s2)

print(1 in s1)
print(1 in s2)

s1.add(10)
s1.update([10, 11, 12])
print(s1)

s2.remove(4)  # error if not present
s2.discard(20)  # no error if not present
print(s2)


print(s1,s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.intersection(s2))
print(s1 & s2)

print(s1.difference(s2))
print(s1 - s2)

print(s1.symmetric_difference(s2))
print(s1 ^ s2)