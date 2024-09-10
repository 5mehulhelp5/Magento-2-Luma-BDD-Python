import time

from help_selectors.shoppingCartSelectors import *
from pages.base_page import BasePage


class ShoppingCart(BasePage):

    def store_product_name(self):
        self.store_product_info(SELECTED_PRODUCT_NAME_SELECTOR)

    def chose_size(self):
        self.wait_for_element(PRODUCT_FIRST_SIZE_SELECTOR, 5).click()

    def chose_color(self):
        self.wait_for_element(PRODUCT_FIRST_COLOR_SELECTOR, 56).click()

    def chose_quantity(self, value):
        self.type(QUANTITY_SELECTOR, value)

    def add_product_to_cart(self):
        self.wait_for_element(ADD_TO_CART_SELECTOR, 5).click()

    def verify_cart_page_url(self):
        time.sleep(5)
        return self.driver.current_url

    def restore_product_name(self):
        self.store_product_info(CART_PRODUCT_NAME_SELECTOR)

    def verify_if_product_is_the_same(self):
        if self.store_product_name() == self.restore_product_name():
            return 'The product is the same'
        else:
            return 'The product is different'

    def remove_items(self):
        self.action_chain(CART_SELECTOR)
        time.sleep(1)
        self.action_chain(SEE_DETAILS_SELECTOR)
        self.action_chain(REMOVE_ITEM_FROM_CART_SELECTOR)
        self.wait_for_element(REMOVE_ITEM_BUTTON_SELECTOR).click()
        time.sleep(1)
