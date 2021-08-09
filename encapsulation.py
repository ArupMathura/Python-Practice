class base:
    def __init__(self):
        self._a = 2


class derived(base):
    def __init__(self):
        base.__init__(self)
        print("Calling protected member of base class")
        print(self._a)


obj1 = derived()
obj2 = base()
print(obj1.a)
