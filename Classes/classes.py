import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class module:

    def __init__(self, browser):
        self.driver = browser
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def input_main(self):
        self.driver.get("https://market-delivery.yandex.ru")

    def input_pyaterka(self):
        self.driver.get(
            "https://market-delivery.yandex.ru/retail/paterocka")
        magaz = self.driver.find_element(By.CSS_SELECTOR,
                                         "a[href='/retail/paterocka']")
        result = magaz.get_attribute("aria-label")
        return result

    def input_magnit(self):
        self.driver.get(
            "https://market-delivery.yandex.ru/retail/magnit_celevaya")
        magaz = self.driver.find_element(By.CSS_SELECTOR,
                                         "a[href='/retail/magnit_celevaya']")
        result = magaz.get_attribute("aria-label")
        return result

    def input_rivgosh(self):
        self.driver.get(
            "https://market-delivery.yandex.ru/retail/riv_gos")
        magaz = self.driver.find_element(By.CSS_SELECTOR,
                                         "a[href='/retail/riv_gos']")
        result = magaz.get_attribute("aria-label")
        return result

    def input_fixprice(self):
        self.driver.get(
            "https://market-delivery.yandex.ru/retail/fix_price")
        magaz = self.driver.find_element(By.CSS_SELECTOR,
                                         "a[href='/retail/fix_price']")
        result = magaz.get_attribute("aria-label")
        return result

    def input_petshop(self):
        self.driver.get(
            "https://market-delivery.yandex.ru/retail/petshopru")
        magaz = self.driver.find_element(By.CSS_SELECTOR,
                                         "a[href='/retail/petshopru']")
        result = magaz.get_attribute("aria-label")
        return result

    def click_vse(self):

        wait = WebDriverWait(self.driver, 10)
        button_vse = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR,
             "button[class='UiKitButton_root UiKitButton_size-xs UiKitButton_variant-default UiKitButton_shape-rounded']"
             )))
        button_vse.click()

    def click_perekr(self):

        wait = WebDriverWait(self.driver, 10)
        try:
            menu_mag = wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR,
                     "a[href='/retail/perekrestok?placeSlug=perekrestok_dmqpx']"
                     )))
            menu_mag.click()

        except:

            self.driver.refresh()
            self.driver.get("https://market-delivery.yandex.ru/retail/perekrestok")

    def header_perekr(self):

        magaz = self.driver.find_element(By.CSS_SELECTOR,
                                         "a[href='/retail/perekrestok']")
        result = magaz.get_attribute("aria-label")
        return result

    def click_support(self):

        wait = WebDriverWait(self.driver, 10)
        support = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[title='Служба поддержки']")))
        support.click()

    def header_support(self):

        wind = self.driver.find_element(By.CSS_SELECTOR,
                                        "div[class='SupportChatProvider_chat SupportChatProvider_chatActive']"
                                        )
        res = wind.find_element(By.CSS_SELECTOR, "iframe")
        result = res.get_attribute("title")
        return result

    def click_logo(self):
        wait = WebDriverWait(self.driver, 10)
        logo = wait.until(
             EC.visibility_of_element_located((By.CSS_SELECTOR,
                                               "a[class='UiKitRetailHeader_eatsLogo']")))
        logo.click()

        hed_menu = self.driver.find_element(By.CSS_SELECTOR,
                                            "main[class='AppDefaultLayout_container']")
        result = hed_menu.get_attribute("id")
        return result

    def search_text(self, text):
        wait = WebDriverWait(self.driver, 10)
        input = self.driver.find_element(By.TAG_NAME, "input")
        input_text = wait.until(EC.element_to_be_clickable((input)))
        input_text.clear()
        input_text.send_keys(text, Keys.ENTER)

        with allure.step("проверяем результат поиска"):

            try:
                wait.until(EC.visibility_of_element_located(
                     (By.CSS_SELECTOR, "[class='DesktopSearchPage_headerBlock']")))
                result = self.driver.find_element(By.TAG_NAME,
                                                  "input").get_attribute("value")
                return result
            except:
                self.driver.refresh()
                re_input = self.driver.find_element(By.TAG_NAME, "input")
                re_input_text = wait.until(EC.element_to_be_clickable((re_input)))
                re_input_text.clear()
                re_input_text.send_keys(text, Keys.ENTER)

                wait.until(EC.visibility_of_element_located(
                     (By.CSS_SELECTOR, "[class='DesktopSearchPage_headerBlock']")))
                result = self.driver.find_element(By.TAG_NAME,
                                                  "input").get_attribute("value")
                return result

    def click_burgers(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "a[aria-label='Бургеры']")))
            button.click()
        except:
            self.driver.refresh()
            self.driver.get(
                "https://market-delivery.yandex.ru/Velikiy-Novgorod?quickfilter=burger&shippingType=delivery"
                )

    def in_restarants(self):
        result = self.driver.find_element(By.CSS_SELECTOR,
                                          "h3[class='VisuallyHidden_root']").text
        return result

    def click_b_king(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            image = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "h3[title='Доставка из Burger King']")))
            image.click()
        except:
            self.driver.refresh()
            self.driver.get("https://market-delivery.yandex.ru/r/burger_king_ynrku")

    def in_burg_king(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            res = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "h1[class='RestaurantHeader_name UiKitText_root UiKitText_HeaderLoose UiKitText_Bold UiKitText_Text']"
                 )))
        except:
            self.driver.refresh()
            self.driver.get("https://market-delivery.yandex.ru/r/burger_king_ynrku")
            res = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "h1[class='RestaurantHeader_name UiKitText_root UiKitText_HeaderLoose UiKitText_Bold UiKitText_Text']"
                 )))
        result = res.text
        return result
