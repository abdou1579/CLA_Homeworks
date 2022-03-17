#1rectangle
class Rectangle:
    def __init__(self,length,width) :
        self.length=length
        self.width=width
    def area(self):
        return self.width*self.length
#example
rect=Rectangle(5,10)
print(rect.area())

#2Vehicle
class Vehicle:
    def __init__(self,max_speed,mileage_instance):
        self.max_speed=max_speed
        self.mileag_instance=mileage_instance

#3Empty vehicle
class Vehicle:
    pass

#4Child Bus
class Child_bus(Vehicle):
    pass
a=Child_bus(100,50)
print(a.max_speed)
