import random
import time

from help_selectors.createAccountSelectors import *
from pages.base_page import BasePage


class CreateAccount(BasePage):

    @staticmethod
    def generate_random_email():
        random_number = random.randint(1, 9999)
        return f'test{random_number}@test.com'

    def click_create_account_menu(self):
        self.wait_for_element(CREATE_ACCOUNT_SELECTOR, 30).click()

    def insert_first_name(self, first_name):
        self.type(FIRST_NAME_SELECTOR, first_name)

    def insert_last_name(self, last_name):
        self.type(LAST_NAME_SELECTOR, last_name)

    def insert_random_email(self):
        self.type(EMAIL_ADDRESS_SELECTOR, self.generate_random_email())

    def insert_email(self, email):
        self.type(EMAIL_ADDRESS_SELECTOR, email)

    def insert_password(self, password):
        self.type(PASSWORD_INPUT_SELECTOR, password)

    def confirm_password(self, password):
        self.type(CONFIRM_PASSWORD_SELECTOR, password)

    def click_create_account_button(self):
        self.click(CREATE_ACCOUNT_BUTTON_SELECTOR)

    def get_invalid_mail_message_text(self):
        return self.get_element_text(ERROR_INVALID_FIELD_SELECTOR)

    def get_invalid_firstname_message_text(self):
        return self.get_element_text(CREATE_FIRST_NAME_INVALID_SELECTOR)

    def get_invalid_lastname_message_text(self):
        return self.get_element_text(CREATE_LAST_NAME_INVALID_SELECTOR)

    def get_short_password_message_text(self):
        return self.get_element_text(CREATE_SHORT_PASSWORD_SELECTOR)

    def get_six_digits_password_message_text(self):
        return self.get_element_text(CREATE_SIX_CHARACTER_PASSWORD_SELECTOR)

    def get_invalid_password_message_text(self):
        return self.get_element_text(CREATE_INVALID_PASSWORD_SELECTOR)

    def get_account_already_created_message_text(self):
        return self.get_element_text(ERROR_CREATE_MESSAGE_SELECTOR)

    def get_message_text(self):
        time.sleep(5)
        return self.get_element_text(WELCOME_MESSAGE_SELECTOR)
