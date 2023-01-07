class Length:

    def meter_to_km(self, value):
        result = value/1000
        print(f"Length in km = {result}")
    def km_to_meter(self, value):
        result = value*1000
        print(f"Length in meter = {result}")

    def mile_to_yard(self, value):
        result = value*1760
        print(f"Length in yards = {result}")


    def yard_to_mile(self, value):
        result = value/1760
        print(f"Length in miles = {result}")


class Temperature:
    def celcius_to_kelvin(self, value):
        result = value + 273.15
        print(f"Temperature in kelvin = {result}")

    def kelvin_to_celcius(self, value):
        result = value - 273.15
        print(f"Temperature in kelvin = {result}")

    def fahrenheit_to_celcius(self, value):
        result = (value-32)*5/9
        print(f"Temperature in kelvin = {result}")

    def celcius_to_fahrenheit(self, value):
        result = (value*9/5) + 32
        print(f"Temperature in kelvin = {result}")


