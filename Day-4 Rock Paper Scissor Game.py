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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
choices = [rock,paper,scissors]
if choice not in (0,1,2):
    print("Can't print the image!")
else:
    print(choices[choice])
print(f"Computer's choice:\n{choices[computer_choice]}")
if choice > 2 or choice < 0:
    print("Not a valid choice!!!")
elif choice == computer_choice:
    print("It's a draw.")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
