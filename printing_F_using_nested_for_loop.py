#program to print
#      XXXXX
#      XX
#      XXXXX
#      XX
#      XX
# Ignore that strings can be mutiplied with an integer
numbers=[5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)
        