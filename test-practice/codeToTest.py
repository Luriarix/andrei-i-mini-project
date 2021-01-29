import pip._vendor.requests
import json

def get_countries():
    headers = {'Content-Type': 'application/json'}
    api_url = "https://restcountries.eu/rest/v2/all"

    response = pip._vendor.requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def mock_get_countries():
    countries = [
    {
        "name": "Afghanistan",
        "topLevelDomain": [
            ".af"
        ],
        "alpha2Code": "AF",
        "alpha3Code": "AFG",
        "callingCodes": [
            "93"
        ],
        "capital": "Kabul",
        "altSpellings": [
            "AF",
            "Afġānistān"
        ],
        "region": "Asia",
        "subregion": "Southern Asia",
        "population": 27657145,
        "latlng": [
            33.0,
            65.0
        ],
        "demonym": "Afghan",
        "area": 652230.0,
        "gini": 27.8,
        "timezones": [
            "UTC+04:30"
        ],
        "borders": [
            "IRN",
            "PAK",
            "TKM",
            "UZB",
            "TJK",
            "CHN"
        ],
        "nativeName": "افغانستان",
        "numericCode": "004",
        "currencies": [
            {
                "code": "AFN",
                "name": "Afghan afghani",
                "symbol": "؋"
            }
        ],
        "languages": [
            {
                "iso639_1": "ps",
                "iso639_2": "pus",
                "name": "Pashto",
                "nativeName": "پښتو"
            },
            {
                "iso639_1": "uz",
                "iso639_2": "uzb",
                "name": "Uzbek",
                "nativeName": "Oʻzbek"
            },
            {
                "iso639_1": "tk",
                "iso639_2": "tuk",
                "name": "Turkmen",
                "nativeName": "Türkmen"
            }
        ],
        "translations": {
            "de": "Afghanistan",
            "es": "Afganistán",
            "fr": "Afghanistan",
            "ja": "アフガニスタン",
            "it": "Afghanistan",
            "br": "Afeganistão",
            "pt": "Afeganistão",
            "nl": "Afghanistan",
            "hr": "Afganistan",
            "fa": "افغانستان"
        },
        "flag": "https://restcountries.eu/data/afg.svg",
        "regionalBlocs": [
            {
                "acronym": "SAARC",
                "name": "South Asian Association for Regional Cooperation",
                "otherAcronyms": [],
                "otherNames": []
            }
        ],
        "cioc": "AFG"
    },
    {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "topLevelDomain": [
            ".uk"
        ],
        "alpha2Code": "GB",
        "alpha3Code": "GBR",
        "callingCodes": [
            "44"
        ],
        "capital": "London",
        "altSpellings": [
            "GB",
            "UK",
            "Great Britain"
        ],
        "region": "Europe",
        "subregion": "Northern Europe",
        "population": 65110000,
        "latlng": [
            54.0,
            -2.0
        ],
        "demonym": "British",
        "area": 242900.0,
        "gini": 34.0,
        "timezones": [
            "UTC-08:00",
            "UTC-05:00",
            "UTC-04:00",
            "UTC-03:00",
            "UTC-02:00",
            "UTC",
            "UTC+01:00",
            "UTC+02:00",
            "UTC+06:00"
        ],
        "borders": [
            "IRL"
        ],
        "nativeName": "United Kingdom",
        "numericCode": "826",
        "currencies": [
            {
                "code": "GBP",
                "name": "British pound",
                "symbol": "£"
            }
        ],
        "languages": [
            {
                "iso639_1": "en",
                "iso639_2": "eng",
                "name": "English",
                "nativeName": "English"
            }
        ],
        "translations": {
            "de": "Vereinigtes Königreich",
            "es": "Reino Unido",
            "fr": "Royaume-Uni",
            "ja": "イギリス",
            "it": "Regno Unito",
            "br": "Reino Unido",
            "pt": "Reino Unido",
            "nl": "Verenigd Koninkrijk",
            "hr": "Ujedinjeno Kraljevstvo",
            "fa": "بریتانیای کبیر و ایرلند شمالی"
        },
        "flag": "https://restcountries.eu/data/gbr.svg",
        "regionalBlocs": [
            {
                "acronym": "EU",
                "name": "European Union",
                "otherAcronyms": [],
                "otherNames": []
            }
        ],
        "cioc": "GBR"
    }
    ]
    return countries

def get_country_code(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['alpha3Code']
    return None

def get_country_currency(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['currencies'][0]['code']
    return None

def transform(name: str):
    # countries = get_countries()
    countries = mock_get_countries()
    code = get_country_code(countries, name)
    currency = get_country_currency(countries, name)

    return {"name": name, "country_code": code, "currency_code": currency}

def show_country_info():
    idx = 0
    countries = mock_get_countries()

    for country in countries:
        print(idx, country['name'])
        idx += 1

    print()

    # selected_country_idx = int(input("Please choose a country: "))
    name = countries[0]['name']
    result = transform(name)
    print(result)
    return result