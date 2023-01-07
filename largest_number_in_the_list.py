# program to find the largest number list
list=[1,3,5,8,9]
max=list[0]
for term in list:
    if max<=term:
        max=term
print(f'largest number in the list is {max}')