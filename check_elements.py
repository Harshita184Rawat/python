''' Write a function to which takes input a list and  return True if the first and last number of the list is same. If numbers are different then return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:

 list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False '''

def check_elements():
    Arr = []
    n=int(input("Enter the size of Arr: "))
    print("Enter the elements")
    for i in range(n):
        item=int(input())
        Arr.append(item)
    for item in Arr:
        if Arr[0]==Arr[n-1]:
            print('True')   
        else:
            print('False')
            
check_elements()
