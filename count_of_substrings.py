'''
Write a program to find how many times substring “Emma” appears in the given string.

Given:
str_x = "Emma is good developer. Emma is a writer"

Expected Output:
Emma appeared 2 times

'''
str_x = "Emma is good developer. Emma is a writer"
key='Emma'
count=0
for item in str_x:
    word=str_x.split()
for i in word:
    if i==key:
        count=count+1

print(f"The word {key} appreaed {count} times in string")
    
    