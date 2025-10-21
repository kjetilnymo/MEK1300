#legger hver bokstav i stringen du har skrvete inn i dictonaey
string=input("enter a string: ")

characters={}

for char in string:
    characters[char]=characters[char]+1

for char in string:
    characters[char]=characters[char]+1

print(characters)



#søke etter key som ikke fins uten å få error
my_d={'a':1, 'b':2}
print(my_d.get('d', "NO")) #ser vi key d er den hvis ikke skrives NO


def main():
    my_contacts={"Fred":98646829, "Mary":97676939, "Bob": 47899983}

    if "Fred" in my_contacts:
        print("Number for Fred ->", my_contacts[Fred])
    else:print ("Fred is nor in my contact list. ")

    name_list=find_names(my_contacts, 98646829)
    print("Names for 98646829:," end="")

    print()

    print_all(my_contacts)

def find_names(contacts,number):
    name_list=[]
    for name in contacts:
        if contacts[name]==number:
            name_list.append(name)
    
    return name_list

def print_all(my_contacts):
    print("All names and numbers: ")
    for key in sorted(contacts)
    print("%10s %d" % key, contacts[key])

    #oversette tall til tekst
def main():
    dictionary={
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


    phone_number = input("enter your phone number: ")
    result = translate(dictionary, phone_number)
    print(result)



def translate(dictionary, phone_number):
    result = ""
    for char in phone_number:
        result += dictionary.get(char,"?")
        result += " "
    return result

main()