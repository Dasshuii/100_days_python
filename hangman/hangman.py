import random

WORDS = ['apple', 'acid', 'beat', 'begin', 'bird', 'cash', 'choice', 'coffee']

def get_letter_input(prompt):
    letter = input(prompt)
    while len(letter) > 1 or not letter.isalpha():
        letter = input(prompt)
    return letter


def main():
    lives = 5
    word_to_guess = random.choice(WORDS)
    to_guess = ''.join('_' for _ in word_to_guess)
    win = False
    
    letters_used = []

    while (not win and lives and '_' in to_guess):
        print(to_guess)
        print(f'Letters used: {letters_used} | Lives: {lives}')
        letter = get_letter_input('Letter: ')
        if letter in word_to_guess:
            print('Correct!')
            to_guess = to_guess[: word_to_guess.index(letter)] + letter + to_guess[word_to_guess.index(letter) + 1:]
            letters_used += letter
        else:
            print('Incorrect :(')
            lives -= 1
            letters_used += letter
    print(to_guess)


if __name__ == '__main__':
    main()