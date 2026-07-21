dict = {"I":2,"love":1,"to":2,"play":2,"video":2,"games":2}

count = 0

for i in dict.values():
    if i == 2:
        count += 1
    
print("Frequency of 2 in the dictionary:",count)