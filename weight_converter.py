weight=int(input("Weight:"))
unit=input("(L)bs or (K)g: ")
if unit.upper()=="L":
    print(f"you are {2.2046*weight} pounds")
else:
    print(f"you are {0.45*weight} kilos")    
