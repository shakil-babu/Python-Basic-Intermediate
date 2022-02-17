# =================== Number guessing game ==============
import random


# secret number
secretNumber = random.randint(1, 10)

# run game


def run_game():
    guesses = []
    guess = 0

    while len(guesses) < 5:
        try:
            guess = int(input("Guess a number between 1 to 10 :"))
        except ValueError:
            print("{} is not a number!".format(guess))

        else:
            if guess == secretNumber:
                print("Congo! you got the number {}".format(guess))
                break
            elif guess > secretNumber:
                print("{} is too high".format(guess))

            elif guess < secretNumber:
                print("{} is too low!".format(guess))

            else:
                print("Sorry! that's not it!")

        guesses.append(guess)


# invock function
run_game()
