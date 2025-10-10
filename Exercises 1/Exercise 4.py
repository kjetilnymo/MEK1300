#oppgave 2 hefte 4a
word=input("skriv inn et ord: ")

for letter in word: #går igjennom bokstaver
    if letter.isupper():#lager condition for bokstaven den går igjennom
        print(letter) #printer bokstaven når condition er stemmer

#b
word=input("skriv inn et ord: ")

for letter in range(0,len(word),2): #jmå ha in range for at den skal gå igjennom word på spesfikk måte
    print(word[letter])
    

#c

word=input("skriv inn et ord: ")

vowels=["a","e","i","o","u","y"]

for letter in word:
    if letter in vowels:
        word=word.replace(letter,"_")

print(word)

#d
word=input("skriv inn et ord: ")
total=0 #deefinere counter
vowels= "aeiouyAEIOUY" #definere vokalene

for letter in word: #går igjennom bokstaven
    if letter in vowels:#setter condition for bokstavene
        total+=1 #da legges det i counter
print(total) #printer counter etter å ha gått igjennom alle bokstavne
 

#e
word=input("skriv inn et ord: ")
total=0
for letter in word: #går igjennom hver bokstav
    total+=1 #for hver legges til 1 i ounter
print(total)


x=1 #counter er x og starter fra 0

while x<=5:
    y=1+x+(x**2/2)+(x**3/6)+(x**4/24)
    print(y)
    x+=1
#samme
for x in range (0,5+1):
    y=1+x+(x**2/2)+(x**3/6)+(x**4/24)
    print(y)
    
n=int(input("enter person: "))

#biletter
i=1
total=0
while i<=n:
   age=int(input(f"alder for person {i}: "))
   if age<=2:
       total=total+0
   elif age>=3:
        total=total+14
   elif age>12:
        total=total+23
   elif age>=65:
        total=total=18
   i+=1
print(f"the total fort the group {total:.2f}")
    

#eksempel fra forelesning
string=input("write a string")
mellomrom=0
for char in string:
    if char==" ":
        mellomrom+=1
print(f"det er {mellomrom} mellom rom i string")

def cube_volume(side_length):
    volume=side_length*3
    return volume
#linjene over definerer funksjonen
#linjene under gir 
result=cube_volume(2)
print("a cube with side length 2 has volum", result)

result2=cube_volume(10)
print("a cube with side length 2 has volum", result2)

#
n=int(input("write a positive integer: "))

i=1

if n<1:
    print("invalied input")
else:
    print("the odd number(n) till number", n, "...", end="")
    while i<=n:
                if i % 2 !=0:
                    print(i, end=" ")
                    i=i+1

n=int(input("enter number of stars: "))

i=1 #counter


while i<=n:
    j=0  #setter variabel j inni første loop for å nulstille
    while j<=n-i:
        print("*", end=" ")
        j=j+1
    print()        
    i=i+1
    
    #samme men med for
for i in range(n, 0,-1): #fra n ned til 0 så den går -1 ned 
    for j in range(1, i+1): #j viser hvor mange i som printes på rad
        print("*", end="") #får det til å printes på rad
    print() #setter mellom rom til neste rad
    

    x=1 #counter er x og starter fra 0

while x<=5:
    y=1+x+(x**2/2)+(x**3/6)+(x**4/24)
    print(y)
    x+=1
#samme
for x in range (0,5+1):
    y=1+x+(x**2/2)+(x**3/6)+(x**4/24)
    print(y)
    
n=int(input("enter person: "))


i=1
total=0
while i<=n:
   age=int(input(f"alder for person {i}: "))
   if age<=2:
       total=total+0
   elif age>=3:
        total=total+14
   elif age>12:
        total=total+23
   elif age>=65:
        total=total=18
   i+=1
print(f"the total fort the group {total:.2f}")
    

#eksempel
string=input("write a string")
mellomrom=0
for char in string:
    if char==" ":
        mellomrom+=1
print(f"det er {mellomrom} mellom rom i string")

def cube_volume(side_length):
    volume=side_length*3
    return volume
#linjene over definerer funksjonen
#linjene under gir 
result=cube_volume(2)
print("a cube with side length 2 has volum", result)

result2=cube_volume(10)
print("a cube with side length 2 has volum", result2)

fn=input("skriv inn et fn: ")
ln=input("skriv inn et ln: ")

print(fn, ln)
score=int(input("skriv inn score:"))
total=0
emne=0


while score!=-1:
    total+=score
    emne+=1
    score=int(input("skriv inn score:"))
    if score==-1:
        break

print(total/emne)