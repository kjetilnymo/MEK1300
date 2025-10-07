#Exercise 6



a = [1,2,3,4,5,4,3,2,1,0]

"""

#a)

total = 0
for i in range (10):
    total = total + a[i]
    


#b)

total = 0
for i in range (0, 10, 2):
    total = total + a[i]
    


#c)

total = 0
for i in range (1, 10, 2):
    total = total + a[i]
  


#d)

total = 0
for i in range (2, 11):
    total = total + a[i]      
    



#e)

total = 0
i = 1
while i < 10:
    total = total + a[i]     
    i = 2 * i
    
print(total)



#f)

total = 0
for i in range (9, -1, -1):
    total = total + a[i]      



#g)

total = 0
for i in range (9, -1, -2):
    total = total + a[i]  
   

#h)

total = 0
for i in range (0, 10):
    total =  a[i] - total 
    
print(total)

"""

#Oppgave 2

from random import randint

values = []

for i in range(10):
    number = randint(0, 100)
    values.append(number)

    
print(values, "\n") #\n lager mellom me


#Oppgave 3

"""

#a)

for number in values:
    print(number, end=" ")



#b)

count = 0
for number in values:
    while count <  1:
        print(sum(values))
        count = count + 1
    



#b2)


for number in values:
    print(sum(values))
    break



#4
even=[] #definere liste for even tall
odd=[] #definere liste for odd tall
for number in values: # går igjennom hvert tall i lista
    if number %2 == 0: # hvis tallet er even
        even.append(number) #legges det til i even lista
    else: #hvis ikke 
        odd.append(number) #legges den inn i oss lista
print("Even list",even,"Odd list",odd) #printer ut begge listene

"""
#5
count = 0
if count < 10:
    for number in values: # går igjennom hvert tall i lista    
        if number %2 != 0: # hvis tallet er even
            values.remove(number)
            count += 1

print(values)
  