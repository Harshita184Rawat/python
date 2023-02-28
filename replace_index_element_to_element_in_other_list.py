# python program to replace a element on index n in list1 to the element in list2
list1=[1,2,3,8,5]
list2=[5,6,7,4,9]
print("List1: ",list1)
n=int(input("Enter the index of list1: "))
if n>len(list1):
    print("Index out of range")
print("List2: ",list2)
key=int(input("Enter the of list2 to be positioned at index n: "))
list1[n-1]=key
print("Resultant list1: ",list1)