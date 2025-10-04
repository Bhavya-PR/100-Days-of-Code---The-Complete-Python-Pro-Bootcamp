import data
menu = data.MENU
resource = data.resources
resource['cost'] = 0
option = 'latte'

def users_choice():
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${resource['cost']}")
        customer_choice = users_choice()
    return customer_choice

def check_supplies(user_choice):
    reset = False
    if 'water' in menu[user_choice]['ingredients'] and (resource['water'] < menu[user_choice]['ingredients']['water']):
        print("Sorry there is not enough water.")
        reset = True
    elif 'coffee' in menu[user_choice]['ingredients'] and (resource['coffee'] < menu[user_choice]['ingredients']['coffee']):
        print("Sorry there is not enough coffee.")
        reset = True
    elif 'milk' in menu[user_choice]['ingredients'] and (resource['milk'] < menu[user_choice]['ingredients']['milk']):
        print("Sorry there is not enough milk.")
        reset = True
    return reset

def update_supplies(option,source):
    source['water'] -= menu[option]['ingredients']['water']
    source['coffee'] -= menu[option]['ingredients']['coffee']
    if 'milk' in menu[option]['ingredients']:
        source['milk'] -= menu[option]['ingredients']['milk']
    source['cost'] += menu[option]['cost']

while 1:
    choice = users_choice()
    if choice == 'off':
        break
    resets = check_supplies(choice)
    while resets:
        choice = users_choice()
        resets = check_supplies(choice)
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount_paid = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if amount_paid < menu[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        user_choice = users_choice()
        continue
    else:
        change =round(amount_paid - menu[choice]['cost'],2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice} ☕. Enjoy!")
        update_supplies(choice,resource)
print("Have a good day!")
