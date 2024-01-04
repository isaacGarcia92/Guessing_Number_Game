import random
from enum import Enum


class YesOrNo(Enum):
    YES = 1
    NO = 0


def generate_random_num():
    rand_num = random.randint(1, 9)
    return rand_num


def input_is_number(string):
    try:
        return int(string)
    except ValueError:
        return None


def validate_num_input():
    while True:
        user_input = input('Enter a number: ')
        parsed_int = input_is_number(user_input)

        if parsed_int is None:
            print('Invalid Input!')
        else:
            return parsed_int


def start_game():
    rand_num = generate_random_num()
    guesses = 0

    while True:
        user_num = validate_num_input()

        if user_num == rand_num:
            guesses += 1
            print(f'Congratulations! You have guessed the number in {guesses} guesses')
            break
        elif user_num > rand_num:
            guesses += 1
            print('Number is too high!')
        else:
            guesses += 1
            print('Number is too low!')


def ask_to_continue():
    while True:
        user_option = input('Do you want to continue playing? Please write yes or no: ').upper()

        if user_option.isalpha():
            if user_option == YesOrNo(1).name:
                start_game()
            elif user_option == YesOrNo(0).name:
                return print('Thanks for playing!')
            else:
                print('Please write the correct option')
        else:
            print('Invalid Option!')


def main():
    start_game()
    ask_to_continue()


if __name__ == '__main__':
    main()
