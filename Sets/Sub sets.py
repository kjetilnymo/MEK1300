"""

emails = ["a@x.com", "b@@x.com", "a@x.com"]

# Converts list to set to remove duplicate elements
unique_emails = set(emails)

for element in unique_emails:
    print(element)



my_list = [(1, 2), (5, 7), (1, 2), (4, 3), (1, 2)]

# Converts tuple to set to remove duplicate elements,
# then converts back to list, and prints new list 
# without previous duplicate elements
my_list = list(set(my_list))

print(my_list)


"""
# A set is only a subset of another set if all of
# the elements in the set, are an element in the 
# other set.

# Ex: canadian is a subset of british, because all
# the elements in canadian (red, white), are in 
# british. 

canadian = {"red", "white"}
british = {"red", "white", "blue"}
italian = {"red", "white", "green"}
french = {"blue", "white", "red"}

# Checks if canadian is a subset of british - True
print(canadian.issubset(italian))

# Checks if atalian is a subset of british - False
print(italian.issubset(british))

# Checks if the elements in 'french' and 'british
# are equal.
print(french == british)

# Checks if the elements in 'french' and 'british
# aren't equal.
print(canadian != french)


# .union of two sets contains all the elements from
# the two sets.
print(canadian.union(italian))
print(french.union(italian))
# Can also use | for same purpose
print(french | italian)

# .intersection finds the elements two sets 
# have in common
print(french.intersection(italian))

# . difference finds the elements the first set has,
# that the second set does not have
print(french.difference(italian))
print(italian.difference(french))

