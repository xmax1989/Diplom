import requests
import pytest
import allure

# базовый URL
base_url = "https://market-delivery.yandex.ru/"
# переменные магазинов
pyaterochka = "pyaterochka_t2jc3"
perekresstok = "perekrestok_dmqpx"
# переменные товаров
chesnok = -13310160054  # чеснок
ogurci = "-525139689"  # Огурцы_фасованные
griby = "-13309503477"  # Шампиньоны_Global_Village
# местополжение
longitude = 31.245475
latitude = 58.540295
# текс в тесте поиска
text = "пельмени"


@allure.title("ГЛАВНАЯ")
@pytest.mark.test_api
@pytest.mark.test_positive
def test_get_main():
    with allure.step("отправляем запрос"):
        resp = requests.get(base_url + "web-api/initial-server-data?lang=ru\
                            &asset=desktop&serviceBrand=dc")
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 200


@allure.title("ИНФО О МАГАЗИНЕ")
@pytest.mark.test_api
@pytest.mark.test_positive
def test_mag_info():
    with allure.step("отправляем запрос"):
        resp = requests.get(base_url, "api/v2/catalog/perekrestok_dmqpx\
                            ?&shippingType=delivery")
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 200


@allure.title("СТРАНИЦА МАГАЗИНА")
@pytest.mark.test_api
@pytest.mark.test_positive
def test_mag_main():
    body = {
        "slug": pyaterochka,
        "latitude": latitude,
        "longitude": longitude,
        "maxDepth": 0
        }
    with allure.step("отправляем запрос"):
        resp = requests.post(base_url +
                             "api/v2/menu/goods?auto_translate=false",
                             json=body)
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 200
    with allure.step("проверяем заголовок ответа"):
        assert resp.headers["Content-Type"] == 'application/json'


@allure.title("КАТАЛОГ ТОВАРОВ")
@pytest.mark.test_api
@pytest.mark.test_positive
def test_mag_catalog():
    body = {
        "slug": pyaterochka,
        "categories":
        [
            {"id": 44008, "min_items_count": 1, "max_items_count": 25},
            {"id": 259964, "min_items_count": 1, "max_items_count": 25},
            {"id": 257642, "min_items_count": 1, "max_items_count": 25},
            {"id": 165, "min_items_count": 1, "max_items_count": 25},
            {"id": 257564, "min_items_count": 1, "max_items_count": 25},
            {"id": 19280, "min_items_count": 1, "max_items_count": 25},
            {"id": 1034, "min_items_count": 1, "max_items_count": 25},
            {"id": 1033, "min_items_count": 1, "max_items_count": 25},
            {"id": 144639, "min_items_count": 1, "max_items_count": 25}
            ]
            }
    with allure.step("отправляем запрос"):
        resp = requests.post(base_url + 'api/v2/menu/goods/get-categories?\
                             auto_translate=false', json=body)
        resp_len = resp.json()
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 200
    with allure.step("проверяем что каталог товаров не пустой"):
        assert len(resp_len) > 0


@allure.title("ДОБАВЛЕНИЕ ТОВАРА В КОРЗИНУ")
@pytest.mark.test_api
@pytest.mark.test_positive
def test_add_item():
    body = {
        "item_id": chesnok,
        "quantity": 1,
        "place_slug": pyaterochka,
        "place_business": "shop"
        }
    with allure.step("отправляем запрос"):
        resp = requests.post(base_url +
                             "api/v1/cart?longitude=31.245475&latitude=58.540295&\
                             screen=menu&shippingType=delivery&autoTranslate=false",
                             json=body)
        resp_body = resp.json()
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 200
    with allure.step("проверяем добавленный товар по id"):
        assert resp_body['item_id'] == chesnok


@allure.title("УДАЛЕНИЕ ТОВАРА")
@pytest.mark.test_api
@pytest.mark.test_positive
def test_del_item():
    with allure.step("отправляем запрос"):
        resp = requests.delete(base_url +
                               "api/v2/cart?longitude=31.245475&latitude=58.540295&\
                               screen=menu&shippingType=delivery&autoTranslate=false")
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 204


@allure.title("ПОИСК ТОВАРА")
@pytest.mark.test_api
@pytest.mark.test_positive
def test_search():
    body = {
        "text": text,
        "filters": [],
        "location":
        {"longitude": longitude,
         "latitude": latitude}
        }
    with allure.step("отправляем запрос"):
        resp = requests.post(base_url + "eats/v1/full-text-search/v1/search",
                             json=body)
        resp_len = resp.json()
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 200
    with allure.step("проверяем что ответ не пустой"):
        assert len(resp_len) > 0


@allure.title("ДОБАВЛЕНИЕ НЕСУЩЕСТВУЮЩЕГО ТОВАРА В КОРЗИНУ")
@pytest.mark.test_api
@pytest.mark.test_negative
def test_neg_item():
    body = {
        "item_id": "-2457",
        "quantity": 1,
        "place_slug": pyaterochka,
        "place_business": "shop"
        }
    with allure.step("отправляем запрос"):
        resp = requests.post(base_url +
                             "api/v1/cart?longitude=31.245475&latitude=58.540295&\
                                screen=menu&shippingType=delivery&\
                                    autoTranslate=false", json=body)
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 400


@allure.title("ПУСТОЙ ПОИСК")
@pytest.mark.test_api
@pytest.mark.test_negative
def test_empty_search():
    body = {
      "text": "",
      "filters": [],
      "location":
      {"longitude": longitude,
       "latitude": latitude}
       }
    with allure.step("отправляем запрос"):
        resp = requests.post(base_url + "eats/v1/full-text-search/v1/search",
                             json=body)
    with allure.step("проверяем статус код ответа"):
        assert resp.status_code == 200
