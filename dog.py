# dog.py

class Dog:                              # create a class about dogs
    def __init__(self, name, age):      # Every time you make a new instance of the Dog class, this method will run and it sets the initial state of the object. Parameters that every instance of a class will have should be defined in this method
        self.name = name
        self.age = age
