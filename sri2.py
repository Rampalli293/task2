import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            number_of_guesses += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {number_of_guesses} guesses.")
                break
        except ValueError:
            print("Please enter a valid number.")

if _name_ == "_main_":
    number_guessing_game()
