import math

opposite = float(input("Enter the opposite of the triangle:"))
adjecent = float(input("Enter the adjacent of the triangle:"))
hypnotuse = float(input("Enter the hypnotuse of the triangle"))



print(f"Sin:{math.sin(opposite/hypnotuse)}")

print(f"Cos:{math.cos(adjecent/hypnotuse)}")

print(f"Tan:{math.tan(opposite/adjecent)}")

