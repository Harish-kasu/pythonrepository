import random

a,b = 1,100

num = random.randint(a,b)


guess = int(input(f" guess a number between {a} and {b} : "))
guesses = 0

while True:
    guesses += 1
    if guess < num:
        print(f"your guess {guess} is too low")
        guess = int(input(f" guess a number between {a} and {b} : "))
    elif guess > num:
        print(f"your guess {guess} is too high ")
        guess = int(input(f" guess a number between {a} and {b} : "))
    else:
        print(f"your guess {guess} is correct : ")
        break

print(f" you guessed the number in {guesses} guesses ")


