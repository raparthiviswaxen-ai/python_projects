import random


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

images = [rock, paper, scissors]

user_choice = int(input("choose a number to play: 0 for rock, 1 for paper or 2 for scissor \n"))
if user_choice >= 0 and user_choice <= 2:
   print(images[user_choice])

computer_choice = random.randint(0, 2)
print("computer choose: ")
print(images[computer_choice])

if user_choice > 2 or user_choice < 0:
    print("Its a wrong number, you lose and computer won!")
elif user_choice == 0 and computer_choice == 2:
    print("You Won!")
elif user_choice > computer_choice:
    print("You Won!")
elif computer_choice > user_choice:
    print("You Lose!")
elif computer_choice == user_choice:
    print("it's a Draw! ")








# # two = ["rock", "paper", "scissors"]
# # kiss = [one, two]
#
# ch = int(input("choose a number to play, 0 for rock, 1 for paper and 2 for scissors \n"))
# print()
# if ch == 0:
#     print(rock)
# elif ch == 1:
#     print(paper)
# elif ch == 2:
#     print(scissors)
# else:
#     print("choose only from above numbers")
#
#
# ch2 = random.choice(one)
# print("computer choose:")
# if ch2 == rock:
#     print(rock)
# elif ch2 == paper:
#     print(paper)
# else:
#     print(scissors)
#
# if ch == 0 & ch2 == [0]:
#     print("game tied")
# if ch == 0 & ch2 == [1]:
#     print("you lost")
# if ch == 0 & ch2 == [2]:
#     print("you won")










# game1 = input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors \n")
# print("you choose:")
# if game1 == 0:
#     print(rock)
# elif game1 == 1:
#     print(paper)
# else:
#     print(scissors)
#
# a=["rock", "paper", "scissors"]
# game2 = random.choice(a)
# print("Computer choose:")
#
# if game2 == "rock":
#     print(rock)
# elif game2 == "paper":
#     print(paper)
# else:
#     print(scissors)
#
#
# if game1 == game2:
#     print("Its a Draw!")
# elif game1 == 0 & game2 == "paper":
#     print("you lost!")
# else:
#     print("its wrong")