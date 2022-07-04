MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def check_sufficient(drink_type):
    drink_type = drink_type.lower()

    if drink_type == "espresso":
        if MENU[drink_type]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water")
            return False
        if MENU[drink_type]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
    elif drink_type == "latte" or drink_type == "coffee":
        if MENU[drink_type]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water")
            return False
        if MENU[drink_type]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        if MENU[drink_type]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
    return True


def print_report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["water"]) + "g")
    print("Money: $" + str(money))


def process_transaction(q, d, n, p, cost):
    total = 0
    while q > 0:
        q -= 1
        total += 0.25
    while d > 0:
        d -= 1
        total += 0.10
    while n > 0:
        n -= 1
        total += 0.05
    while p > 0:
        p -= 1
        total += 0.01
    if total < cost:
        return False
    elif round(total, 2) > cost:
        # calculate change
        print("Your change is $" + str(round(total-cost, 2)))
        return True
    else:
        return True


def make_coffee(coffee):
    if coffee == "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]


while True:
    selection = input("What would you like? (espresso/latte/cappuccino):").lower()
    if selection == "off":
        exit()
    elif selection == "print report":
        print_report()
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        if check_sufficient(selection):
            # check for coins
            print("Please insert coins.")
            quarters = float(input("How many quarters?:"))
            dimes = float(input("How many dimes?:"))
            nickels = float(input("How many nickels?:"))
            pennies = float(input("How many pennies?:"))
            transaction_result = process_transaction(quarters, dimes, nickels, pennies, MENU[selection]["cost"])
            if not transaction_result:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += MENU[selection]["cost"]
                make_coffee(selection)
                print("Here is your latte. Enjoy!")
    else:
        print("Please enter either espresso/latte/cappuccino")
