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
    report = '\n'.join([f'{resource.capitalize()}: {amount}{units[resource]}' for resource, amount in resources.items()]) + f'\nMoney: ${machine_money:.2f}'
    print(report)

def is_resource_sufficient(drink):
    ingredients = menu[drink]['ingredients'].items()
    for key, value in ingredients:
        if resources[key] < value:
            return f'Sorry there is not enough {key}'
    return None

def get_coins():
    prompt = 'How many {0}? '
    coins = ['quarters', 'dimes', 'nickles', 'pennies']
    return {coin : get_integer(prompt.format(coin)) for coin in coins}

def coin_to_value(coin):
    return {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }[coin]

def check_payment(coins, drink):
    money = 0
    drink_price = menu[drink]['cost']

    for key, value in coins.items():
        money += (coin_to_value(key) * value)

    if money == drink_price:
        global machine_money
        machine_money += money
        return None
    elif money > drink_price:
        difference = money - drink_price
        machine_money += drink_price
        return f'Here is ${round(difference, 2)} dollars in change.'
    else:
        return 'Sorry that\'s not enough money. Money refunded.'

def prepare_drink(drink):
    drink_ingredients = menu[drink]['ingredients'].items()
    for key, value in drink_ingredients:
        resources[key] -= value
    return f'Here is your {drink}'

def make_drink(drink):
    enough_resources = is_resource_sufficient(drink)
    payment = check_payment(get_coins(), drink)
    if enough_resources == None and not 'Sorry' in payment:
        if payment:
            print(payment)
        print(prepare_drink(drink))
    else:
        if enough_resources:
            print(enough_resources)
        print(payment)

def main():
    off = False
    while not off:
        match get_choice():
            case 'off':
                off = True
            case 'report':
                print_report()
            case 'latte':
                make_drink('latte')
            case 'cappucino':
                make_drink('cappucino')
            case 'espresso':
                make_drink('espresso')
            case _:
                print('Invalid option. Try again')

if __name__ == '__main__':
    main()