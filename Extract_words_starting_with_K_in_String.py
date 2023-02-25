# Extract words starting with K in String List

'''
Given list of phrases, extract all the Strings with begin with character K.

Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l 
Output : [‘learning’, ‘love’] 
Explanation : All elements with L as starting letter are extracted. 

Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = m 
Output : [] 
Explanation : No words started from “m” hence no word extracted.
'''
test_list = ["Gfg is good for learning", "Gfg is for geeks", "I love G4G"]
k='l'
result=[]
for substring in test_list:
    string=substring.split()
    for item in string:
        if item[0].lower()==k:
            result.append(item)
            break
print(result)