import random
import art


def game_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        return 0

def guess_a_num(answer):
    lives = game_level()
    game_over = False
    while not game_over:
        if lives == 0:
            print("You've run out of guesses. Refresh the app to run again.")
            game_over = True
        else:
            print(f"You have {lives} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == answer:
                print(f"You got it! The answer was {guess}")
                game_over = True
            elif guess > answer:
                print("Too high.\n"
                      "Try again.")
                lives -= 1
            elif guess < answer:
                print("Too low.\n"
                      "Try again.")
                lives -= 1
            else:
                print("Try again.")

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    rand_num = random.randint(0,100)
    # print(f"Naisho desu yo: {rand_num}")
    guess_a_num(rand_num)

game()


# # Bootcamp Solution
# from random import randint
# from art import logo


# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5


# # Function to check users' guess against actual answer
# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns - 1
#     else:
#         print(f"You got it! The answer was {actual_answer}")


# # Function to set difficulty
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS


# def game():
#     print(logo)
#     # Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(1, 100)
#     print(f"Pssst, the correct answer is {answer}")

#     turns = set_difficulty()

#     # Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         # Let the user guess a number
#         guess = int(input("Make a guess: "))
#         # Track the number of turns and reduce by 1 if they get it wrong
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses, you lose.")
#             return
#         elif guess != answer:
#             print("Guess again.")




# game()


