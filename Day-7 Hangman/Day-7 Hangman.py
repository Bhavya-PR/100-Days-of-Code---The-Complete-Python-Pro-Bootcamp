import random
import hangman_words
import hangman_art

stages = hangman_art.stages
word_list = hangman_words.word_list
logo = hangman_art.logo

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Word to guess : {placeholder}")
print(f"**************************** {lives}/6 LIVES LEFT ****************************")

display = ["_"] * len(chosen_word)
completed= False
while not lives <= 0 and not completed:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(stages[lives-1])
        print(f"You've already guessed {guess}")
        continue
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
        if "_" not in display:
            completed = True
    if guess not in display:
        print(stages[lives-1])
        print(f"You guesses {guess}, that's not in the word.\nYou lose a life.")
        lives -= 1
    else:
        print(stages[lives])
    print(f" Word to guess : {"".join(display)}")
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
if completed:
    print("You Win!")
else:
    print(f"IT WAS {chosen_word}! You Lose!")