# # my solution
# import random
# import art

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# def hit_card(list_card: list):
#     list_card.append(random.choice(cards))

# def print_final_card(your_card, computer_card, sum_your_card, sum_comp_card):
#     print(
#     f"""
#     Your final hand: {your_card}, final score: {sum_your_card}
#     Computer's final hand {computer_card}, final score: {sum_comp_card}
#     """)

# def sum_card(list_card: list):
#     card_sum = 0
#     for card in list_card:
#         if card == 11:
#             if card_sum + card > 21:
#                 card_sum += 1
#             else:
#                 card_sum += card
#         else:
#             card_sum += card
#     return card_sum

# def black_jack():
#     is_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#     while is_play == "y":
#         print(art.logo)
#         your_card = random.sample(cards, 2)
#         computer_card = [random.choice(cards)]
#         sum_your_card = sum_card(your_card)
#         sum_comp_card = sum_card(computer_card)

#         def card_comparison(total_car1, total_card2):
#             if total_car1 == total_card2:
#                 print("You Draw!")
#             elif total_car1 > total_card2:
#                 print("You Win!!")
#             else:
#                 print("You Lose!!")

#         while sum_your_card < 21:
#             print(f"Your cards: {your_card}, current score: {sum_your_card}")
#             print(f"Computer's first card: {computer_card[0]}")
#             get_card = input("Type 'y' to get another card, type 'n' to pass: ")
#             if get_card == "y":
#                 hit_card(your_card)
#                 sum_your_card = sum_card(your_card)
#             elif get_card == "n":
#                 while sum_comp_card < 17:
#                     hit_card(computer_card)
#                     sum_comp_card = sum_card(computer_card)
#                 if sum_comp_card > 21:
#                     print_final_card(your_card, computer_card, sum_your_card, sum_comp_card)
#                     print("Computer went over. You Win!")
#                     black_jack()
#                 else:
#                     print_final_card(your_card, computer_card, sum_your_card, sum_comp_card)
#                     card_comparison(sum_your_card, sum_comp_card)
#                     black_jack()
#         if sum_your_card > 21:
#             print_final_card(your_card, computer_card, sum_your_card, sum_comp_card)
#             print("You went over. You lose!")
#             black_jack()
# black_jack()

#bootcamp solution
import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
