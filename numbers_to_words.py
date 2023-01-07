phone_num = input("Phone: ")
print(phone_num)
num_dictionary ={
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output =""
for number in phone_num:
    output+=num_dictionary[number]+ " "
print(output)
    