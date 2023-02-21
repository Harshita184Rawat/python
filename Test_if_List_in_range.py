# Test if List contains elements in ginen Range

list=[1,3,5,6,8,3,5,6,7,8,3]

start=int(input("Enter the starting of list:"))
end=int(input("Enter the endpoint of list:"))

# to check whether all elements of list lies in range
for item in list:
    if item<start:
        print("list is not in range.",item,"is out of range.")
        break
    if item>end:
        print("list is not in range.",item,"is out of range.")
        break
