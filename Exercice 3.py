"""

#Oppgave 1 a)
i = 0
j = 10
n = 0

print("i", "%8s" % "j", "%8s" % "n")
#Linjen over setter opp bokstavene i, j og n over tabellen.
print("-" * 19)
#Linjen over lager linjen på toppen av tabellen

while i < j : #Loopen skal fortsette frem til i >= j
    i = i + 1
    j = j - 1
    n = n + 1
    print(f"{i:<4}", f"{j:4}", f"{n:8}")
    #Linjen over printer loopen nedover i "tabellen"
     

#Oppgave 1 b)    
i = 0
j = 0
n = 0

print("i", "%8s" % "j", "%8s" % "n")
print("-" * 19)

while i < j :
    i = i + 1
    j = j - 1
    n = n + 1
    print(f"{i:<4}", f"{j:4}", f"{n:8}")
  
    

#Oppgave 1 c)
i = 10
j = 0
n = 0

print("i", "%8s" % "j", "%8s" % "n")
print("-" * 19)

while i > 0 :
    i = i - 1
    j = j + 1
    n = n + i - j
    print(f"{i:<4}", f"{j:4}", f"{n:8}")
    

#Oppgave 1 d)
i = 0   
j = 10
n = 0

print("i", "%8s" % "j", "%8s" % "n")
print("-" * 19)

while i != j :
    i = i + 2
    j = j - 2
    n = n + 1
    print(f"{i:<4}", f"{j:4}", f"{n:8}")
    

#Oppgave 2
tall = 0

n = int(input("Enter a square: "))

while n > tall**2:
    print(tall**2)
    tall = tall + 1
    
    

#Oppgave 3

c = 0
f = c * (9/5) + 32
    
print("Celsius |", "%8s" % "Farenheit")
print("-" * 19)


while c < 130 :
    print(f"{c:>7}", "|" , f"{f:>9}")
    c = c + 10
    f = c * (9/5) + 32
    
  
 

#Oppgave 4

FirstName = str(input("Enter your first name: "))
LastName = str(input("Enter your last name: "))
score = 0
count = 0
total = 0

score = int(input("Enter your score, or '-1' to finish: "))
while score != -1:
    total += score #legger til innlagt score til total
    count += 1 #legger til 1 til count for hver score som blir skrevet inn
    score = int(input("Enter your score, or '-1' to finish: "))
    if score == -1:
        break

avg = total / count

print(FirstName)
print(LastName)
print(avg)


#Oppgave 5 a)

a = str(input("Enter a line: "))
for letter in a:
    if letter.isupper():
        print(letter, end=("")) #end=("") sier at bokstavene skal stå på samme rad
  

#Oppgave 5 b)

string = str(input("Enter a line: "))
for i in range(0, len(string), 2):
    print(string[i], end="")


#Oppgave 5 c)

vokal = ["a","e","i","o","u", "y"]

string = (input("Enter a line: ")) 

for vokal in vokal:
    string = string.replace (vokal, "_")

print(string)



#Oppgave 5 d)

a = str(input("Enter a line: "))
print(len(a))

"""

#Oppgave 5 e)
a = str(input("Enter a line: "))
v = ["a","e","i","o","u", "y"]










    