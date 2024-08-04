import random
import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignIn(BasePage):
    URL = 'https://osc-ultimate-demo.mageplaza.com/'
    FACEBOOK_URL = 'https://www.facebook.com/login.php?skip_api_login=1&api_key=744024889374221&kid_directed_site=0&app_id=744024889374221&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D744024889374221%26redirect_uri%3Dhttps%253A%252F%252Fosc-ultimate-demo.mageplaza.com%252Fsociallogin%252Fsocial%252Fcallback%252F%253Fhauth_done%253DFacebook%26scope%3Demail%252C%2Bpublic_profile%26state%3DHA-9TVEDQ8LKP1CFWJNA7IXH562GYBU4RO30MSZ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Def1a15c6-dc47-4450-87df-51bf4645cd70%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fosc-ultimate-demo.mageplaza.com%2Fsociallogin%2Fsocial%2Fcallback%2F%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-9TVEDQ8LKP1CFWJNA7IXH562GYBU4RO30MSZ%23_%3D_&display=page&locale=ro_RO&pl_dbl=0'

    CLOSE_DEMO_NAVIGATION_SELECTOR = (By.XPATH, '//button[@class="navigation-close" and @title="Close navigation"]')
    CONFIRM_PASSWORD_SELECTOR = (By.XPATH, '//input[@id="password-confirmation-social" and @title="Confirm Password"]')
    CREATE_ACCOUNT_SELECTOR = (By.XPATH, '//a[contains(text(), "Create an Account")]')
    CREATE_ACCOUNT_BUTTON_SELECTOR = (By.XPATH, '//button[@id="button-create-social" and @title="Create an Account"]')
    EMAIL_ADDRESS_SELECTOR = (By.XPATH, '//input[@id="email_address_create" and @title="Email"]')
    FACEBOOCK_ACCEPT_COOKIES_SELECTOR = (By.XPATH, '//button[@data-cookiebanner="accept_button" and @type="submit"] | //span[contains(text(), "Allow all cookies")]')
    FACEBOOCK_ERROR_MESSAGE_SELECTOR = (By.XPATH, '//div[@class="fsl fwb fcb" and contains(text(), "Error Accessing App")]')
    FACEBOOCK_LOGIN_SELECTOR = (By.XPATH, '//a[@class="btn btn-block btn-social btn-facebook"]')
    FIRST_NAME_SELECTOR = (By.XPATH, '//input[@id="firstname" and @title="First Name"]')
    INVALID_LOGIN_OR_PASSWORD_SELECTOR = (By.XPATH, '//div[contains(text(), "Invalid login or password.")]')
    LAST_NAME_SELECTOR = (By.XPATH, '//input[@id="lastname" and @title="Last Name"]')
    LINKEDIN_ERROR_MESSAGE_SELECTOR = (By.XPATH, '//p[@class="message"]')
    LINKEDIN_LOGIN_SELECTOR = (By.XPATH, '//a[@class="btn btn-block btn-social btn-linkedin"]')
    YAHOO_ACCEPT_COOKIES_SELECTOR = (By.XPATH, '//button[@class="pure-button puree-button-primary oauth2-authorize-button"]')
    YAHOO_CONFIRM_PASSWORD_SELECTOR = (By.XPATH, '//input[@id="request-password-confirmation"]')
    YAHOO_INPUT_PASSWORD_SELECTOR = (By.XPATH, '//input[@id="request-password-social"]')
    YAHOO_LOGIN_SELECTOR = (By.XPATH, '//a[@class="btn btn-block btn-social btn-yahoo"]')
    YAHOO_NEXT_BUTTON_SELECTOR_1 = (By.XPATH, '//input[@id="login-signin"]')
    YAHOO_NEXT_BUTTON_SELECTOR_2 = (By.XPATH, '//button[@id="login-signin"]')
    YAHOO_SUBMIT_SELECTOR = (By.XPATH, '//button[@class="action send primary"]')
    YAHOO_USER_EMAIL_SELECTOR = (By.XPATH, '//input[@class="phone-no "]')
    YAHOO_USER_PASSWORD_SELECTOR = (By.XPATH, '//input[@id="login-passwd" and @class="password"]')
    GITHUB_EMAIL_SELECTOR = (By.XPATH, '//input[@class="form-control input-block js-login-field"]')
    GITHUB_LOGIN_SELECTOR = (By.XPATH, '//a[@class="btn btn-block btn-social btn-github"]')
    GITHUB_PASSWORD_SELECTOR = (By.XPATH, '//input[@class="form-control form-control input-block js-password-field"]')
    GITHUB_SIGNIN_BUTTON_SELECTOR = (By.XPATH, '//input[@class="btn btn-primary btn-block js-sign-in-button"]')
    PASSWORD_INPUT_SELECTOR = (By.XPATH, '//input[@id="password-social" and @title="Password"]')
    SIGNIN_BUTTON_SELECTOR = (By.XPATH, '//button[@id="bnt-social-login-authentication"]')
    SIGNIN_EMAIL_SELECTOR = (By.XPATH, '//input[@id="social_login_email"]')
    SIGNIN_ERROR_MESSAGE_1 = (By.XPATH, '//div[contains(text(), "Invalid login or password.")]')
    SIGNIN_ERROR_MESSAGE_2 = (By.XPATH, '//div[@id="social_login_email-error"]')
    SIGNIN_PASSWORD_SELECTOR = (By.XPATH, '//input[@id="social_login_pass"]')
    SIGNIN_SELECTOR = (By.XPATH, '//a[contains(text(), "Sign In")]')
    SIGN_OUT_BUTTON_SELECTOR = (By.XPATH, '//li[@class="link authorization-link"]')
    SIGN_OUT_MENU_SELECTOR = (By.XPATH, '//button[@class="action switch" and @data-action="customer-menu-toggle"]')
    SIGN_OUT_MESSAGE_SELECTOR = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    WELCOME_MESSAGE_SELECTOR = (By.XPATH, '//span[@class="logged-in"]')

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

    def insert_email(self, email):
        self.type(self.EMAIL_ADDRESS_SELECTOR, email)

    def insert_password(self, password):
        self.type(self.PASSWORD_INPUT_SELECTOR, password)

    def confirm_password(self, password):
        self.type(self.CONFIRM_PASSWORD_SELECTOR, password)

    def click_create_account_button(self):
        self.click(self.CREATE_ACCOUNT_BUTTON_SELECTOR)

    def get_message_text(self):
        time.sleep(5)
        return self.get_element_text(self.WELCOME_MESSAGE_SELECTOR)

    def click_sign_out_menu(self):
        self.click(self.SIGN_OUT_MENU_SELECTOR)

    def click_sign_out_button(self):
        self.click(self.SIGN_OUT_BUTTON_SELECTOR)

    def get_sign_out_message_text(self):
        return self.get_element_text(self.SIGN_OUT_MESSAGE_SELECTOR)

    def click_signin_menu(self):
        self.wait_for_element(self.SIGNIN_SELECTOR, 10).click()

    def insert_sign_in_email(self, email):
        self.type(self.SIGNIN_EMAIL_SELECTOR, email)

    def insert_sign_in_password(self, password):
        self.type(self.SIGNIN_PASSWORD_SELECTOR, password)

    def click_sign_in_button(self):
        self.click(self.SIGNIN_BUTTON_SELECTOR)

    def get_invalid_email_or_password_message_text(self):
        return self.get_element_text(self.INVALID_LOGIN_OR_PASSWORD_SELECTOR)

    def get_invalid_email_format_message_text(self):
        return self.get_element_text(self.SIGNIN_ERROR_MESSAGE_2)

    def click_facebook_signin_button(self):
        self.click(self.FACEBOOCK_LOGIN_SELECTOR)

    def change_handle_to_feceboock_login_page(self):
        self.change_to_faceboock_window()

    def scroll_down(self):
        self.scroll_down_page()

    def accept_faceboock_cookies(self):
        self.accept_cookies(self.FACEBOOCK_ACCEPT_COOKIES_SELECTOR)

    def get_faceboock_error_message_text(self):
        return self.get_element_text(self.FACEBOOCK_ERROR_MESSAGE_SELECTOR)

    def click_linkedin_signin_button(self):
        self.click(self.LINKEDIN_LOGIN_SELECTOR)

    def change_handle_to_linkedin_login_page(self):
        self.change_to_linkedin_window()

    def get_linkedin_error_message_text(self):
        return self.get_element_text(self.LINKEDIN_ERROR_MESSAGE_SELECTOR)

    def click_yahoo_signin_button(self):
        self.click(self.YAHOO_LOGIN_SELECTOR)

    def change_handle_to_yahoo_login_page(self):
        self.change_to_yahoo_window()

    def insert_yahoo_mail(self, email):
        self.type(self.YAHOO_USER_EMAIL_SELECTOR, email)

    def click_first_next_button(self):
        self.click(self.YAHOO_NEXT_BUTTON_SELECTOR_1)

    def insert_yahoo_password(self, password):
        self.type(self.YAHOO_USER_PASSWORD_SELECTOR, password)

    def click_second_next_button(self):
        self.click(self.YAHOO_NEXT_BUTTON_SELECTOR_2)

    def accept_yahoo_cookies(self):
        self.click(self.YAHOO_ACCEPT_COOKIES_SELECTOR)

    def change_handle_to_main_page(self):
        self.change_to_main_window()

    def fill_password_field(self, password):
        self.type(self.YAHOO_INPUT_PASSWORD_SELECTOR, password)

    def fill_confirm_password_field(self, password):
        self.type(self.YAHOO_CONFIRM_PASSWORD_SELECTOR, password)

    def submit_yahoo_formular(self):
        self.click(self.YAHOO_SUBMIT_SELECTOR)

    def click_github_signin_button(self):
        self.click(self.GITHUB_LOGIN_SELECTOR)

    def change_handle_to_github_login_page(self):
        self.change_to_github_window()

    def insert_github_username(self, username):
        self.type(self.GITHUB_EMAIL_SELECTOR, username)

    def insert_github_password(self, password):
        self.type(self. GITHUB_PASSWORD_SELECTOR, password)

    def click_github_signin(self):
        self.click(self.GITHUB_SIGNIN_BUTTON_SELECTOR)





