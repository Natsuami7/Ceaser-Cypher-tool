# Ceaser Cypher Tool

'''
Title : Ceaser Cypher Tool
Author : Chaitanya Shah
Class : CYSE1002
Date : October 2024

Description :
This is a ceaser cypher tool which is used to encode and decode the text provided by the user.
The user will have choice 1. Encode , 2. Decode  and 3. Bruteforce (which is decoding without knowing the key)
This is a simple cryptography tool to encode messages by providing shift key provided by user and same for decoding.
'''



import string


def encode(text, shift):
    '''

    Encodes a given text using a Caesar cipher with a specified shift.

    :param text: str
        The input string to be encoded. It can contain alphabetic characters (both upper and lower case)
        as well as non-alphabetic characters, which will remain unchanged.
    :param shift: int
        The number of positions each alphabetic character is shifted. A positive shift moves characters
        to the right (forward in the alphabet), while a negative shift moves them to the left.

    :return: str
        The encoded string, where each alphabetic character is shifted by the specified amount.
        Non-alphabetic characters remain unchanged.

    Description:
    This function implements a Caesar cipher, shifting each letter in the input `text` by the specified
    `shift` value. The shift wraps around the alphabet (e.g., with a shift of 1, 'z' becomes 'a').
    The case of each letter is preserved, and non-alphabetic characters are not affected.

    '''

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
    '''

     Decodes a given text that was encoded using a Caesar cipher with a specified shift.

    :param text: str
        The encoded string that needs to be decoded.
    :param shift: int
        The number of positions each alphabetic character was shifted during encoding.

    :return: str
        The decoded string, where each alphabetic character is shifted back by the specified amount.
        Non-alphabetic characters will remain unchanged.

    Description:
    This function reverses the Caesar cipher encoding process by using the `encode` function with the
    negative of the specified `shift` value, effectively shifting each character back to its original position.
    '''

    return encode(text, -shift)


def brute_force(text):
    '''
     Attempts to decode a Caesar cipher encoded text by trying all possible shift values.

    :param text: str
        The encoded string that needs to be decoded. It may contain alphabetic characters (both upper and lower case)
        as well as non-alphabetic characters, which will remain unchanged.

    :return: None
        This function does not return a value. It prints the decoded output for each shift value from 1 to 26.

    Description:
    This function iterates through all possible shift values (1 to 26) to decode the given `text` using a
    Caesar cipher. It calls the `decode` function with each shift value and prints the resulting decoded text,
    allowing the user to manually inspect each result and find the correct shift.
    '''

    for shift in range(1,27):
        print(f'Shift {shift}: {decode(text,shift)}')


def get_text():
    '''
    Prompts the user to input a string and returns the entered text.

    :return: str
        The text entered by the user as a string.

    Description:
    This function uses the `input` function to prompt the user with the message 'Enter your text : '.
    It captures the user's input and returns it as a string.
    '''

    return input('Enter your text : ')


def get_shift():
    '''
    Prompts the user to input a shift key for a Caesar cipher and validates the input.

    :return: int
        The shift key entered by the user, which is an integer between 1 and 25.

    Description:
    This function continuously prompts the user to enter a shift key until a valid input is provided.
    It checks if the input is an integer and within the specified range (1-25).
    If the input is not valid, it displays an appropriate error message and prompts again.
    Once a valid input is received, it returns the shift value.
    '''

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
                brute_force(text)
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
