#can be key in dictonary
#fixed elements, can not be changed
#

"""

point = (10, 20)
color = (255, 165, 0)
birth_day = (1990, 5, 17)

"""

x = 10
y = 20


print("Before swap")
print("x =", x)
print("y =", y)

"""
temp = x
x = y
y = temp
"""

(x, y) = (y, x)
#bytter veridene til x og y med tuple

print("\nAfter swap")
print("x =", x)
print("y =", y)

