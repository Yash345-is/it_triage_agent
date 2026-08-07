import random

al = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

al2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","X","Y","Z"]



a = random.choice(al)

b = random.choice(al)

while b == a :
    b = random.choice(al)

c = random.choice(al)

while c == a or c == b :

    c = random.choice(al)

d = random.choice(al2)

e = random.choice(al2)

while e == d:
    e = random.choice(al2)

f = random.choice(al2)


while f == e or f == d :
    f = random.choice(al2)

g = random.randint(1,11)

h = random.randint(1,11)

print(f"{a}{b}{c}{d}{e}{f}{g}{h}")