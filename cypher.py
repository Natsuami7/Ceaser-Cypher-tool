import string


def encode(text, shift):
    alphabet_list = list(string.ascii_lowercase)
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_index = (alphabet_list.index(char) + shift) % 26
            shifted_char = alphabet_list[shifted_index]
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char

    return result


def decode(text, shift):
    return encode(text, -shift)


def brute_force(text):
    for shift in range(1,27):
        print(f'Shift {shift}: {decode(text,shift)}')


def get_text():
    return input('Enter your text : ')


def get_shift():
    while True:
        shift = input('Enter the shift key (1-25) : ')
        try:
            shift = int(shift)
            if 1 <= shift <= 25:
                return shift
            print('Error : Shift should be between 1 and 25')
        except ValueError:
            print('Error : Invalid Input. Please Enter A Number')


while True:
    try:
        action = int(input('What would you like to do \n\t1.Encode \n\t2.Decode \n\t3.Brute-Force \n\t4.Exit \n Enter your Choice : '))
        match action:
            case 1:
                print('..................Encoder....................\n')
                text = get_text()
                shift = get_shift()
                print('\t..................Encoding....................\n')
                print(f'Encoded text : {encode(text,shift)}')
            case 2:
                print('..................Decoder....................\n')
                text = get_text()
                shift = get_shift()
                print('\t..................Decoding....................\n')
                print(f'Decoded Text : {decode(text,shift)}')
            case 3:
                print('..................Bruteforce....................\n')
                text = get_text()
                print('\t..................Doing Bruteforce....................\n')
                print(f'{brute_force(text)}\n')
            case 4:
                print('Exiting..........')
                exit()
            case _:
                print('Invalid Choice. Enter 1,2,3 or 4.')
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print('Thank you for using my ceaser cypher tool. Goodbye !')
