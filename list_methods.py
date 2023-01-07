numbers=[3,5,6,9,10,21]
# to append an element in the end 
numbers.append(32)
print(numbers)
# to insert at desired index
numbers.insert(3,7) # (index,element)
print(numbers)
# to remove an item 
numbers.remove(9) # (item which is to be removed)
print(numbers)
# to remove all the items/elements of a list
numbers.clear()
print(numbers)
numbers=[3,5,9,6,9,10,2]
# to remove the last item from list use "pop" method
numbers.pop()
print(numbers)
# index method:return the index of the first occurance of the element to be search
print(numbers.index(6))
# to check the presence of an element
print(6 in numbers)
# to count the no. occurrences of an element 
print(numbers.count(9))
# to sort a list
numbers.sort()
print(numbers)
# to reverse the list
numbers.reverse()
print(numbers)
# to copy the list 
numbers2 = numbers.copy()
print(numbers2)