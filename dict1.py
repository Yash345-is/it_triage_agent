dict1 = {"name":"Yashas","age":11.5,"hobby":"watching rain"}

print(dict1) #prints the entire dictionary

for i in dict1:
    print(i) #prints only keys

print(dict1.get("age")) #prints only the specified keys / values 


for i in dict1.values():
    print(i) #prints only values

for i in dict1.items():
    print(i) #prints the dictionary seperately