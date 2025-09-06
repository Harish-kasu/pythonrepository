import random

num = random.randint(1, 100)
guesses = 0

print("----------------------------------------------------")
print("--------python random number guessing game----------")
while True:
    guess = input("Guess a number between 1 and 100: ").strip()

    if guess.isdigit():
        guess = int(guess)
        if 1 <= guess <= 100:
            guesses += 1
            if guess < num:
                print(f"Your guess {guess} is too low.")
            elif guess > num:
                print(f"Your guess {guess} is too high.")
            else:
                print(f"Your guess {guess} is correct! You guessed it in {guesses} tries.")
                break
        else:
            print("Please enter a number between 1 and 100.")
    else:
        print("Please enter a valid number.")


     