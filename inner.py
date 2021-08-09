# you can create object of inner class inside the outer class
#                 or
# you can create object of inner class outside the outer class provided you use outer class name to call it


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i3'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Arup', 22)
s2 = Student('Raju', 44)

s1.show()
# print(s1.lap.brand)

# lap1 = Student.Laptop()

# lap1.show()

