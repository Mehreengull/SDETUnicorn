import time

from selenium.webdriver.common.by import By


class ShopPage:
    search_id = "woocommerce-product-search-field-0"
    search_cta_xpath = "//button[normalize-space()='Search']"
    camera_heading_css = ".zak-page-title"
    add_to_cart_xpath = "//button[normalize-space()='Add to cart']"
    add_confirm_link = "View cart"
    add_main_cta_xpath = "//a[@aria-label='Add to cart: “Branded Converse”']"
    view_cart_xpath = "//a[normalize-space()='View cart']"

    def __init__(self, driver):
        self.driver = driver

    def inputSearchText(self, search_input):
        self.driver.find_element(By.ID, self.search_id).send_keys(search_input)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.search_cta_xpath).click()

    def getPageHeading(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.camera_heading_css)
        return element.text

    def addToCart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_xpath).click()

    def addToCartConfirm(self):
        element = self.driver.find_element(By.LINK_TEXT, self.add_confirm_link)
        element.is_displayed()
        element.click()

    def addToCartClick(self):
        self.driver.find_element(By.XPATH, self.add_main_cta_xpath).click()

    def viewCart(self):
        self.driver.find_element(By.XPATH, self.view_cart_xpath).click()
