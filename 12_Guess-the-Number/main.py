# TODO 1: Randomly select a number between 1 - 100
# TODO 2: Ask the player to choose the difficulty level
# TODO 3: Tell how many attempts are remaining to guess
# TODO 4: Ask the user to make a guess.
# TODO 5: Compare the user guessed and selected number and tell if guessed right,
#  or else is it higher or lower than what the number is.
# TODO 6: If the incorrect number is guessed, reduce the life and ask to guess again until lives are available.
# TODO 7: End th game if they guess correctly or if they are out of lives


from random import randint
from art import logo

#creating global constants for lives to use in any function
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return None


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    #print(f"The correct answer is {answer}")

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print(f"You've run out of guesses. The answer was {answer}.")
            return
        elif guess!= answer:
            print("Guess again.")


game()