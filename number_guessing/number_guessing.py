import random

ATTEMPTS = {
    'easy' : 10,
    'hard' : 5,
}

def get_attempts():
    user_input = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    while user_input not in ATTEMPTS.keys():
        user_input = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    return ATTEMPTS[user_input]

def welcome():
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')

def get_random_number(min, max):
    return random.randint(min, max)

def get_guess():
    user_input = input('Make a guess: ')
    while not user_input.isdigit():
        user_input = input('Make a guess: ')
    return int(user_input)

def check_guessed(guess, number):
    return guess == number

def main():
    attempts = get_attempts()
    number = get_random_number(0, 100)
    guessed = False

    while not guessed and attempts:
        print(f'You have {attempts} remaining to guess the number.')
        guess = get_guess()
        guessed = check_guessed(guess, number)
        print('Too high' if guess > number else ('Guessed!' if guessed else 'Too low!'))
        attempts -= 1


if __name__ == '__main__':
    main()