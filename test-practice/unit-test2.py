import codeToTest

def test_get_country_code():
    expected = 'AFG'
    actual = codeToTest.get_country_code(codeToTest.mock_get_countries(), 'Afghanistan')
    assert expected == actual

test_get_country_code()


def test_get_country_currency():
    expected = 'AFN'
    actual = codeToTest.get_country_currency(codeToTest.mock_get_countries(), 'Afghanistan')
    assert expected == actual

test_get_country_currency()


def test_transform():
    expected = {'name': 'Afghanistan', 'country_code': 'AFG', 'currency_code': 'AFN'}
    actual = codeToTest.transform('Afghanistan')
    assert expected == actual

test_transform()


def test_show_country_info():
    expected = {'name': 'Afghanistan', 'country_code': 'AFG', 'currency_code': 'AFN'}
    actual = codeToTest.show_country_info()
    assert expected == actual

test_show_country_info()
