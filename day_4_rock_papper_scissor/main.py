rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
rps = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player_chose = int(input())
computer_chose = random.randint(0, 2)

if player_chose >= 0 and player_chose <= 2:
    print(rps[player_chose])
    print("Computer chose:")
    print(rps[computer_chose])

if player_chose >= 3 or player_chose < 0 :
    print("Invalid number. Game Over!")
elif player_chose == 0 and computer_chose == 2:
    print("You win!")
elif player_chose == 2 and computer_chose == 0:
    print("You Lose!")
elif computer_chose > player_chose:
    print("You Lose!")
elif player_chose > computer_chose:
    print("You Win!")
elif player_chose == computer_chose:
    print("It's a Draw!")