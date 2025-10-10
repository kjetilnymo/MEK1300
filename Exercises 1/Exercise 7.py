#Exercise 7

from random import randint

"""
#Oppgave 1

values = []

for i in range(20):
    number = randint(0, 99)
    values.append(number)

print(values, "\n")

sorted_numbers = sorted(values)
# sorted() funksjonen sorterer tallene i lista [values]

print(sorted_numbers)


#Oppgave 2
 
a = [1, 4 ,9 ,16, 9, 7, 4, 9, 11]
b = [11, 11, 7, 9, 16, 4, 1]

def same_list(a, b):
    a = set(a) # Fjerner duplikate nummer
    b = set(b)
    if a == b: # Sjekker om listene har samme nummer, uavhengig av rekkefølge
        return("The lists have identical numbers")
    else:
        return("The lists do not have identical numbers")

print(same_list(a, b))



#Oppgave 3

def sum_without_smallest():
    values = []
    total = 0
    smallest = 101  # setter smallest son en verdi større en 100
    for i in range(10):
        number = randint(1, 100)
        values.append(number)
        total += number
        if number < smallest:
            smallest = number 
# For hvert tall som blir generert, sjekker den om
# det er mindre enn 'smallest'. Hvis det er mindre,
# erstatter det 'smallest'. Så sjekker den igjen med
# neste tall.
    print(smallest)
    print(values)
    return total - smallest

print(sum_without_smallest())

"""

#Oppgave 4
def list_witout_smallest():
    values = []
    smallest = 101
    smallest_index = 0
    for i in range(10):
        number = randint(1, 100)
        values.append(number)
        if number < smallest:
            smallest = number 
            smallest_index = i
    print(values)

    values.pop(smallest_index)
    print(smallest)
    print(values)

list_witout_smallest()