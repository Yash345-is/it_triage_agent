class Cars:

    def __init__(self,wheel_count):
        self.wheel_count = wheel_count

    def info(self):
        print("The car has",self.wheel_count,"wheels")


class Electric(Cars):

    def __init__(self,charger,wheel_count):
        self.charger = charger
        super().__init__(wheel_count)

    def info(self):
        print("The electric car uses the",self.charger,"charger")

        super().info()


e1 = Electric("Electric","4")

e1.info()



    