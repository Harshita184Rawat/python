import converter
print('''
press 1 for conversion of length units
press 2 for conversion of temperature unit
''')
choice = input("Enter your choice: ")
if choice == "1":
    from converter import Length
    value = int(input("Length: "))
    unit = input("(K)bs or (M)g or (MILE) or (YARD): ")
    if unit.upper() == "K":
        Length.meter_to_km(value)
    elif unit.upper() == "M":
        Length.km_to_meter(value)
    elif unit.upper() == "MILE":
        Length.yard_to_mile(value)
    elif unit.upper() == "YARD":
        Length.mile_to_yard(value)

elif choice == "2":
    from converter import Temperature

    value = int(input("Temperature: "))
    unit = input("(K)kelvin or (C)celcius or (F)Fahrenheit or (CF)celcius: ")
    if unit.upper() == "K":
        Temperature.celcius_to_kelvin(value)
    elif unit.upper() == "C":
        Temperature.kelvin_to_celcius(value)
    elif unit.upper() == "F":
        Temperature.celcius_to_fahrenheit(value)
    elif unit.upper() == "YARD":
        Temperature.fahrenheit_to_celcius(value)
