from help_selectors.signInSelectors import *
from pages.base_page import BasePage


class SignIn(BasePage):

    def insert_email(self, email):
        self.type(EMAIL_ADDRESS_SELECTOR, email)

    def click_signin_menu(self):
        self.wait_for_element(SIGNIN_SELECTOR, 10).click()

    def insert_sign_in_email(self, email):
        self.type(SIGNIN_EMAIL_SELECTOR, email)

    def insert_sign_in_password(self, password):
        self.type(SIGNIN_PASSWORD_SELECTOR, password)

    def click_sign_in_button(self):
        self.click(SIGNIN_BUTTON_SELECTOR)

    def get_invalid_email_or_password_message_text(self):
        return self.get_element_text(INVALID_LOGIN_OR_PASSWORD_SELECTOR)

    def get_invalid_email_format_message_text(self):
        return self.get_element_text(SIGNIN_ERROR_MESSAGE_2)

    def click_facebook_signin_button(self):
        self.click(FACEBOOCK_LOGIN_SELECTOR)

    def change_handle_to_feceboock_login_page(self):
        self.change_to_faceboock_window()

    def scroll_down(self):
        self.scroll_down_page()

    def accept_faceboock_cookies(self):
        self.action_chain(FACEBOOCK_ACCEPT_COOKIES_SELECTOR)

    def get_faceboock_error_message_text(self):
        return self.get_element_text(FACEBOOCK_ERROR_MESSAGE_SELECTOR)

    def click_linkedin_signin_button(self):
        self.click(LINKEDIN_LOGIN_SELECTOR)

    def change_handle_to_linkedin_login_page(self):
        self.change_to_linkedin_window()

    def get_linkedin_error_message_text(self):
        return self.get_element_text(LINKEDIN_ERROR_MESSAGE_SELECTOR)

    def click_yahoo_signin_button(self):
        self.click(YAHOO_LOGIN_SELECTOR)

    def change_handle_to_yahoo_login_page(self):
        self.change_to_yahoo_window()

    def insert_yahoo_mail(self, email):
        self.type(YAHOO_USER_EMAIL_SELECTOR, email)

    def click_first_next_button(self):
        self.click(YAHOO_NEXT_BUTTON_SELECTOR_1)

    def insert_yahoo_password(self, password):
        self.type(YAHOO_USER_PASSWORD_SELECTOR, password)

    def click_second_next_button(self):
        self.click(YAHOO_NEXT_BUTTON_SELECTOR_2)

    def accept_yahoo_cookies(self):
        self.click(YAHOO_ACCEPT_COOKIES_SELECTOR)

    def change_handle_to_main_page(self):
        self.change_to_main_window()

    def fill_password_field(self, password):
        self.type(YAHOO_INPUT_PASSWORD_SELECTOR, password)

    def fill_confirm_password_field(self, password):
        self.type(YAHOO_CONFIRM_PASSWORD_SELECTOR, password)

    def submit_yahoo_formular(self):
        self.click(YAHOO_SUBMIT_SELECTOR)

    def click_github_signin_button(self):
        self.click(GITHUB_LOGIN_SELECTOR)

    def change_handle_to_github_login_page(self):
        self.change_to_github_window()

    def insert_github_username(self, username):
        self.type(GITHUB_EMAIL_SELECTOR, username)

    def insert_github_password(self, password):
        self.type(GITHUB_PASSWORD_SELECTOR, password)

    def click_github_signin(self):
        self.click(GITHUB_SIGNIN_BUTTON_SELECTOR)
