'''
Uncommon elements in Lists of List

Aims at achieving the task of finding uncommon two list, in which each element is in itself a list.
'''
list1 = [ [1, 2], [3, 4], [5, 6] ]
list2 = [ [3, 4], [5, 7], [1, 2] ]
print("Original first list: ", list1)
print("Original second list: ", list2)
result=[]
for i in range(len(list1)):
    if list1[i] not in list2:
        result.append(list1[i])
    if list2[i] not in list1:
        result.append(list2[i])

print("Uncomman lists in first and second lists: ",str(result))