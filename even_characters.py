# Write a program to accept a string from the user and 
# display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
string=input('Enter a string: ')
print(f'Original string is {string} ')
n=len(string)
print('Printing Even characters')
for i in range(0, n-1, 2):
    print("index[", i, "]", string[i])
