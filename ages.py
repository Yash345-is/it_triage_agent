class myclass:

    def __init__(self):   
        self.__age = 20

    def show(self):
        print("The age is:",self.__age)

    def change(self,new_age):

        self.__age = new_age

    def __str__(self):
        return f"The age printed using str fucntion is: {self.__age}"

o1 = myclass()

o1.show()

print(o1)

o1.change(15)

o1.show()

print(o1)