#oppgave 1
from random import randint


values = []

for i in range(10):
    number = randint(0, 100)
    values.append(number)

    
print(values, "\n") #printer lista 
sorted_liste=sorted(values) #lager en ny liste der talla fra values blir sortet
print(sorted_liste) #printer den nye lisa


 #oppgave 2
a=[1,4,9,16,9,7,4,9,11] #definere listene
b=[11,11,7,9,16,4,1] 

def same_list(a,b): # definere funksjon, som skal ta imot to lister a og b
    a=set(a) #ser bort fra duplikater
    b=set(b)
    if a == b:#ser om de inneholder like verdier
        return True #Hvis ja printes True ut
    else:
        return False
       
print(same_list(a,b))#tilkaller funksjonen og retunere det som står i return




#oppgave 3
from random import randint


def sum_without_smallest(): #definere funksjon
    values = [] #definere en liste
    total=0 #definere en total verdien
    for i in range(10): #går  igjennom løkka 10 ganger
        number = randint(0, 100) #generer 10 random tall 
        values.append(number) #setter inn tallene i values lista
        total+=number #hver gang den går gjennom lista legger den verdien inn i Total
    print(values) #printer bare lista
    return total-min(values) #funksjonen skal gi ut total verdien minus minste verdi
    
print(sum_without_smallest()) #kaller på funksjonen for verdien som oppgis inni

#oppgave 4

def list_without_smallest(): #lager liste
    a=[1,2,3,4,5,6,7,8] #definere lista
    smallest=a[0] #antar at første tall i plass [0] er minst
    index=0 #antar at indexe til smallest er 0
    for i in a: #går igjennom hver index i lista
         if a[index]<smallest: #hvis tallet i index (i) er mindre enn smallest
            smallest=a[i] #oppdater smallest til dette tallet
            index=i #lagrer hvilket index dette tallet er på
    del a[index] #fjerner denne verdien fra lista
    return a #gir tilbake lista uten inden (i)
print(list_without_smallest()) #kalles på funksjonen

            


        




