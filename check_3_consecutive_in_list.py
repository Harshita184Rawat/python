'''
Our task is to print the element which occurs 3 consecutive times in a Python list. Example :

Input : list = [4, 5, 5, 5, 3, 8]
Output : 5

Input : list = [1, 1, 1, 64, 23, 64, 22, 22, 22]
Output : 1, 22
'''
list = [1, 1, 1, 64, 23, 64, 22, 22, 22]
n=len(list)

for i in range(n-2):
    if list[i]==list[i+1] and list[i+1]==list[i+2]:
        print(list[i])
    