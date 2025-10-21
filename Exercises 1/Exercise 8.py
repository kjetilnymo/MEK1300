# Exercise 8

"""

# Oppgave 1
print("Oppgave 1)")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

# a = no
# b = no, they have {1, 5} in common
# c = {1, 2, 3, 4, 5, 6, 8}
# d = empty dictionary
inboth = set2.intersection(set3)
print(inboth)
# e = {1, 3, 5}
difference = set1.difference(set2)
print(difference)



# Oppgave 2
grade_count = {"A" : 8, "D" : 3, "B" : 15, "F" : 2, "C" : 6}

print("Oppgave 2)")
# a)
print("a)")
for key in grade_count.keys():
    print(key, "", end="")
print("")

# b)
print("b)")
for value in grade_count.values():
    print(value, "", end="")
print("")

# c)
print("c)")
for key in grade_count.keys():
    print(key, ":", grade_count[key])
print("")

# d)
print("d)")

# Creates a list containing the keys in the
# grade_count dictionary, in sorted order
sorted_dict = sorted(grade_count)

# Gathers and prints the values with the keys from
# the grade_count dict, in order with the 
# sorted_dict list.
for key in sorted_dict:
   print(key, ":", grade_count[key])

print("")


# e)
print("e)")
total = 0

for value in grade_count.values():
    total += value

result = total / len(grade_count)
print(result)

print("")

# f)
print("f)")

for key in sorted_dict:
    print(key, ":", (grade_count[key] * "*"))

print("")


# Oppgave 3
print("Oppgave 3)")
def main():
    numbers={
    "0":"Zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
    }


    phone_number = input("Enter your phone number: ")
    result = translate(numbers, phone_number)
    print(result)



def translate(numbers, phone_number):
    result = ""
    for char in phone_number:
        result += numbers.get(char,"?")
        result += " "
    return result

main()

"""

# Oppgave 4
print("Oppgave 4)")

students = dict()

def main():
    answer1 = "NO" 
    answer2 = "YES" 

    answer = "NO"
 
    while answer == answer1:

        choice1 = input("Would you like to:\n A: Add/remove students.\n B: Modify grades.\n C: Print all grades.\n Type: 'A', 'B' or 'C': ").upper()
        if choice1 == "A":
            choice2 = input("Would you like to add or remove a student?\n Type 'Add' or 'Remove': ").upper()
            if choice2 == "Add".upper():
                    new_student = input("What is the name of the new student? ").upper()
                    new_grade = input("What is their grade? ").upper()
                    students[new_student] = new_grade
            elif choice2 == "Remove".upper():
                    remove_student = input("Which student would you like to remove?").upper()
                    if remove_student in students:
                        students.pop(remove_student)
                    else:
                        print("That student does not exist.")
        elif choice1 == "B".upper():
            student_modified = input("What student would you like to modify the grade of? ").upper()
            new_grade = input("What is their new grade? ").upper()
            if student_modified in students:
                students[student_modified] = new_grade
            else:
                 print("That student does not exist.")

        elif choice1 == "C".upper():
            for key in students:
                print(key, ":", (students[key]))
        answer = str(input("Are you finished? Type 'YES' or 'NO'. ")).upper()
    else:
        print("Okey, see you again.")
    

main()
