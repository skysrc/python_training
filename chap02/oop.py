class House: 
    def printMe(self):
        print("this is a house")

class Room(House):
    def printMe2(self):
        print("this is a room")

house = House()
house.printMe()

room = Room()
room.printMe2()
room.printMe()