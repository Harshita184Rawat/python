str = "String Methods In Python"

# count occurence of substrings
print(str.count('in'))

# to get index 
print(str.find('n'))
print(str.index('n'))

print(str.isdecimal())
print(str.islower())
print(str.isupper())
print(str.islower())
print(str.istitle())

# join method
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# to conert in lower case
print(str.casefold())
print(str.lower())

print(str.upper())
print(str.title())

# strip method
x="      remove empty        spaces     "
print(x.strip())
print(x.lstrip())
print(x.rstrip())

# maketrans method
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt.replace('P','S')
print(txt)

# zfill method
k="10"
y=k.zfill(5)
print(y)

# split method
x=str.split(" ",2)
print(x)









