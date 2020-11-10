from PO.StuffForMarket import MarketSearch as market_search
import pytest
from selenium import webdriver


class Test_1_Search:
    baseUrl = "https://market.yandex.ru/"
    text = "Веники"



    def test_search_and_compare(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.baseUrl)
        etalon = 100500
        self.sc1 = market_search(self.driver)
        sc = self.sc1
        self.driver.implicitly_wait(5)
        sc.search_veniks(self.text)
        sc.make_list_view()
        sc.more_veniks()
        prices = sc.take_prices_of_veniks()
        max_price, min_price = sc.find_goods_with_max_min_price(prices)

        self.driver.close()

        assert max_price < etalon
        assert min_price < etalon
        assert min_price < max_price





