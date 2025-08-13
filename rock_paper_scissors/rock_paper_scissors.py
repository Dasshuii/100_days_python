import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def main():
    options = [ROCK, PAPER, SCISSORS]
    choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n')
    choice = options[int(choice)]
    computer_choice = random.choice(options)
    print(f'You choose:\n{choice}')
    print(f'Computer\'s choose:\n{computer_choice}')
    check_winner(choice, computer_choice)

    
def check_winner(user_choice, computer_choice):
    if (user_choice == ROCK and computer_choice == SCISSORS) and (user_choice == PAPER and computer_choice == ROCK) and (user_choice == SCISSORS and computer_choice == PAPER):
        print('User wins!')
    elif user_choice == computer_choice:
        print('Tie!')
    else:
        print('Computer wins!')


if __name__ == '__main__':
    main()