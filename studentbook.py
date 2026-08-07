dict1 = {"student1":90,"student2":85,"student3":92,"student4":89,"student5":95}

sum = 0

for i in dict1.values():
    sum = sum + i

print(sum)

avg = sum/5

print(avg)

a = max(dict1)

print(a)

b = min(dict1)

print(b)


lookup = input("Which student's marks do you want to look for?:")
if lookup == "student1":
    print(dict1.get("student1"))

elif lookup == "student2":
    print(dict1.get("student2"))

elif lookup == "student2":
    print(dict1.get("student3"))

elif lookup == "student4":
    print(dict1.get("student4"))

elif lookup == "student5":
    print(dict1.get("student5"))