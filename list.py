list = [345,654,346,856,876,1024]

total = 0

a = len(list)

print(len(list))

print(list[1:5:2])

for i in list:

    total = total + i

print(total)

avg = round(total / a,2)

print(avg)

c = min(list)

print(c)

d = max(list)

print(d)