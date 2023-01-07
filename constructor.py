class coordinates:
    def __init__(self, x, y): # constructor method
        self.x=x
        self.y=y
    # self is reference to current object 
    
    def print_value(x,y):
        print(f"Values are: x={x}, y={y}")
        

coordinates1 = coordinates.print_value(23,45)
coordinates2 = coordinates.print_value(38,90)