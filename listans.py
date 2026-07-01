def matching(list1):
    listans = []
    count = 0  
    
    for i in list1:

        if len(i) >=2 and (i[0] == i[-1]):
            count = count + 1
            listans.append(i)
    print(listans)
    return count

list1 = ["grg","lol","xx","brl","grtghy"]

print("There are",matching(list1),"words which have satisfied both the conditions")    
    
 