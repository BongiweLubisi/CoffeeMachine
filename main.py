from mymenu import MENU, resources


machine_on = True
money = 0

while machine_on:
    enough_resource = True
    while enough_resource:
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if option == "report":
            print(f'Water: {resources["water"]} \nMilk: {resources["milk"]} \nCoffee: {resources["coffee"]} \nMoney: ${money}')
        elif option == "espresso" or "latte" or "cappuccino":
            if option == "latte" or option == "cappuccino":
                if resources["milk"] < MENU[option]["ingredients"]["milk"]:
                    print("Sorry, the isn't enough milk")
                    enough_resource = False
            if resources["water"] < MENU[option]["ingredients"]["water"]:
                print("Sorry, the isn't enough water")
                enough_resource = False
                if resources["coffee"] < MENU[option]["ingredients"]["coffee"]:
                    print("Sorry, the isn't enough coffee")
                    enough_resource = False
            else:
                print("Please insert coins!")
                quarter = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickles = int(input("How many nickles: "))
                pennies = int(input("How many pennies: "))
                total = (0.25 * quarter) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
                money += total

                option_cost = MENU[option]["cost"]
                change = money - option_cost
                round(change, 2)
                if money >= option_cost:
                    print(f"Here is ${change} in change")
                    print(f"Here is your {option}. Enjoy!")
                    money -= total
                    resources["water"] -= MENU[option]["ingredients"]["water"]
                    resources["coffee"] -= MENU[option]["ingredients"]["coffee"]

                    if option == "latte" or option == "cappuccino":
                        resources["milk"] -= MENU[option]["ingredients"]["milk"]

                else:
                    money -= total
                    print(f"Sorry!, That's not enough money. Money refunded")





