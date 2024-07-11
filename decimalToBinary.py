#program to convert decimal number to binary

d_number=int(input("Enter the number: "))
binary=""
while d_number>0:
    binary=str(d_number%2)+binary
    d_number=d_number//2

print("Binary output: ",binary)
