s1 = {10, 20, 30}
print(s1)
print(type(s1))

s2 = set([30, 40, 50])
print(s2)
print(type(s2))

s3 = {}
print(s3)
print(type(s3))

s4 = set()
print(s4)
print(type(s4))

s1.add(40)
print(s1)

s1.add(40)
print(s1)

s1.update([50, 60])
print(s1)

s1.update([80, 70], [90, 100])
print(s1)

s1.discard(90)
print(s1)

s1.remove(30)
print(s1)

s1.clear()
print(s1)

s1.add(50)
print(s1)

del s1
# print(s1)

print(s2)
print(len(s2))

print(20 in s2)
print(30 in s2)

s4.update([45, 60, 50])
print(s4)

print(s4 | s2)
print(s2.union(s4))

print(s2 & s4)
print(s4.intersection(s2))

print(s2 - s4)
print(s4 - s2)
print(s2.difference(s4))
print(s4.difference(s2))

print(s2 ^ s4)
print(s4.symmetric_difference(s2))

print(s2.isdisjoint(s4))

s1 = {2, 4, 6, 8}
s2 = {4, 8}

print(s1 <= s2)
print(s2 <= s1)
print(s2.issubset(s1))

print(s1 < s2)
print(s2 < s1)

print(s1 >= s2)
print(s2 >= s1)
print(s1.issuperset(s2))
print(s1 > s2)



