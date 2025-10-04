from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

working_condition = True
while working_condition:
    choice = input(f"What would you like? ({menu.get_items()}):").lower()
    if choice == "off":
        working_condition = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif menu.find_drink(choice):
        menuItem = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(menuItem) and moneyMachine.make_payment(menuItem.cost):
            coffeeMaker.make_coffee(menuItem)
