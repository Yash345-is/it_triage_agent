from abc import ABC,abstractmethod


class Absclass(ABC):


    def output(self,x):

        print("The value passed is",x)

    @abstractmethod

    def task(self):

        print("Inside abstract class")


class Childclass(Absclass):

    def task(self):
        
        print("Inside the child class")

o1 = Childclass()

o1.task()

o1.output(20)


