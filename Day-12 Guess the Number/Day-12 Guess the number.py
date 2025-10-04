import random, art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
original_number = random.randint(1,100)

def core_logic(attempt):
    is_play = True
    while is_play and attempt > 0:
        guess = int(input("Make a guess: "))
        if guess < original_number:
            attempt -= 1
            print("Too low.")
            print("Guess again.")
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif guess > original_number:
            attempt -= 1
            print("Too high.")
            print("Guess again.")
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {original_number}")
            is_play = False
    if attempt == 0:
        print("You've run out of guesses, you lose.")
        return
    return

if level == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
    core_logic(attempts)
else:
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5
    core_logic(attempts)
