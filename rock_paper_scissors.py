# 30.07.2021
# I suppose one can male it faster and easier. But for now I cannot.

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

user_choice = int(input(
    "Let's start the game! Here are the variants: "
    "1 is for rock, 2 is for paper and 3 is for scissors. "
    "What's your move? "))
py_choice = random.randint(1, 3)

if user_choice == py_choice:
    print("It's a draw!")

if user_choice > 3:
    print('Oh no, wrong choice!')

#  This part decides is user has won or not.
while user_choice == 1:
    print(f"You choice is \n{rock}")
    if py_choice == 3:
        print(f'Py chose: {scissors}\nYou won!')
    if py_choice == 2:
        print(f'Py chose: {paper}\nYou lost!')
    break

while user_choice == 2:
    print(f"You choice is \n{paper}")
    if py_choice == 1:
        print(f'Py chose: {rock}\nYou won!')
    if py_choice == 3:
        print(f'Py chose: {scissors}\nYou lost!')
    break

while user_choice == 3:
    print(f"You choice is \n{scissors}")
    if py_choice == 2:
        print(f'Py chose: {paper}\nYou won!')
    if py_choice == 1:
        print(f'Py chose: {rock}\nYou lost!')
    break
