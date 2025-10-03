from random import random, randint, uniform

"""

number = random()

print(number)



for _ in range (10):
    number = random()
    print(f"{number:.3f}")

for _ in range(10):
    number = random.uniform(2, 14)
    print(number)

"""

for _ in range(1):
    d1 = randint(1, 100)
guess1 = int(input("Guess a number: "))
if guess1 == d1:
    print("Congratulations! You guessed the number in ** attempt(s).")
elif guess1 < d1:
    print("The number is higher")
    newguess = int(input("Guess again: "))
elif guess1 > d1:
    print("The number is lower")
    newguess = int(input("Guess again: "))