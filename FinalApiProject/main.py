import requests
import json
import pytest

@pytest.fixture
def api_keys():
    return {
        "api_key1": "1d838399-19c4-4e18-92f9-b9208cc5b4ce",
        "api_key2": "954c791f-8d50-4cfc-8827-7eeae0a2d36c"
    }

@pytest.fixture
def base_urls():
    return {
        "search_maps": "https://search-maps.yandex.ru/v1/",
        "geocode_maps": "https://geocode-maps.yandex.ru/1.x/"
    }

# Тест поиска организаций
def test_search(api_keys, base_urls):
    url = base_urls["search_maps"]
    params = {
        "apikey": api_keys["api_key2"],
        "text": "аптека",
        "lang": "ru_RU",
        "ll": "30.360909,59.931058",
        "spn": "0.01,0.01",
        "type": "biz",
        "results": 3
    }
    response = requests.get(url, params=params)
    assert response.status_code == 200
    response_data = response.json()
    print("Ответ: ")
    print(response_data)


# Тест поиска по геокоду
def test_geocode(api_keys, base_urls):
    url = base_urls["geocode_maps"]
    params = {
        "apikey": api_keys["api_key1"],
        "geocode": "Омск,+улица+Панфилова,+дом+10",
        "format": "json"
    }
    response = requests.get(url, params=params)
    assert response.status_code == 200
    response_data = response.json()
    print("Ответ: ")
    print(response_data)



# Тест пустого геокода
def test_empty_geocode(api_keys, base_urls):
    url = base_urls["geocode_maps"]
    params = {
        "apikey": api_keys["api_key1"],
        "geocode": "",
        "format": "json"
    }
    response = requests.get(url, params=params)
    assert response.status_code in [400, 404]
    response_data = response.json()
    print("Ответ: ")
    print(response_data)




