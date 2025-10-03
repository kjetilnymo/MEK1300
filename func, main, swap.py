"""
def main():
    choice = menu()
    while choise != 5:
        if choice < 1 or choice > 5:
            print("Invalid input!")
            
        else:
            num1 = int(input("\n Enter number 1: "))
            num2 = int(input("Enter number 2: "))
            
            if choice == 1:
                result = add(num1, num2)
                print(f"{num1 + {num2} = {result}")
                
                



x = 10 #Lokal variabel

def my_func():
    print("Inside the function: ", x)
    
my_func()
print("Inside the function: ", x)



count = 0 # global variabel

def increment():
    global count
    count += 1
    print("Inside function: ", count)
    
def decriment():
    global count
    count -= 1
    
increment()
print("Outside function: ", count)

"""

a = int(input("Enter b: "))
b = int(input("Enter a: "))

def main():
    print("\nBefore swap: ")
    print("a =", a)
    print("b =", b)
    
    swap(a, b)
    
    print("\nAfter swap: ")
    print("a =", a)
    print("b =", b)
    
def swap():
    global a, b
    temp = a
    a = b
    b = temp
    
main()
    
    
    
    
    
    
    