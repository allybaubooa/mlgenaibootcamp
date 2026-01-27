class Door:
    def __init__(self):
        self.is_opened = False
    
    def open_door(self):
        self.is_opened = True
        print("Door opened!")

    def close_door(self):
        self.is_opened = False
        print("Door closed!")

class BlockedDoor(Door):
    def open_door(self):
        raise Exception("A blocked door cannot be opened.")

    def close_door(self):
        raise Exception("A blocked door cannot be closed.")

door = Door()
door.open_door()      
door.close_door()  

blocked = BlockedDoor()
blocked.open_door()  
