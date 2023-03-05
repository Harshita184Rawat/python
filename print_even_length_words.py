# Program to print even length words in a string
'''
Given a string. The task is to print all words with even length in the given string.

Examples: 
Input: s = "This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am
'''
s = "i am laxmi"
string=s.split()
for item in string:
    if len(item)%2==0:
        print(item)