set1 = {1,2,3,4,5,6,7,8,'чёрт'}
list1 = [i **25 for i in range(2)]
set2 = set(list1)
print(set1)
print(list1)
print(set2)
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)

