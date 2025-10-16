# Container that stores a collection of unique values.
# Elements in set are not stored in particular order,
# and can not be accessed by position.

# To make a set:
names = {"Luigi", "Mario", "Wario"}

# You can use set function to convert any sequense 
# into a set_

names = ["Luigi", "Mario", "Wario"]
cast = set(names)


# Copy of lecture code

fruits = {"apple", "banana", "cherry", "banana"}
print(fruits)

# Sets cannot have duplicate values/elements

# {} creates empty dictonary, not empty set

# To create empty set:
empty_set = set()

# Can use 'in'/'not in' operator to see if something
# is an element in the set

# Checks how many uniqe elements in set 'fruits'
print(len(fruits))

# Checks if 'apple' is element in set 'fruits'
print("apple" in fruits)

for element in fruits:
    print(element)

# Best to use 'set' if you dont care about placement
# order or duplicates

# You can add and remove elements from a set, like 
# you can with lists (and not tuples)

fruits.add("orange")

print(fruits)

fruits.add("kiwi")

for element in fruits:
    print(element)

# Use .discard method to remove elements from the set
# Gives no error if element is not part of set
fruits.discard("kiwi")

print(fruits)

# Can also use .remove to remove element from set
# Unlike .discard, .remove gives error if element is
# not in list

# .clear method removes all elements from set
fruits.clear()
print(fruits)


