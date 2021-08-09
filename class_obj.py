class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("the configaration is : ", self.cpu, self.ram)


com1 = Computer('i5', 8)
com2 = Computer('Ryzen 3', 4)

# Computer.config(com1)
#
# Computer.config(com2)

com1.config()