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

ascii_list = [rock, paper, scissors]
user_choice = int(input("Press 0 for Rock, 1 for Paper, and 2 for Scissors. Your choice: "))
computer_choice = random.randint(0, 2)

print(f"You chose {ascii_list[user_choice]}")
print(f"Computer chose {ascii_list[computer_choice]}")

if computer_choice == user_choice:
    print("It's a draw")
elif computer_choice == 0:
    if user_choice == 1:
        print("You win")
    else:
        print("You lose")
elif computer_choice == 1:
    if user_choice == 0:
        print("You lose")
    else:
        print("You win")
else:
    if user_choice == 0:
        print("You win")
    else:
        print("You lose")