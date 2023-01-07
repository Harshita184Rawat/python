# classes are used to define new types, these can have methods and attributes
class point: # pascal naming convention
    
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")
# here move and draw methods to the point

point1 = point()
point1.x=79
point1.y=23
print(point1.x)
point.draw()

point2 = point()
point2.x=7
print(point2.x)
