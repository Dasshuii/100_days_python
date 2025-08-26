import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACKJACK = 21

def get_starting_hand():
    '''
        Returns the starting hand of the game
    '''
    card1 = get_random_card()
    card2 = get_random_card()
    while card1 + card2 > BLACKJACK:
        card2 = get_random_card()
    return [card1, card2]

def get_random_card():
    '''
        Returns a random card from the array
    '''
    return random.choice(CARDS)

def get_winner(player_hand, computer_hand):
    '''
        Calculates and return the winner
    '''
    player_hand_score = get_hand_score(player_hand)
    computer_hand_score = get_hand_score(computer_hand)
    return 'You win' if player_hand_score > computer_hand_score else ('Draw!' if computer_hand_score == player_hand_score else 'You lose')

def get_hand_score(hand):
    '''
        Calculates hand score
    '''
    return sum(hand)

def eliminate(hand):
    '''
        Check if hand's score exceed 21
    '''
    return True if get_hand_score(hand) > BLACKJACK else False
   
def main():
    player_hand_score = 0
    computer_hand_score = 0
    choice = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')

    




if __name__ == '__main__':
    main()