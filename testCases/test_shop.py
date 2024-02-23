from pageObjects.ShopPage import ShopPage
from utilities.customLogger import Logger


class TestShop:
    logger = Logger.loggen()

    def test_shop(self, openBrowser):
        self.logger.info("***Start***")
        self.driver = openBrowser
        self.shop = ShopPage(self.driver)
        self.shop.inputSearchText("Camera")
        self.shop.clickSearch()
        product = self.shop.getPageHeading()
        print(product)
        actual_page_heading = "Canon Antique Camera"
        if product == actual_page_heading:
            assert True
            self.logger.info("*** Product name is matched ***")
        else:
            self.driver.save_screenshot("./screenshots/" + "product_search.png")
            self.logger.error("*** Desired product not found ***")
            assert False
        self.shop.addToCart()
        self.shop.addToCartConfirm()
