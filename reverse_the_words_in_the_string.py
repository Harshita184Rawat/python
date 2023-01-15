string = input("Enter the string: ")
s = string.split()[::-1]
result = []
for i in s:
    result.append(i)
print(" ".join(result))
    