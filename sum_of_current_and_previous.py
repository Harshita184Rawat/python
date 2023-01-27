# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
sum=0
for number in range(10):
    current=number
    previous=number-1
    if number==0:
        previous=0
    sum=current+previous
    print(f"current number is {current} previous number is {previous} sum: {sum}")
    number=number+1
    