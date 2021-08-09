# instance variable : if we define a variable in __init__

# class variable : if we define a variable outside of __init__

# namespace : namaspace is an area where you create and store object/variable

# two types of namespace : class namespace , instance/objece namespace

class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

Car.wheels = 5

c2.mil = 8

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)