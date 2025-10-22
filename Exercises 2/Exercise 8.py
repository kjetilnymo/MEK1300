#Oppgavee 2
#a
grade_count={"A":8, "D":3, "B":15, "F":2, "C":6}
for key in grade_count:
    print(key)
#e
total=0 #definere total
for value in grade_count.values():#går igjennom values
    total+=value #setter value veriden inn i total
print(total/len(grade_count)) #deler total som er sum av values, deler det på antall values


#oppgave 3
def main():
    s_g={}
    def update():
        name_student=input("Skriv inn navnet til studenten:")
        if name_student in s_g:
            grade_student=input("skriv inn studentens nye karakter: ")
            s_g[name_student]=grade_student

    action=input("Velg mellom add, remove, update, print: ")

    if action=="add":
        name_student=input("Skriv inn navnet til studenten: ")
        grade_student=input("skriv inn studentens karakter: ")
        s_g[name_student]=grade_student
        print(s_g)
    elif action=="remove":
        name_student=input("Skriv inn navnet til studenten:")
        grade_student=input("skriv inn studentens karakter: ")
        s_g.pop(name_student)
        print(s_g)

    elif action=="update":
      name_student=input("Skriv inn navnet til studenten:")
      if name_student in s_g:
              update()
        
     

main()


 