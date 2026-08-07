class student:
    print("This the student class")

    def __init__(self,grade,name):

        self.grade = grade
        self.name = name
        print("Grade:",grade,"Name:",name)
        

s1 = student("6th","Jason")

s2 = student("4th","Josh")