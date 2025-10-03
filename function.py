"""
def cube_volume(side_length):
   if side_length > 0:
        volume = side_length **3
        return volume
    else:
        return False

result = cube_volume(2)
print("A cube with side length 2 has volume", result)

result2 = cube_volume(5)
print("A cube with side length 5 has volume", result2)

"""

def pyramid_volume(height, base_length):
    base_area = base_length * base_length
    volume = height * base_area / 3
    return volume

height = float(input("Enter the height of the pyramid: "))
base_length = float(input("Enter the length of one of the sides of the pyramids base: "))

result = pyramid_volume(height, base_length)

print(result)