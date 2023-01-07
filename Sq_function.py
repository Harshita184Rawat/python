def square(number):
    return number*number
    # by default all function in python returns None

number = int(input("Enter number: "))
result = square(number)    
print(f" square of {number} is {result}")
