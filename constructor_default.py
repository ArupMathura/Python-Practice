class ABC:
    def __init__(self):
        self.abc = "This is a default constructor"

    def print_statement(self):
        print(self.abc)


obj = ABC()
obj.print_statement()
