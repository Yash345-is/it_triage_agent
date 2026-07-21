dict1 = {"student1":90,"student2":85,"student3":92,"student4":89,"student5":95}
a = dict1.get("student1")
b = dict1.get("student2")
c = dict1.get("student3")
d = dict1.get("student4")
e = dict1.get("student5")

avg = (a + b + c + d + e)/5

print(avg)
    
f = max(dict1)

print(f)

g = min(dict1)

print(g)
    
lookup = input("Which students's marks do you want to get?:")

if lookup == "student1":
    print(a)

if lookup == "student2":
    print(b)

if lookup == "student3":
    print(c)

if lookup == "student4":
    print(d)

if lookup == "student5":
    print(e)





