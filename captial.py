class India():

    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the language of India")

    def type(self):
        print("India is a developing country")

class USA():

    def capital(self):
        print("The capital of USA is Washington,D.C.")

    def language(self):
        print("English is the language of USA")

    def type(self):
        print("USA is a developed country")


obj_ind = India()

obj_usa = USA()

for country in (obj_ind,obj_usa):

    country.capital()

    country.language()

    country.type()

