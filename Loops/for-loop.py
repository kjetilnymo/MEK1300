"""
string = "Python"

i = 0

#while loop
#while i < len(string):
#    print(string[i])
#    i = i + 1
    
#for loop
for char in string:
    print(char)
    


#while loop
i = 0

while i < 10:
    print(i)
    i = i +1

#for loop 
for i in range(1, 11):
    print(i)
    


for i in range(40,20,-2):
    print (i)
    
for i in range(2):
    print("Hi")
    
"""

INITIAL_BALANCE = 10000
RATE = 0.05

num_years = int(input("Enter the number of years: "))

balance = INITIAL_BALANCE

#print("%5s %12s" % ("Year", "Balance"))
print(f"{'Year':5s} {'Balance':>12s}")
print("-" * 20)

for year in range(1, num_years+1):
    interest = balance * RATE
    balance = balance + interest
    print("%3d %14.2f" % (year, balance))
    
    


RMAX = 15
CMAX = 5

for i in range(1, CMAX + 1):
    print("%10d" % i, end="")
print()

for _ in range(1, CMAX + 1):
    print("%10s" % "x", end="")
print()
    
print("   ", "-" * 40)

for x in range(1, RMAX+1):
    for n in range(1, CMAX+1):
        print("10d" % x ** n, end="")
    print()