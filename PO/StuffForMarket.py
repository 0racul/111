from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import re
import time


class MarketSearch:
    input_search_id = "header-search"
    list_maker = '//input[@value="list"]'
    goods_list = '//div[@data-zone-name="snippetList"]'
    list_item_price = '//span[@data-autotest-currency="₽"]/span[1]'
    stuff_price_value = "data-autotest-value"
    more_button = '//button[@class="_1zrxtiGhhX _1e9zvPEa4O"]'
    search_button = '//button[@class="_1XiEJDPVpk"]'


    def __init__(self, driver):
        self.driver = driver

    def search_veniks(self, text):
        self.driver.find_element_by_id(self.input_search_id).send_keys(text)
        self.driver.find_element_by_xpath(self.search_button).click()

    def make_list_view(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.list_maker).click()
        time.sleep(5)

    def take_prices_of_veniks(self):
        prices = []
        numbers = self.driver.find_elements_by_xpath(self.list_item_price)
        for number in numbers:
            prices.append(number.text)

        return prices

    def find_goods_with_max_min_price(self, prices):
        prices_final = []
        for price in prices:
            prices_final.append(int(re.sub(r'[^0-9.]+', r'', price)))

        max_price = max(prices_final)
        min_price = min(prices_final)

        return max_price, min_price

    def more_veniks(self):
        actions = ActionChains(self.driver)
        try:
            while self.driver.find_element_by_xpath(self.more_button).is_displayed():
                actions.move_to_element(self.driver.find_element_by_xpath(self.more_button))
                self.driver.find_element_by_xpath(self.more_button).click()
        except NoSuchElementException:
            return
