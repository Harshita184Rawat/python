'''
Given a list of integers with duplicate elements in it. The task is to generate another list, 
which contains only the duplicate elements. In simple words, the new list should contain elements that appear as more than one.

Examples:

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]

Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]
'''
list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
output_list=[]
i=0
j=0

for item in list:
    count=0
    key=list[i]
    for num in list:
        if(key==num):
            count=count+1
            continue
    if count>1:
        if key not in output_list:
            output_list.append(key)
    
    i=i+1
    
print("Input: ", list)
print("Output: ", output_list)
