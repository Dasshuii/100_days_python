def encode(shift, plain_text):
    encoded_text = ''
    for letter in plain_text:
        encoded_letter = (ord(letter) - 97 + shift) % 26 + 97
        encoded_text += chr(encoded_letter)
    return encoded_text

def decode(shift, encoded_text):
    decoded_text = ''
    for letter in encoded_text:
        decoded_letter = (ord(letter) - 97 - shift) % 26 + 97
        decoded_text += chr(decoded_letter)
    return decoded_text

def main():
    opt = 'yes'
    while(opt == 'yes'):
        choice = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').strip().lower()
        if choice == 'encode':
            plain_text = input('Type your message:\n')
            shift = int(input('Type the shift number:\n'))
            encoded_text = encode(shift, plain_text)
            print(f'Here\'s the encoded result: {encoded_text}')
            opt = input('Type \'yes\' if you want to go again. Otherwise type \'no\':\n')
        else:
            encoded_text = input('Type your message:\n')
            shift = int(input('Type the shift number:\n'))
            decoded_text = decode(shift, encoded_text)
            print(f'Here\'s the encoded result: {decoded_text}')
            opt = input('Type \'yes\' if you want to go again. Otherwise type \'no\':\n')

if __name__ == '__main__':
    main()