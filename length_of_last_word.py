#Given string s with words and spaces find the length of last word in s

s = "   fly me   to   the moon  "
x=s.split()
n=len(x)
print(len(x[n-1])) # or x[-1]