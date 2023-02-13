# to find length of list without using inbuilt length() function

list=[23,45,56,67,67,4,3,34,4,87,89,67,5,90]

def cal_length(list):
    count=0
    for item in list:
        count=count+1
    print("length of list is: ",count)

cal_length(list)