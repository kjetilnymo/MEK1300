#MEK1300 - Exercise 1

from math import sqrt


#Verdier oppgave 1
x = 2.5
y = -1.5
m = 18
n = 4


#Oppgave 1 a-e
a = (x + n * y - (x + n) * y)
b = (m // n + m % n)
c =(5 * x - n / 5)
d = (1 - (1 - (1 - (1 - (1 - n)))))
e = (sqrt(sqrt(n)))

print(f"""
Oppgave 1:
    
    a) {a}
    b) {b}
    c) {c}
    d) {d}
    e) {e:.3f}""")

#Verdier oppgave 2
m = 18
n = 17

#Oppgave 2 a-f
a = n // 10 + n % 10
b = n % 2 + m % 2
c = (m + n) // 2
d = (m + n) / 2.0
e = int(0.5 * (m + n))
f = int(round(0.5 * (m + n)))

print(f"""
      
Oppgave 2:
    
    a) {a}
    b) {b}
    c) {c}
    d) {d}
    e) {e}
    f) {f}""")
    
#Verider oppgave 3
s = ("Hello")
t = ("World")

#Oppgave 3 a-g
a = len(s) + len(t)
b = s[1] + s[2]
c = s[len(s) // 2]
d = s + t
e = t + s
f = s * 2

print(f"""
      
Oppgave 3:
    
    a) {a}
    b) {b}
    c) {c}
    d) {d}
    e) {e}
    f) {f}
    """)

    
#Oppgave 4 a-e
print(f"""
Oppgave 4:
    """)

Number1 = float(input("Enter number 1: "))
Number2 = float(input("Enter number 2: "))

summ = Number1 + Number2
difference = Number1 - Number2
product = Number1 * Number2
average = (Number1 + Number2) / 2
distance = abs(Number1 - Number2)
maximum = max(Number1, Number2)
minimum = min(Number1, Number2)
    
print(f"""
      a) The sum is {summ}
      b) The difference is {difference}
      c) The product is {product}
      d) The average is {average}
      e) The distance is {distance}
      f) The maximum value is {maximum}
      g) The minimum value is {minimum}""")
    

#Oppgave 5
print(f"""\n
      
Oppgave 5:
""")
print(f"{'Sum =':<15} {summ:.0f}")
print(f"{'Difference =':<15} {difference}")
print(f"{'Product =':<15} {product}")
print(f"{'Average =':<15} {average}")
print(f"{'Distance =':<15} {distance}")
print(f"{'Maximum =':<15} {maximum}")
print(f"{'Minimum =':<15} {minimum}")



#Oppgave 6
print(f"""
      
Oppgave 6:
    """)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"""
The Area of the rectangle is {area}
The Perimeter of the rectangle is {perimeter}""")


#Oppgave 7
print(f"""
      
Oppgave 7:
    """)
word = str(input("Enter a word: "))

first_two = word[:2]
last_two = word[-2:]

result = first_two + "..." + last_two

print(result)


#Oppgave 8
print(f"""
      
Oppgave 8:
    """)
number = str(input("Enter a five digit number: "))

number_one = number[0]     
number_two = number[1] 
number_three = number[2]
number_four = number[3] 
number_five = number[4] 

result = number_one + " " + number_two + " " + number_three + " " + number_four + " " + number_five                

print(result)














