dict1 = {'Codingal':2,'is':2,'best':2,'for':2,'coding':1}

count = 0

for i in dict1.values():
    if i == 2:
        count += 1

print(f"The frequency of 2 in the dictionary is {count}")