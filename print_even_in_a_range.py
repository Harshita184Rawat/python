'''
Given starting and end points, write a Python program to print all even numbers in that given range. 

Example:
Input: start = 4, end = 15
Output: 4, 6, 8, 10, 12, 14

Input: start = 8, end = 11
Output: 8, 10

'''
start=int(input("Enter the starting number of range: "))
end=int(input("Enter the ending number of range: "))

print("Even numbers are: ")
for item in range(start,end+1):
    if item%2==0:
        print(item)