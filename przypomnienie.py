def fun():
    pass

class Animal:
    def __init__(self, name):
        self.name = name

class LandAnimal:
    def __init__(self, legs):
        self.legs = legs


ryba = Animal("ryba")
print(ryba.name)