# Objects and classes
# Instance variables and Instance methods 

class Car:
    def __init__(self, windows, doors, engineType):
        self.windowsVariable = windows  #Instance variable or attribute
        self.doors = doors              #Instance variable
        self.engineTypeVariable = engineType  #Instance variable
    
    def drive(self): #Instance method
        print(f"The person is driving the {self.engineTypeVariable} car")

obj1 = Car(4,5,"petrol")
obj1.drive()

# single inheritance and multiple inheritance
# Polymorphism - Method overriding

# Encapsulation 
# - Public, protected, private access modifiers(or variables),  getter and setter methods.
# public - variables accessible within and outside the class
# protected - accessible within class and derived classes
# private - accessible only within the class

# Defination: It is a concept of wrapping up of data and methods. It restricts direct access to some of the 
#             object components.

# Abstraction:
# - It is concept of hiding complex implementation details and showing only the necessary features of an object.

from abc import ABC,abstractmethod

class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

def start_vehicle(veh):
    veh.start_engine()
    veh.drive()

tata = Car()
start_vehicle(tata)

