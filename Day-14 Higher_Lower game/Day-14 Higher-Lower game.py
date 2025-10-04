import art, game_data, random
print(art.logo)

data = game_data.data
def random_choice():
    return random.choice(data)

def game(current_score):
    data1 = random_choice()
    data2 = random_choice()
    if data1 == data2:
        data2 = random_choice()
    while 1:
        print(f"Compare A: {data1['name']}, {data1['description']}, {data1['country']}")
        print(art.vs)
        print(f"Against B: {data2['name']}, {data2['description']}, {data2['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a' and data1['follower_count'] > data2['follower_count']:
            print("\n" * 20)
            print(art.logo)
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            data2 = random_choice()
            if data1 == data2:
                data2 = random_choice()
        elif guess == 'b' and data2['follower_count'] > data1['follower_count']:
            print("\n" * 20)
            print(art.logo)
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            data1 = data2
            data2 = random_choice()
            if data1 == data2:
                data2 = random_choice()
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            return

game(current_score=0)