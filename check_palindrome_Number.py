'''
Write a program to check if the given number is a palindrome number.
-> A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
'''
def check_palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number>0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

check_palindrome(234432)
check_palindrome(125)

    
