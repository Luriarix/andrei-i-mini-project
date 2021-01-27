def add_two_numbers(a, b):
    try:
        return a + b
    except TypeError:
        return TypeError


# adds two whole numbers
def test_adds_two_numbers():
    a = 5
    b = 2
    expected = 7

    result = add_two_numbers(a, b)

    assert result == expected 

test_adds_two_numbers()


# adds a positive whole number to a negative whole number
def test_adds_positive_and_negative_numbers():
    a = 7
    b = -12
    expected = -5

    result = add_two_numbers(a, b)

    assert result == expected 

test_adds_two_numbers()


# adds two floating point numbers
def test_adds_two_floating_point_numbers():
    a = 7.5
    b = 2.25
    expected = 9.75

    result = add_two_numbers(a, b)

    assert result == expected 

test_adds_two_numbers()


# adds a string to a whole number
def test_adds_a_string_to_a_number():
    a = "maybe"
    b = 5
    expected = TypeError

    result = add_two_numbers(a, b)

    assert result == expected 

test_adds_two_numbers()


# adds two strings
def test_adds_two_strings():
    a = "call me"
    b = ", maybe"
    expected = "call me, maybe"

    result = add_two_numbers(a, b)

    assert result == expected 

test_adds_two_numbers()