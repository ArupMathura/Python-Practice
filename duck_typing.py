class Laptop:
    def code(self, ide):
        ide.execute()


class PyCharm:
    def execute(self):
        print("compiling")
        print("running")


lap1 = Laptop()
lap1.code(ide=PyCharm())
