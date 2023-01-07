import random


class Dice:
    def roll():
        i = random.randint(1,6)
        j = random.randint(1,6)
        return (i,j) # or i,j will work as same
 
        
Dice1 = Dice()
print(Dice.roll())