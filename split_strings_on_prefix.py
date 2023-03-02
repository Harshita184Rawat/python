'''
Split Strings on Prefix Occurrence

Input : test_list = ["geeksforgeeks", "best", "geeks", "and"], pref = "geek"
Output : [['geeksforgeeks', 'best'], ['geeks', 'and']] 
Explanation : At occurrence of string “geeks” split is performed.

Input : test_list = [“good”, “fruits”, “goodness”, “spreading”], pref = “good” 
Output : [[‘good’, ‘fruits’], [‘goodness’, ‘spreading’]] 
Explanation : At occurrence of string “good” split is performed. 
'''
test_list = ["string", "best", "geeks", "and"]
print("List of strings: ",test_list)
pref=input("Enter the prefix to split string: ")
res=[]
for string in test_list:
    
    if string.startswith(pref):
        res.append([string])
    else:
        res[-1].append(string)

    
print("Prefix Splitted list: ", str(res))