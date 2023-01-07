# guess the number.You have 3 chance
key=9
chance=1
while chance<=3:
    number=int(input("Guess: "))
    chance=chance+1
    if number==key:
        print("You Won!")
        break
else: print("Sorry,you failed!")