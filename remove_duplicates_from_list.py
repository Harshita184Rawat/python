# program to remove the duplicates in a list
names=['himanshi', 'mosh', 'Arpita', 'krishna', 'mosh']
# count vala and nested for loops
for item in names:
    if names.count(item)>=2:
        names.remove(item)
print(names)