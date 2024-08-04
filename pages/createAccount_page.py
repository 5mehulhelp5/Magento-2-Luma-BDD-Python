import random
import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CreateAccount(BasePage):
    URL = 'https://osc-ultimate-demo.mageplaza.com/'

    CLOSE_DEMO_NAVIGATION_SELECTOR = (By.XPATH, '//button[@class="navigation-close" and @title="Close navigation"]')
    CONFIRM_PASSWORD_SELECTOR = (By.XPATH, '//input[@id="password-confirmation-social" and @title="Confirm Password"]')
    CREATE_ACCOUNT_SELECTOR = (By.XPATH, '//a[contains(text(), "Create an Account")]')
    CREATE_ACCOUNT_BUTTON_SELECTOR = (By.XPATH, '//button[@id="button-create-social" and @title="Create an Account"]')
    CREATE_FIRST_NAME_INVALID_SELECTOR = (By.XPATH, '//div[contains(text(), "First Name is not valid!")]')
    CREATE_INVALID_PASSWORD_SELECTOR = (By.XPATH, '//div[contains(text(), "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters.")]')
    CREATE_LAST_NAME_INVALID_SELECTOR = (By.XPATH, '//div[contains(text(), "Last Name is not valid!")]')
    CREATE_SIX_CHARACTER_PASSWORD_SELECTOR = (By.XPATH, '//div[contains(text(), "The password needs at least 8 characters. Create a new password and try again.")]')
    CREATE_SHORT_PASSWORD_SELECTOR = (By.XPATH, '//div[@id="password-social-error"]')
    EMAIL_ADDRESS_SELECTOR = (By.XPATH, '//input[@id="email_address_create" and @title="Email"]')
    ERROR_CREATE_MESSAGE_SELECTOR = (By.XPATH, '//div[contains(text(), "There is already an account with this email address. If you are sure that it is your email address, ")]')
    ERROR_INVALID_FIELD_SELECTOR = (By.XPATH, '//div[@id="email_address_create-error"]')
    FIRST_NAME_SELECTOR = (By.XPATH, '//input[@id="firstname" and @title="First Name"]')
    LAST_NAME_SELECTOR = (By.XPATH, '//input[@id="lastname" and @title="Last Name"]')
    PASSWORD_INPUT_SELECTOR = (By.XPATH, '//input[@id="password-social" and @title="Password"]')
    SIGN_OUT_BUTTON_SELECTOR = (By.XPATH, '//li[@class="link authorization-link"]')
    SIGN_OUT_MENU_SELECTOR = (By.XPATH, '//button[@class="action switch" and @data-action="customer-menu-toggle"]')
    SIGN_OUT_MESSAGE_SELECTOR = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    WELCOME_MESSAGE_SELECTOR = (By.XPATH, '//span[@class="logged-in"]')

    def generate_random_email(self):
        random_number = random.randint(1, 9999)
        return f'test{random_number}@test.com'

    def navigate_to_page(self):
        self.driver.get(self.URL)

    def close_navigation_demo(self):
        self.wait_for_element(self.CLOSE_DEMO_NAVIGATION_SELECTOR, 10).click()

    def click_create_account_menu(self):
        self.wait_for_element(self.CREATE_ACCOUNT_SELECTOR, 10).click()

    def insert_first_name(self, first_name):
        self.type(self.FIRST_NAME_SELECTOR, first_name)

    def insert_last_name(self, last_name):
        self.type(self.LAST_NAME_SELECTOR, last_name)

    def insert_email(self):
        self.type(self.EMAIL_ADDRESS_SELECTOR, self.generate_random_email())

    def insert_email_wrong(self, email):
        self.type(self.EMAIL_ADDRESS_SELECTOR, email)

    def insert_password(self, password):
        self.type(self.PASSWORD_INPUT_SELECTOR, password)

    def confirm_password(self, password):
        self.type(self.CONFIRM_PASSWORD_SELECTOR, password)

    def click_create_account_button(self):
        self.click(self.CREATE_ACCOUNT_BUTTON_SELECTOR)

    def click_sign_out_menu(self):
        self.click(self.SIGN_OUT_MENU_SELECTOR)

    def click_sign_out_button(self):
        self.click(self.SIGN_OUT_BUTTON_SELECTOR)

    def get_invalid_mail_message_text(self):
        return self.get_element_text(self.ERROR_INVALID_FIELD_SELECTOR)

    def get_invalid_firstname_message_text(self):
        return self.get_element_text(self.CREATE_FIRST_NAME_INVALID_SELECTOR)

    def get_invalid_lastname_message_text(self):
        return self.get_element_text(self.CREATE_LAST_NAME_INVALID_SELECTOR)

    def get_short_password_message_text(self):
        return self.get_element_text(self.CREATE_SHORT_PASSWORD_SELECTOR)

    def get_six_digits_password_message_text(self):
        return self.get_element_text(self.CREATE_SIX_CHARACTER_PASSWORD_SELECTOR)

    def get_invalid_password_message_text(self):
        return self.get_element_text(self.CREATE_INVALID_PASSWORD_SELECTOR)

    def get_sign_out_message_text(self):
        return self.get_element_text(self.SIGN_OUT_MESSAGE_SELECTOR)

    def get_account_already_created_message_text(self):
        return self.get_element_text(self.ERROR_CREATE_MESSAGE_SELECTOR)

    def get_message_text(self):
        time.sleep(5)
        return self.get_element_text(self.WELCOME_MESSAGE_SELECTOR)
