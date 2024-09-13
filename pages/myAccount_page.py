import time

from help_selectors.myAccountSelectors import *
from pages.base_page import BasePage


class MyAccount(BasePage):

    def access_account_menu(self):
        self.action_chain(MY_ACCOUNT_MENU_SELECTOR)

    def click_account_button(self):
        self.click(MY_ACCOUNT_BUTTON_SELECTOR)

    def access_edit_shipping_address(self):
        self.click(EDIT_SHIPPING_ADDRESS_SELECTOR)

    def street_input(self, street):
        self.type(SHIPPING_STREET_SELECTOR, street)

    def country_select(self, country):
        self.select_from_dropdown(SHIPPING_COUNTRY_SELECTOR, country)

    def region_select(self, region):
        self.select_from_dropdown(SHIPPING_REGION_SELECTOR, region)

    def phone_input(self, phone):
        self.type(SHIPPING_PHONE_NUMBER_SELECTOR, phone)

    def city_input(self, city):
        self.type(SHIPPING_CITY_SELECTOR, city)

    def zip_code_input(self, zip_code):
        self.type(SHIPPING_ZIP_CODE_SELECTOR, zip_code)

    def click_save_button(self):
        self.click(SHIPPING_SAVE_ADDRESS_SELECTOR)

    def get_save_address_message(self):
        time.sleep(1)
        return self.wait_for_element(SHIPPING_SAVE_ADDRESS_MESSAGE_SELECTOR, 5).text
