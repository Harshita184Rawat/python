'''
Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

'''
list = [35, 76, 80, 34, 55, 32]
for i in list:
    if(i%5==0):
        print(i)
