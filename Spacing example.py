price = 1.7457468494

print(price)
print("%6.3f" % price) #6 = antall plasser: med/foran tallet. 3: antall desimaler i tallet.


title1 = "quantity:"
title2 = "price:"

print("%10s %10d" % (title1, 24))
print("%10s %10.2f" % (title2, 17.29))

print(f"{title1:<10s} {24:10d}")
print(f"{title2:<10s} {17.6754:10.3f}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

#print("Hi " + name + ". You are " + str(age) + " years old.")
