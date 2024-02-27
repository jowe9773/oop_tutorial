# dog.py

class Dog:                              # create a class about dogs
    species = "Canis familiaris"        # class attributes - something that is the same for every instance of a class

    def __init__(self, name, age):      # Every time you make a new instance of the Dog class, this method will run and it sets the initial state of the object. Parameters that every instance of a class will have should be defined in this method
        
        self.name = name                # Creates an attribute called name and assigns it the value of the variable name 
        self.age = age                  # These are instance attributes

    

fido = Dog("Fido", 15)                         #instantiate the dog class for fido
