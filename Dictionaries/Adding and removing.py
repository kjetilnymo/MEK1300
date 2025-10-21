# Dictionaries are used to associate keys and values.

"""

colors = {"Red", "Green", "Blue"}

favorite_colors = {"Romeo" : "Green", "Adam" : "Red"}

"""

d = dict()

# Prints what type "d" is (dictionary).
print(type(d))

# Gives different keys (Name, Age), different values
# (David, 21).
student = {"Name" : "David", "Age" : 21, "Major" : "CS"}

print(student)



# Use .pop method to remove a key, and the value
# asserted to it.
print(student)
student.pop("Age")

# The key "Age" was removed, together with its
# value; 21.
print(student)

# Runs through student, and prints each of the keys
# in this dictionary.

student["Job"] = "McDonalds"
student["Age"] = 24

for key in student:
    print(key)

# Can alternatively use the .keys method
for key in student.keys():
    print(key)

# Uses .values method to run through student, and 
# prints each of the values in this dictionary.
for value in student.values():
    print(value)

# Prints all the keys in the dictionary (student),
# and all the values asserted to them.
for key in student:
    print(key, ":", student[key])