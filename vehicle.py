class Vehicle:
  def __init__(self, wheels):
    self.wheels = wheels

  def print_num_wheels(self):
    print(self.wheels)

class Car(Vehicle):
  def __init__(self, num_doors=4):
    Vehicle.__init__(self, 4)
    self.num_doors = num_doors

  def print_car(self):
    self.print_num_wheels()
    print(self.num_doors)

class Motorcycle(Vehicle):
  def __init__(self):
    Vehicle.__init__(self, 2)


coupe = Car(num_doors=2)
coupe.print_car()

bike = Motorcycle()
bike.print_num_wheels()