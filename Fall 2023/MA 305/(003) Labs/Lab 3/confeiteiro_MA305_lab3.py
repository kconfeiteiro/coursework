# -*- coding: utf-8 -*-
"""
Krystian Confeiteiro
Dr. Sam
MA 305 - 06DB
Lab 3
10/16/2023
"""

# define function to convert the list of strings into a list of integers
int_list = lambda _list: list(map(lambda x: int(x), _list))


# define function to prepare the credit card number (Step 1)
def _prep_data(cardnum: str = None):
    cardnum = cardnum.replace(" ", "")
    cardnum = int_list([*cardnum])
    return cardnum[::-1]


# define function to sum the digits of two-digit number
def _sum(number: int = None):
    return int(sum(int_list(str(number))))


# define function to validate the list of numbers
def _test(num_list: list = None):
    return True if sum(num_list) % 10 == 0 else False


# define function to combine all steps into a single function
def validate_card(card_number: str = None):
    prepped_data = _prep_data(card_number)
    for i in range(1, len(prepped_data), 2):
        _num = 2 * prepped_data[i]
        if _num > 9:
            prepped_data[i] = _sum(_num)
        else:
            prepped_data[i] = _num

    _msg = f"| FOR CARD: '{card_number}' |"
    _dashes = "-" * len(_msg)
    is_real = _test(prepped_data)

    print(f"{_dashes}\n{_msg}\n{_dashes}")
    print("IS VALID:", is_real, "\n")


# define card number input
card = input("Input card number: ")

# complete step 3 and 4 then print final outcome
validate_card(card)
