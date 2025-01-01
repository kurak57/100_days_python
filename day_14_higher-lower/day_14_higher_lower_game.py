# My solution
import random
import os
from game_data import data
from art import  logo, vs

def person_string(person: dict):
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return f"{name}, {description}, from {country}"

def compare(p1,p2):
    if p1 > p2:
        return "a"
    else:
        return "b"

def game():
    score = 0
    person1 = random.choice(data)
    person2 = random.choice(data)
    while person1 == person2:
        person2 = random.choice(data)

    game_over = False

    while not game_over:
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print("Compare A:", person_string(person1))
        print(vs)
        print("Compare B:", person_string(person2))

        ply_inpt = input("Who has more followers? Type 'A' or 'B':").lower()
        answer = compare(person1["follower_count"], person2["follower_count"])
        if ply_inpt == answer:
            score += 1
            person1 = person2
            person2 = random.choice(data)
            while person1 == person2:
                person2 = random.choice(data)
            os.system('cls')
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True
game()

# #Bootcamp Solution
# # Display art
# from art import logo, vs
# from game_data import data
# import random


# def format_data(account):
#     """Takes the account data and returns the printable format."""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"


# def check_answer(user_guess, a_followers, b_followers):
#     """Take a user's guess and the follower counts and returns if they got it right."""
#     if a_followers > b_followers:
#         return user_guess == "a"
#     else:
#         return user_guess == "b"


# print(logo)
# score = 0
# game_should_continue = True
# # Generate a random account from the game data
# account_b = random.choice(data)

# # Make the game repeatable.
# while game_should_continue:

#     # Making account at position B become the next account at position A.
#     account_a = account_b
#     account_b = random.choice(data)

#     if account_a == account_b:
#         account_b = random.choice(data)

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")

#     # Ask user for a guess.
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#     # Clear the screen
#     print("\n" * 20)
#     print(logo)

#     # - Get follower count of each account
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]

#     # Check if user is correct.
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     # Give user feedback on their guess.
#     # score keeping.
#     if is_correct:
#         score += 1
#         print(f"You're right! Current score {score}")
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}.")
#         game_should_continue = False
