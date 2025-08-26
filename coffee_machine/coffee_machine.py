MENU = {
    'espresso' : {
        'ingredients' : {
            'water' : 50,
            'coffee' : 18,
        },
        'cost' : 1.5
    },
    'latte': {
        'ingredients' : {
            'water' : 200,
            'milk' : 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappucino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0
    },
}
coins = {
    'quarters': 0,
    'dimes': 0,
    'nickles': 0,
    'pennies': 0,
}
resources = {
    'water' : 300,
    'milk': 200,
    'coffee' : 100,
    'money' : 0
}

def check_enough_resources(drink):
    ingredients_required = MENU[drink]['ingredients'].items()
    for key, value in ingredients_required:
        if (value > resources[key]):
            return key
    return None

def make_drink(drink):
    ingredients_required = MENU[drink]['ingredients'].items()
    for key, value in ingredients_required:
        resources[key] -= value
            
def print_report():
    for key, value in resources.items():
        print(f'{key.capitalize()}: {value}')

def insert_coins():
    for key in coins.keys():
        coins[key] = int(input(f'How many {key}?: '))

def sum_coins():
    return sum(coins.values())

def get_drink():
    prompt = 'What would you like? (espresso/latte/cappucino): '
    drink = input(prompt)
    while (drink not in MENU) and (drink not in ['off', 'report']):
        print('Invalid drink. Try again')
        drink = input(prompt)
    return drink

def print_menu():
    for drink, value in MENU.items():
        print(f'{drink} : ${value['cost']}')

def main():
    drink = get_drink()
    print_report()

            
        
if __name__ == '__main__':
    main()