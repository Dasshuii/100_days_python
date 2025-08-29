class MenuItem:
    def __init__(self, name : str, cost : float, ingredients : dict) -> None:
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
    
class Menu:
    def __init__(self, items : list) -> None:
        self.items = items
    
    def get_items(self) -> str:
        return "/".join([item.name for item in self.items])
    
    def find_drink(self, order_name : str) -> MenuItem:
        if self.items.count(order_name):
            return self.items.index(order_name)
        return None
    
class CoffeeMaker:
    def __init__(self, resources : dict) -> None:
        self.resources = resources

    def report(self) -> None:
        print(f'Water: {self.resources['water']}ml')
        print(f'Milk: {self.resources['milk']}ml')
        print(f'Coffee: {self.resources['coffee']}g')
    
    def is_resource_sufficient(self, drink : MenuItem) -> bool:
        drink_ingredients = drink.ingredients
        for key, value in drink_ingredients.items():
            if value > self.resources[key]:
                print(f'Sorry there is not enough {key}')
                return False
        return True
    
    def make_coffee(self, order : MenuItem) -> None:
        drink_ingredients = order.ingredients
        for key, value in drink_ingredients.items():
            self.resources[key] -= value
        print(f'Here is your {order.name}!')

class MoneyMachine:
    def __init__(self, money : float = 0.0) -> None:
        self.money = money
    
    def report(self):
        print(f'Money: ${self.money:.2f}')

    def get_coins(self) -> dict:
        coins = {
            'quarters': Utility.get_integer('Quarters: '),
            'dimes': Utility.get_integer('Dimes: '),
            'nickles': Utility.get_integer('Nickles: '),
            'pennies': Utility.get_integer('Pennies: ')
        } 

        parser = {
            'quarters': 0.25,
            'dimes': 0.10,
            'nickles': 0.05,
            'pennies': 0.01
        }
        money = 0
        for key, value in coins.items():
            money += (parser[key] * value)
        return money

    def make_payment(self, cost: float, total_coins: float) -> bool:
        if total_coins == cost:
            self.money += total_coins
            return True
        elif total_coins > cost:
            difference = total_coins - cost
            self.money += cost
            print(f'Here is your change ${difference:.2f}')
            return True
        else:
            print('Not enough money.')
            return False

class Utility:
    @staticmethod
    def get_integer(prompt: str) -> int:
        user_input = input(prompt)
        while not user_input.isdigit():
            user_input = input(prompt)
        return int(user_input)


def main():
    espresso = MenuItem('espresso', 1.5, {'water': 50, 'milk': 0, 'coffee': 10})
    latte = MenuItem('latte', 3.0, {'water': 100, 'milk': 150, 'coffee': 3})
    cappucino = MenuItem('cappucino', 2.25, {'water': 125, 'milk': 100, 'coffee': 6})
    menu = Menu([espresso, latte, cappucino])
    coffeMaker = CoffeeMaker({
        'water': 500,
        'milk': 300,
        'coffee': 175
    })
    moneyMachine = MoneyMachine()

    off = False
    while not off:
        choice = input(f'What would you like? {menu.get_items()}: ')
        off = choice == 'off'

        match choice:
            case 'report':
                coffeMaker.report()
                moneyMachine.report()
            case espresso.name:
                if coffeMaker.is_resource_sufficient(espresso) and moneyMachine.make_payment(espresso.cost, moneyMachine.get_coins()):
                    coffeMaker.make_coffee(espresso)
            case cappucino.name:
                if coffeMaker.is_resource_sufficient(cappucino) and moneyMachine.make_payment(cappucino.cost, moneyMachine.get_coins()):
                    coffeMaker.make_coffee(cappucino)
            case latte.name:
                if coffeMaker.is_resource_sufficient(latte) and moneyMachine.make_payment(latte.cost, moneyMachine.get_coins()):
                    coffeMaker.make_coffee(latte)


if __name__ == '__main__':
    main()