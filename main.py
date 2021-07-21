import ITEMS
coffee_list = ITEMS.MENU
coffee_resources = ITEMS.resources
coffee_money = 0

def calculate_money(q, d, n, p):
    """ 
    This function accepts three arguments to calculate the money 
    inserted into the coffee machine
    """""
    quarters_inserted = 0.25 * q
    dimes_inserted = 0.1 * d
    nickles_inserted = 0.05 * n
    pennies_inserted = 0.01 * p
    sum_money = quarters_inserted + dimes_inserted + pennies_inserted + nickles_inserted

    return round(sum_money, 2)


def make_coffee(user_choice, list_coffee, resour):
    """ 
    Reduce the resources in the coffee machine
    """""
    for item in list_coffee[user_choice]['ingredients']:
        resour[item] -= list_coffee[user_choice]['ingredients'][item]
    return True


def check_resources(user_choice, resources, list_coffee):
    """
    Check the resources in the coffee machine if another
    drink can be purchased
    """""
    if resources['water'] < list_coffee[user_choice]['ingredients']['water']:
        print("Sorry there is not enough water")
        return False
    elif resources['milk'] in list_coffee[user_choice]['ingredients']:
        if resources['milk'] < list_coffee[user_choice]['ingredients']['milk']:
            print("Sorry there is not enough milk")
            return False
    elif resources['coffee'] < list_coffee[user_choice]['ingredients']['coffee']:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True
    return True


def check_money(user_choice, list_coffee, cal_money):
    """ 
    Check money that the user put into the coffee machine
    """""
    global coffee_money
    if cal_money < list_coffee[user_choice]['cost']:
        print("Sorry you do not have enough money. Money refunded")
        return False
    elif cal_money >= list_coffee[user_choice]['cost']:
        change = cal_money - list_coffee[user_choice]['cost']
        print(f"Here is your change ${round(change,2)}")
        print(f"Enjoy your {user_choice}!!")
        coffee_money = list_coffee[user_choice]['cost']
        return True



q = True
while q:
    user_input = input("What would you like? (espresso, latte, cappuccino): ")
    if user_input in coffee_list:
        if check_resources(user_input,coffee_resources,coffee_list):
            print("Please insert coins")
            quarters = int(input("how many quarters: "))
            dimes = int(input("how many dimes: "))
            nickles = int(input("how many nickles: "))
            pennies = int(input("how many pennies: "))
            total_money = calculate_money(quarters, dimes, nickles, pennies)
        if check_resources(user_input,coffee_resources,coffee_list):
            total_money
            if check_money(user_input,coffee_list,total_money):
                make_coffee(user_input,coffee_list,coffee_resources)
    elif user_input == 'report':
        print(f"Water: {coffee_resources['water']}ml")
        print(f"Milk: {coffee_resources['milk']}ml")
        print(f"Coffee: {coffee_resources['coffee']}g")
        print(f"Money: ${coffee_money}")
    else:
        q = False
