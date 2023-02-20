'''
Given starting and endpoints, write a Python program to print all odd numbers in that given range. 

Example:

Input: start = 4, end = 15
Output: 5, 7, 9, 11, 13, 15

Input: start = 3, end = 11
Output: 3, 5, 7, 9, 11
'''

start=int(input("Enter the starting of range: "))
end=int(input("Enter the endpoint of range: "))
for item in range(start,(end+1)):
    if item%2!=0:
        print(item)