class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first=f
        self.second=s

    def calculate(self):
        self.answer = self.first + self.second

    def display(self):
        print("First number : ", self.first)
        print("Second number : ", self.second)
        print("Answer is : ", self.answer)


obj = Addition(1000, 2000)
obj.calculate()
obj.display()

