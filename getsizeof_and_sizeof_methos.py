import sys

# To find the size of a Tuple in Python

#       1.Using getsizeof() function:
# The getsizeof() function belongs to the python’s sys module.
tuple = ("A", 1, "B", 2, "C", 3)
x=str(sys.getsizeof(tuple))
print("Size of tuple using 'getsizeof()' function is "+ x)

#       2.Using inbuilt __sizeof__() method:
# inbuilt __sizeof__() method to determine the space allocation of an object without any additional garbage value.
y=str(tuple.__sizeof__())
print("Size of tuple using '__sizeof__()' function is " + y)
