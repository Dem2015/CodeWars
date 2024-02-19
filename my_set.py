set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
set3 = {1, 3, 5}
list1 = [10, 11, 12]
set1.add(0)
print(set1)

set2.update(list1)
print(set2)
set2.remove(12)
print(set2)

set2.discard(11)
print(set2)

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set2 - set1)

print(set1.symmetric_difference(set2))
print(set2 ^ set1)

if set3.issubset(set1):
    set3.add(2)
    print(set3, True)
if set1.issuperset({4, 5, 6}):
    set1.update(set(list1))
    print("Произошло объединение: ", set1)
else:
    print(set1, set(list1), "Объединения не случилось")





