'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Examples:  
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
'''
List1= [23, 65, 19, 90]
pos1 = 1
pos2 = 3

def swap(List, pos1, pos2):
    for i in List:
         if i==List[pos1]:
             for j in List[pos1:]:
                 if j==List[pos2]:
                     temp=j
                     j=i
                     i=temp
    print(List)

swap(List1,2,3)
