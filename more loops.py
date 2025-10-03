"""
n = int(input("Enter a positive integer: "))

i = 1

if n < 1:
    print("Invalid input")
else:
    print("The odd number(s) till number", n, "-->", end=" ")
    while i < n:
        if i % 2 != 0:
            print(i, end=" ")
        i = i + 1
        



n = int(input("Enter the number you want in the first row: "))

i = 1

while i <= n:
    j = 0
    while j <= n - i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1
    
    

EMPLOYEE = 5
i = 1

while i <= EMPLOYEE:
    monthly_sales = float(input("Enter monthly sales: "))
    
    if monthly_sales >= 30000:
        income = 575 + monthly_sales * 0.2
        
    elif monthly_sales >= 25000:
        income = 520 + monthly_sales * 0.1
        
    elif monthly_sales >= 20000:
        income = 500 + monthly_sales * 0.05
        
    elif monthly_sales > 0:
        income = 400 + monthly_sales * 0.02
        
    else:
        print("Invalid input!")
        
    print("Income is", income)
    i = i + 1
    

"""

from random import randint

heads = 0 #1
tails = 0 #2

i = 1

while i <= 10:
    coin = randint(1,2)
    if coin == 1:
        heads += 1
    else:
        tails += 1
    
    i = i + 1
    
print("heads =", heads)
print("tails =", tails)














    
        
