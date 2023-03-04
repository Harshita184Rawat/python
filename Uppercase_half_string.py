# Uppercase Half String
'''
Given a String, perform uppercase of later part of string. 

Input : test_str = "goldenapple" 
Output :  goldeNAPPLE
Explanation : Latter half of string is uppercased. 

Input : test_str = "notebook"
Output : noteBOOK
Explanation : Latter half of string is uppercased.
'''

test_str = "notebook"
n=len(test_str)//2
result=''
for i in range(len(test_str)):
    if i<n:
        result=result+test_str[i]

    else:
        result=result+(test_str[i].upper())
        
print(result)

    