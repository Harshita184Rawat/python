class parent:
    def __init__(self, id):
        self.id = id
    
    def print_id(id):
        print(f"ID is {id}")
        
        
class child(parent):
    pass # if we want to keep the class empty we can use pass
    
    
child1 = child(1)
child1.print_id()