name=input("Enter a name")
alphabet=input("Enter an alphabet")
i=0
count=0
while i < len(name):
    if name[i]==alphabet:
        count=count+1
    i=i+1
print("The alphabet,",alphabet,",occured",count,"times")


