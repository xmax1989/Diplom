import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Classes.classes import module


@allure.title("ПЕРЕКРЕСТОК")
@allure.description("Тест заходит на сайт переходит на вкладку все магазины,\
                    заходит на страницу магазина перекресток\
                    и проверяет название магазина")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_delivery_perekrestok():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим на сайт"):
        send.input_main()
    with allure.step("нажимаем на кнопку все магазины"):
        send.click_vse()
    with allure.step("переходим на страницу магазина перекресток"):
        send.click_perekr()
    with allure.step("находим заголовок магазина"):
        res = send.header_perekr()
        assert res == "Перекрёсток"
    browser.quit()


@allure.title("ПОДДЕРЖКА")
@allure.description("Тест заходит на сайт нажимает на кнопку поддержки,\
                    и проверяет открытие окна")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_delivery_support():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим на сайт"):
        send.input_main()
    with allure.step("нажимаем на кнопку поддержка"):
        send.click_support()
    with allure.step("находим заголовок окна поддержка"):
        result = send.header_support()
        with allure.step("проверяем заголовок окна"):
            assert result == "Служба поддержки"
    browser.quit()


@allure.title("ВОЗВРАЩЕНИЕ НА ГЛАВНУЮ")
@allure.description("Проверяем возможность вернуться на главную страницу\
                    нажатием на лого в заголовке страници из магазина'")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_delivery_return_main():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим в магазин пятерочка"):
        send.input_pyaterka()
    with allure.step("нажимаем на 'лого' вернуться на главную"):
        result = send.click_logo()
        with allure.step("проверяем наличие блока 'main' на главной странице"):
            assert result == "main"
    browser.quit()


@allure.description("тест поля поиск товаров")
@allure.title("ПОИСК")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_search_input():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим на сайт"):
        send.input_main()
    with allure.step("вводим текст в поле поиск"):
        text = "молоко"
        result = send.search_text(text)
        assert result == text
    browser.quit()


@allure.description("Тест блока рестораны")
@allure.title("РЕСТОРАНЫ")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_restarants():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим на сайт"):
        send.input_main()
    with allure.step("нажать на кнопку бургеры"):
        send.click_burgers()
        with allure.step("проверяем переход в блок рестораны"):
            result = send.in_restarants()
            assert result == "Фильтры"
    with allure.step("переход на страницу бургер кинг"):
        send.click_b_king()
        with allure.step("проверяем вход на страницу ресторана"):
            result = send.in_burg_king()
            assert result == "Burger King"
    browser.quit()


@allure.title("Пятёрочка")
@allure.description("Проверяем страницы магазинов переходя по прямой ссылке")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_del_pyaterka():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим в магазин пятерочка"):
        result = send.input_pyaterka()
        with allure.step("проверяем переход на страницу магазина"):
            assert result == "Пятёрочка"
    browser.quit()


@allure.title("Магнит")
@allure.description("Проверяем страницы магазинов переходя по прямой ссылке")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_del_magnit():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим в магазин Магнит"):
        result = send.input_magnit()
        with allure.step("проверяем переход на страницу магазина"):
            assert result == "Магнит"
    browser.quit()


@allure.title("РИВ ГОШ")
@allure.description("Проверяем страницы магазинов переходя по прямой ссылке")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_del_rivgosh():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим в магазин РИВ ГОШ"):
        result = send.input_rivgosh()
        with allure.step("проверяем переход на страницу магазина"):
            assert result == "РИВ ГОШ"
    browser.quit()


@allure.title("Fix Price")
@allure.description("Проверяем страницы магазинов переходя по прямой ссылке")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_del_fixprice():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим в магазин Fix Price"):
        result = send.input_fixprice()
        with allure.step("проверяем переход на страницу магазина"):
            assert result == "Fix Price"
    browser.quit()


@allure.title("Pet shop")
@allure.description("Проверяем страницы магазинов переходя по прямой ссылке")
@pytest.mark.test_ui
@pytest.mark.test_positive
def test_del_petshop():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    send = module(browser)
    with allure.step("заходим в магазин Pet shop"):
        result = send.input_petshop()
        with allure.step("проверяем переход на страницу магазина"):
            assert result == "Petshopru"
    browser.quit()
