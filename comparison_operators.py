name=input("Enter your name:")
n=len(name)
if n<3:
    print("name must have atleast three characters")
elif n>50:
    print("name can have maximum 50 characters ")
else:
    print(f"{name} looks Good!")
    