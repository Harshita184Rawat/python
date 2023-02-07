'''
Create a new list from a two list using the following condition:

Given a two list of numbers, write a program to create a new list such that the new list
should contain odd numbers from the first list and even numbers from the second list.

Given:
list1 = [10, 20, 25, 30, 35]//odd
list2 = [40, 45, 60, 75, 90]//even

Expected Output:
result list: [25, 35, 40, 60, 90]
'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

A=[]
i=0
for item1 in list1:
    if i%2!=0:
        A.append(item1)
    i=i+1
j=0
for item2 in list2:
    if j%2==0:
        A.append(item2)
    j=j+1
print("result list:",A)
    

