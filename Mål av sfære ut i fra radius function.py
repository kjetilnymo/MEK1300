#

from math import pi

radius = float(input("Enter a radius: "))

area_circle = pi * radius * radius
circumference_circle = 2 * pi * radius

volume_sphere = (4/3) * pi * radius ** 3
surface_area_sphere = 4* pi * radius * radius

print(f"\n*** With radius {radius} ***\n")
print(f"Area of the circle = {area_circle:.2f}")
print(f"Circumference of the circle = {circumference_circle:.2f}")
print(f"Volume of the sphere = {volume_sphere:.2f}")
print(f"Surface of the sphere = {surface_area_sphere:.2f}")