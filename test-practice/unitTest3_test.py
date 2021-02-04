# 1
import random
from unittest.mock import  Mock

def get_random_number():
    return random.randint(1, 10)

def add_number_with_random_number(a, get_random_number):
    return a + get_random_number()

def test_add_number_with_random_number():
    a = 5
    mock_get_random_number = Mock()
    mock_get_random_number.return_value = 5
    expected = 10

    actual = add_number_with_random_number(a, mock_get_random_number)

    assert actual == expected


#2
from random import randint
from unittest.mock import  Mock

def get_random_number(randint):
    return randint(1, 10)

def test_get_random_number():
    mock_randint = Mock()
    mock_randint.return_value = 5
    expected = 5

    actual = get_random_number(mock_randint)

    assert actual == expected


# 3
from unittest.mock import patch

def get_user_details():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))

    print(f'Thank you, your name is {name} and your age is {age}')

@patch("builtins.input", side_effect = ['Andy', 27])
@patch("builtins.print")
def test_get_user_details(mock_print, mock_input):
    get_user_details()

    mock_print.assert_called_with("Thank you, your name is Andy and your age is 27")
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1