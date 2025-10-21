
string = input("Enter a string: ")

characters = {}

"""
# Counts the unique characters in a string. Sets 
# each letter -> True, and adds them to dictionary. 
# Does not add duplicates.
for char in string:
    characters[char] = True

"""

# Alternative method
for char in string:
    characters[char] = 0

# Counts how many times each character appers in the
# string
for char in string:
    characters[char] = characters[char] + 1

print("That string contained", len(characters), "unique characters.")

print(characters)