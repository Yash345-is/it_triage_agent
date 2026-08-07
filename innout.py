class IOString:


    def __init__(self):
        self.str1 = ""

    def getstring(self):
        self.str1 = input("Enter String:")

    def printstring(self):
        print("Final result:",self.str1.upper())

obj = IOString()

obj.getstring()

obj.printstring()
