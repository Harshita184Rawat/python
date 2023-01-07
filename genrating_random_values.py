import random 
# random is a built in module in python 

for i in range(3):
    print(random.random())
# random module has a random method used to generate random values btw 0 to 1

# randint method generates random integer values
for i in range(4):
    print(random.randint(23,30))
    
# choice method picks a random item from a list
members = ["ACB", "BHJI", "TYHBN", "YGFGU", "SNJK", "HSUDB"]
leader = random.choice(members)
print(leader)