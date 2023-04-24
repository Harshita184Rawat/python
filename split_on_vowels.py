''' Given a String, perform split on vowels. 

Example:

Input : test_str = ‘GFGaBst’ 
Output : [‘GFG’, ‘Bst’] 
Explanation : a is vowel and split happens on that.

Input : test_str = ‘GFGaBstuforigeeks’ 
Output : [‘GFG’, ‘Bst’, ‘f’, ‘r’, ‘g’, ‘ks’]
Explanation : a, e, o, u, i are vowels and split happens on that.

'''
    
def isVowel(letter):
    if letter.upper()=='A' or 'E' or 'I' or 'O' or 'U':
        return 1
    else:
        return 0

string = "GFGaBst"
for letter in string:
    y=isVowel(letter)
    if y==1:
        x=str.split(letter)
print(x)
        
