'''
Python – Replace index elements with elements in Other List

Given two lists list1,list2 and we need to replace
positions in one list with the actual elements from other list.
'''
# list containing elememts
list1=['a','b','c','d']
# list containing indices
list2=[0,1,2,3,1,3] 
print("list1: ",list1)
print("list2: ",list2)
result=[]
for item in list2:
    result.append(list1[item])
print("Resultant list: ",result)