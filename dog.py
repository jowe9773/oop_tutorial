# dog.py

class Dog:                                                  # create a class about dogs
    species = "Canis familiaris"                            # class attributes - something that is the same for every instance of a class

    def __init__(self, name, age):                          # Every time you make a new instance of the Dog class, this method will run and 
                                                            #   it sets the initial state of the object. Parameters that every instance of a
                                                            #   class will have should be defined in this method
        
        self.name = name                                    # Creates an attribute called name and assigns it the value of the variable name 
        self.age = age                                      # These are instance attributes

    def __str__(self):                                      # returns a string when the class is called to print
        return f"{self.name} is {self.age} years of age."

    def description(self):                                  # Method to describe the instance of the class
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):                                 # Method to have the class instance do something ("speak")
        return f"{self.name} says {sound}!"







# instantiate the objects/ use the classes
fido = Dog("Fido", 15)                                      #instantiate the dog class for fido

print(fido)                                                 #print the string generated in __str__ for the instance of Dog named attribute

print(fido.name)                                            #print the instance and class attributes using 'dot notation'
print(fido.age)
print(fido.species)

fido.species = "Felis silvestris"                           #can change attributes (both class and instance) for a particular instance
print(fido.species)

fido_description = fido.description()                                          #do the decription method for fido
print(fido_description)

fido_says = fido.speak("Meow")                                                 #do the speak method for fido saying "Meow"
print(fido_says)