# inheritance.py

class Parent:
    speaks = ["English"]


class Child(Parent):
    def __init__(self):
        #super().__init__()
        pass

    def nonNativeTounges(self, languages):
        self.speaks.append(languages)


josie = Child()

print(josie.speaks)

josie.nonNativeTounges(["Spanish", "Python"])

print(josie.speaks)