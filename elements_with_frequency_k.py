'''
Given a List, extract all elements whose frequency is greater than K.

Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
Explanation : Both elements occur 4 times. 

Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2 
Output : [4, 3, 6] 
Explanation : 3,4 and 6 all occur 3 times respectively.

'''
test_list =[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k= 3 
count=0
output=[]
i=0
for item in range(len(test_list)):
    count=0
    for j in test_list:
        if j==item:
            count=count+1
    if count>=k:
        output.append(item)
    i=i+1
    
print(output)