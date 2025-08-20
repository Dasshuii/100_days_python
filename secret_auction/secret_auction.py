import os

LOGO = '\U0001F528'

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_name(prompt):
    user_input = input(prompt)
    while not user_input:
        user_input = input(prompt)
    return user_input.strip()

def get_bid(prompt):
    user_input = input(prompt)
    while not user_input or not user_input.isdigit():
        user_input = input(prompt)
    return int(user_input.strip())

def other_bidders():
    options = ['yes', 'no']
    prompt = f'Are there other bidders? Type \'{options[0]}\' or \'{options[1]}\'? '
    user_input = input(prompt).strip().lower()
    while not user_input or user_input not in options:
        user_input = input(prompt).strip().lower()
    return True if user_input == 'yes' else False

def get_bidder():
    name = get_name('What is your name? ')
    bid = get_bid('What is your bid? $')
    return {name : bid}

def get_winner(bidders):
    key_list = list(bidders.keys())
    max = key_list[0]
    for key in bidders:
        if bidders[key] > bidders[max]:
            max = key
    return (max, bidders[max])

def main():
    print(LOGO)
    bidders = {}
    bidders.update(get_bidder())
    while other_bidders():
        clear_console()
        bidders.update(get_bidder())
    winner_name, winner_bid = get_winner(bidders)
    print(f'The winner is {winner_name} with a bid of ${winner_bid}')


if __name__ == '__main__':
    main()