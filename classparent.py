class Animals:

    def __init__(self,name):

        self.name = name

    def info(self):
        print("Name of the animal is:",self.name)

class Wild(Animals):

    def __init__(self, name,type_of_food):

        self.type_of_food = type_of_food

        super().__init__(name)

    def info(self):

        super().info()

        print("The type of food this animal consumes is:",self.type_of_food)

a1 = Wild("Tiger","Zebra")

a1.info()

a2 = Animals("Cat")

a2.info()