# 1
def add_two_numbers(a, b):
    return a + b

def test_add_two_numbers():
    a = 5
    b = 5
    expected = 10

    result = add_two_numbers(a, b)

    assert result == expected 

test_add_two_numbers()


# 2
import random

def get_random_number():
    return random.randint(1, 10)

def add_number_with_random_number(a, get_random_number):
    return a + get_random_number()

def mock_get_random_number():
    return 3

def test_add_number_with_random_number():
    a = 5
    expected = 8

    result = add_number_with_random_number(a, mock_get_random_number)

    print(result)
    assert result == expected 

test_add_number_with_random_number()


# 3
from random import randint

def get_random_number():
    return randint(1, 10)

def add_two_random_numbers(get_random_number):
    return get_random_number() + get_random_number()

def mock_get_random_number():
    return 3

def test_add_two_random_numbers():
    expected = 6

    result = add_two_random_numbers(mock_get_random_number)

    assert result == expected 

test_add_two_random_numbers()



# 4
from random import randint

def get_random_number(randint):
    return randint(1, 10)

def mock_randint(a, b):
    return 3

def test_get_random_number():
    expected = 3

    result = get_random_number(mock_randint)

    print(f'result: {result} == expected: {expected}')

    assert result == expected

test_get_random_number()