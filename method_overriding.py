class A:
    def show(self):
        print("Print A")

class B(A):
    def show(self):
        print("Print B")

a = B()
a.show()