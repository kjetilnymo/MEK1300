
# To make a dictionary, use "{}", and seperate the
# items with comma (,).

contacts = {"Håvard" : 91009288, "Oscar" : 46868430, "Olav" : 91911339}

print(contacts)


# dict function can be use to make a copy of another
# dictionary.
old_contacts = dict(contacts)

# How to access keys in dictionaries. As long as
# the key "Oscar" has been given a value, the value
# is printed.
print("Oscar's number is", contacts["Oscar"])
print(contacts["Håvard"])
print(contacts["Olav"])

# To check if a key is in the dictionary.
print("Oscar" in contacts)
print("Nicky" not in contacts)

# To add a key with a value to a dictionary(contacts).
contacts["Fredrik"] = 92306080

contacts["Kathrine"] = 47959801

# To modify existing key, just assign new value to it.
contacts["Kathrine"] = 47959800

print(contacts)

# Prints out "NA", or whatever is inserted, if the 
# key we are looking for with .get method is not
# in the dictionary.
print(contacts.get('OK', "NA"))


# Created a phonebook function. Enter the name of
# the person you want the number of. If the person
# is in the dictionary, you get the number. If not,
# you get a message saying we don't have the number.
person = input("Who would you like to call?: ")
number = contacts.get(person)

if person in contacts:
    print("To call", person, "dial:", number)
else:
    print("Im sorry, we do not have that number.")
