class myclass:

    __privateVAR = 27

    def __privatemeth(self):

        print("Im inside class myclass")

    def privatevalue(self):

        print("Private Variable Value:",myclass.__privateVAR)

foo = myclass()
foo.privatevalue()

foo.__privatemeth()