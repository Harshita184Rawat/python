# python code to clone a list using in-built extend() function

list=[23,54,565,65,43,45]

def clone(list):
    cloned_list=[]
    cloned_list.extend(list)
    return cloned_list
    
new_list=clone(list)
print("Original ist: ",list)
print("List after cloning: ",new_list)
