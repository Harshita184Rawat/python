matrix=[
    [2,4,5],
    [9,5,6],
    [2,0,4]
]
# to access second element of first row
matrix[0][1]
print(f'second element of first row is {matrix[0][1]}')
# to modify the value of third element of second row
matrix[1][2]=32
print(f'value of third element of second row is {matrix[1][2]}')
# to iterate over a 2D list use nested for loops
for row in matrix:
    for item in row:
        print(item)