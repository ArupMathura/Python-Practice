def add(a, b, c=0):
    return a + b + c


print(add(2, 3))
print(add(2, 3, 4))


# *****************************************************************************
# polymorphism with class method
# *****************************************************************************

class India:
    def capital(self):
        print("delhi")

    def language(self):
        print("hindi")

    def type(self):
        print("devoloping")


class USA:
    def capital(self):
        print("washington, D.C")

    def language(self):
        print("english")

    def type(self):
        print("devoloped")


obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
