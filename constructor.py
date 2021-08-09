class computer:
    def __init__(self):
        self.name = "arup"
        self.age = 22

    # def update(self):
    #     self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()

# c2.name = "raju"

# print(c1.name)
# print(c2.name)

c2.age = 40

if c1.compare(c2):
    print("They are same")
else:
    print("they are not same")
