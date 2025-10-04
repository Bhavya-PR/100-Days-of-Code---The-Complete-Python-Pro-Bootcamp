import art, random
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card():
    return random.choice(card)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You went over. You lose."
    elif u_score == 0:
        return "Opponent went over. You win."
    elif u_score > 21:
        return "You went over. You lose."
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "Opponent went over. You win."
    else:
        return "You went over. You lose."

def blackjack():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else :
            choice = input("Type 'y' to draw another card or 'n' to pass: ").lower()
            if choice == 'y':
                user_cards.append(deal_card())
            elif choice == 'n':
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} , Final score: {user_score}")
    print(f"Computer's final hand: {computer_cards} , Final score: {computer_score}")
    print(compare(user_score,computer_score))

user_choice = input("Do you want to play Blackjack? Type 'y' for yes and 'n' for no: ").lower()
while user_choice == 'y':
    print(art.logo)
    blackjack()
    user_choice = input("Do you want to play Blackjack? Type 'y' for yes and 'n' for no: ").lower()
print("Hey buddy! Don't you want to play the game?")
