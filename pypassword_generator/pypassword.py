import random

ABECEDARY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def main():
    print('Welcome to the PyPassword Generator!')
    letters = int(input('How many letters would you like in your password?\n'))
    symbols = int(input('How many symbols would you like?\n'))
    numbers = int(input('How many numbers would you like?\n'))
    total = letters + symbols + numbers
    password = ''
    base = []

    for _ in range(total):
        if letters:
            base.append(random.choice(ABECEDARY)) 
            letters -= 1
        elif symbols:
            base.append(random.choice(SYMBOLS))
            symbols -= 1
        else:
            base.append(random.choice(NUMBERS))
            numbers -= 1

    for _ in range(len(base)):
        remove_value = random.choice(base)
        base.remove(remove_value)
        password += remove_value
    
    print(f'Your password is: {password}')


if __name__ == '__main__':
    main()