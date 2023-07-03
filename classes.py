class Point():
    def __init__(self, x, y):   # Constructor
        self.x = x
        self.y = y

p = Point(2, 5)
print(p.x)
print(p.y)

class Flight():  
    def __init__(self, capacity):       # Create a new flight.
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):      # Add passangers function
        if not self.open_seats():           # Same as saying if self.open_seats == 0:
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):               # Return amount of open seats function. 
        return self.capacity - len(self.passangers)

flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Genny"]
for i in people:
    success = flight.add_passanger(i)
    if success:
        print(f"Added {i} to flight successfully")
    else:
        print(f"{i} cannot be added since flight is at max capaxity")



