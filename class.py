class fruit:

    taste = 'sweet'

    def __init__(self,type,color):
        self.type = type
        self.color = color

        print("Type:",type,"Taste:",color)

banana = fruit("banana","yellow")

apple = fruit("apple","red")

print(apple.taste)

print(banana.taste)