online_signups=["Alice", "Bob", "Charlie", "David", "Alice","Eva"] #list, tilatter log in mer enn en gang

Previous_attendees=("Bob", "Charli", "Frank", "Grace") #Topuls, viser hvem møt kan ikke endres

Banned_students={"Eva", "Frank"} #set fordi rekkfølge ikke viktig

#remove dulpicates

Unique_signups=set(online_signups)
print("Unique online signups", Unique_signups)


#remove banned students fra unique_signups
allowed_students=Unique_signups-Banned_students
print("Allowed students", allowed_students)

#se hvem første gang studentene er
Previous_set=set(Previous_attendees) #gjør om til set
first_time_students=allowed_students-Previous_set
print("First time studen")

def main():  #lager hoved funksjon
    sentence=input("enter a sentence: ") #ber brukeren skrive inn
    u_set=set() #lager tomt sett
    words=sentence.split() #deler setningen inn i ord
    print(words) #skriver ut liste av ord

for word in words: #loppen går igjen ordene og passer dem til neste def
    cleaned=clean(word) #sender ordene til funksjon clean
    u_set.add(word) #legger ordene inn i settene
    print(u_set) 

def clean(string):
    result="" #starter med tom tekst
    for char in string: #skjekker hver element
        if char.isalnum(): #hvis element er tall/bokstav
            result=result+char.lower() #resultatet får den stringen
    return result
main()


