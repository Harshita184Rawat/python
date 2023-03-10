''' Remove all duplicates from a given string in Python
We are given a string and we need to remove all duplicates from it? What will be the output if the order of character matters? 

Examples:
Input : geeksforgeeks 
Output : geksfor
'''

s="geeksforgeeks"
result=''
for i in range(len(s)):
    if s[i] not in s[(i+1):]:
        result=result+s[i]  
print(result)
        
