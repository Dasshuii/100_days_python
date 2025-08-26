menu = {
    'espresso': {
        'cost': 1.5,
        'ingredients': {
            'water': 50,
            'milk': 0,
            'coffee': 10,
        }
    },
    'latte' : {
        'cost': 3.0,
        'ingredients': {
            'water': 100,
            'milk': 150,
            'coffee': 3,
        }
    },
    'cappucino' : {
        'cost': 2.25,
        'ingredients': {
            'water': 125,
            'milk': 100,
            'coffee': 6
        }
    },
}
actions = ['report', 'off']
resources = {
    'water': 500,
    'milk': 300,
    'coffee': 175,
}
units = {
    'water': 'ml',
    'milk': 'ml',
    'coffee': 'g'
}
machine_money = 0

def get_integer(prompt):
    user_input = input(prompt)
    while not user_input.isdigit():
        user_input = input(prompt)
    return int(user_input)

def get_choice():
    '''
    Ask for user decision if the decision is not in actions or menu ask it again.
    '''
    prompt = f'What would you like? (espresso ${menu['espresso']['cost']}/latte ${menu['latte']['cost']}/cappucino ${menu['cappucino']['cost']}): '
    menu_items = menu.keys()
    choice = input(prompt)
    while choice not in actions and choice not in menu_items:
        choice = input(prompt)
    return choice

def print_report():
    for key, value in resources.items():
        print(f'{key}: {value}{units[key]}')
    print(f'Money: ${machine_money:.2f}')

def is_resource_sufficient(drink):
    ingredients = menu[drink]['ingredients']
    for key, value in ingredients.items():
        if resources[key] < value:
            return False
    return True

def get_coins():
    prompt = 'How many '
    coins = {
        'quarters': get_integer(prompt + 'quarters? '),
        'dimes': get_integer(prompt + 'dimes? '),
        'nickles': get_integer(prompt + 'nickles? '),
        'pennies': get_integer(prompt + 'pennies? ')
    }
    return coins

def coin_to_value(coin):
    coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }
    return coins[coin]

def check_payment(coins, drink):
    money = 0
    drink_price = menu[drink]['cost']

    for key, value in coins.items():
        money += (coin_to_value(key) * value)

    if money >= drink_price:
        global machine_money
        machine_money += money
        return True
    # elif money > drink_price:
    #     difference = money - drink_price
    #     machine_money += drink_price
    #     return round(difference, 2)
    else:
        return False

def prepare_drink(drink):
    drink_ingredients = menu[drink]['ingredients']
    for key, value in drink_ingredients.items():
        resources[key] -= value
    return f'Here is your {drink}'

def main():
    off = False
    while not off:
        choice = get_choice()
        off = choice == actions[1]
        if choice in menu.keys():
            coins = get_coins()
            if is_resource_sufficient(choice) and check_payment(coins, choice):
                print(prepare_drink(choice))
            else:
                print('Not enough resources or insufficient money')
        elif choice == actions[0]:
            print_report()
        else:
            print('Invalid option. Try again.')


if __name__ == '__main__':
    main()