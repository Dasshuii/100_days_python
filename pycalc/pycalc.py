OPERATIONS = ['+', '-', '*', '/']

def get_valid_input(prompt):
    user_input = input(prompt)
    while not user_input:
        user_input = input(prompt)
    return user_input.strip()

def get_number(prompt):
    number = get_valid_input(prompt)
    while not number.isnumeric:
        number = get_valid_input(prompt)
    return float(number)

def get_operation():
    prompt = '\n'.join(OPERATIONS) + '\nPick an operation: '
    operation = get_valid_input(prompt)
    while operation not in OPERATIONS:
        operation = get_valid_input(prompt)
    return operation

def get_result(operation, first_number, second_number):
    match operation:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number
        case '/':
            return first_number / second_number

def main():
    while True:
        first_number = get_number('What\'s the first number?: ')
        operation = get_operation()
        second_number = get_number('What\'s the next number?: ')
        result = get_result(operation, first_number, second_number)
        print(f'{first_number} {operation} {second_number} = {result}')
        choice = get_valid_input(f'Type \'y\' to continue with {result}, or type \'n\' to start a new calculation: ')
        
        while choice == 'y':
            first_number = result
            second_number = get_number('What\'s the next number?: ')
            operation = get_operation()
            result = get_result(operation, first_number, second_number)
            print(f'{first_number} {operation} {second_number} = {result}')
            choice = get_valid_input(f'Type \'y\' to continue with {result}, or type \'n\' to start a new calculation: ')

if __name__ == '__main__':
    main()