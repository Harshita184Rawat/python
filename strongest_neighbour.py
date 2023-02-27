'''
Python program to find the Strongest Neighbour

Given an array arr[] of N positive integers. The task is to find the maximum for every adjacent pair in the array.

Examples:
Input: 1 2 2 3 4 5
Output: 2 2 3 4 5

Input: 5 5
Output: 5
'''
arr=[1,2,2,3,4,5,6,7]
N=len(arr)
output=[]
i=0
for i in range(N):
    if i==N-1:
        break
    output.append(max(arr[i],arr[i+1]))
print(output)