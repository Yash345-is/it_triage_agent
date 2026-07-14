b1 = {'orange','mango','banana','apple','papaya','watermelon','papaya'}

b2 = {'banana','mango','melon','papaya','blackberry','grapefruit','watermelon'}

print(f"Basket 1: {b1}")

print(f"Basket 2: {b2}")

b3 = b1.intersection(b2)

print(b3)

b4 = b1.union(b2)

print(b4)

b5 = b1.difference(b2)

print(b5)

b6 = b2.difference(b1)

print(b6)

import array as arr

a = arr.array('i',[1,65,32,1])

print(a)

a.insert(2,34)

print(a)

a.append(6)

print(a)

print(a.count(1))

a.reverse()

print(a)