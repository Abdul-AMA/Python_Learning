class Car:
    max_speed = 0
    speed_unit = ""

    def __init__(self, max, unit):
        self.max_speed = max
        self.speed_unit = unit
        print("Car with the maximum speed of", self.max_speed, self.speed_unit)

    def printing_car(self):
        print("Car with the maximum speed of", self.max_speed, self.speed_unit)

class Boat:
    max_speed = 0

    def __init__(self, max):
        self.max_speed = max

    def printing_boat(self):
        print("Boat with the maximum speed of", self.max_speed,"knots")



boar = Boat(50)
boar.printing_boat()