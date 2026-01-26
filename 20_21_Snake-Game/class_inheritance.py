class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# Example of how to inherit all the attributes and methods from Super class Animal class
class Fish(Animal):
    def __init__(self):
        super().__init__() #to inherit all the attributes and methods from Super class Animal class

    # example of how to inherit same functionality of breathe from the super class and modify it accordingly for Fish class.
    def breathe(self):
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in water.")


#creating an object nemo from Fish class
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)



# By learning about class inheritance, what allows us to do is to take an existing class that we've created
# or somebody else has created, and then build on top of it without having to reinvent the wheel and redefine
# everything that's in that class.