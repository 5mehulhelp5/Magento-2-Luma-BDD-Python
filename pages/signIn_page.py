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
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if "https://www.facebook.com/login.php?skip_api_login=1&api_key=744024889374221&kid_directed_site=0&app_id=744024889374221&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D744024889374221%26redirect_uri%3Dhttps%253A%252F%252Fosc-ultimate-demo.mageplaza.com%252Fsociallogin%252Fsocial%252Fcallback%252F%253Fhauth_done%253DFacebook%26scope%3Demail%252C%2Bpublic_profile%26state%3DHA-TWB70L86ASUXRNM4ZYDFGK3PCQ5J2HV9OEI1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7fd97cdf-3833-49a9-85eb-f22a7d66db6b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fosc-ultimate-demo.mageplaza.com%2Fsociallogin%2Fsocial%2Fcallback%2F%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-TWB70L86ASUXRNM4ZYDFGK3PCQ5J2HV9OEI1%23_%3D_&display=page&locale=en_US&pl_dbl=0" in url:
                self.driver.switch_to.window(currentWindow)
                break

    def scroll_down(self):
        self.scroll_down_page()

    def accept_faceboock_cookies(self):
        self.action_chain(FACEBOOCK_ACCEPT_COOKIES_SELECTOR)

    def get_faceboock_error_message_text(self):
        return self.get_element_text(FACEBOOCK_ERROR_MESSAGE_SELECTOR)

    def click_linkedin_signin_button(self):
        self.click(LINKEDIN_LOGIN_SELECTOR)

    def change_handle_to_linkedin_login_page(self):
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if 'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=86n928xh7uro9z&redirect_uri=https%3A%2F%2Fosc-ultimate-demo.mageplaza.com%2Fsociallogin%2Fsocial%2Fcallback%2F%3Fhauth.done%3DLinkedIn&scope=r_liteprofile+r_emailaddress&state=HA-5O0FMR9H2QZYS4UXA8LNW1ITG6V37PCKJBED' in url:
                self.driver.switch_to.window(currentWindow)
                break

    def get_linkedin_error_message_text(self):
        return self.get_element_text(LINKEDIN_ERROR_MESSAGE_SELECTOR)

    def click_yahoo_signin_button(self):
        self.click(YAHOO_LOGIN_SELECTOR)

    def change_handle_to_yahoo_login_page(self):
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if 'https://login.yahoo.com/?src=oauth&client_id=dj0yJmk9dXZGSk1oUzhLdHJKJmQ9WVdrOWFWbDNNMU5VTmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTk4&crumb=&redirect_uri=https%3A%2F%2Fosc-ultimate-demo.mageplaza.com%2Fsociallogin%2Fsocial%2Fcallback%2F&done=https%3A%2F%2Fapi.login.yahoo.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9dXZGSk1oUzhLdHJKJmQ9WVdrOWFWbDNNMU5VTmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTk4%26redirect_uri%3Dhttps%253A%252F%252Fosc-ultimate-demo.mageplaza.com%252Fsociallogin%252Fsocial%252Fcallback%252F%26response_type%3Dcode%26scope%3Dprofile%26state%3DHA-OGZC3P80SB6ALKFDW9M7Q5TJ2REY1NX4IHUV' in url:
                self.driver.switch_to.window(currentWindow)
                break

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

    def get_yahoo_error_message_text(self):
        return self.get_element_text(YAHOO_ERROR_MESSAGE_SELECTOR)

    def change_handle_to_main_page(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def fill_password_field(self, password):
        self.type(YAHOO_INPUT_PASSWORD_SELECTOR, password)

    def fill_confirm_password_field(self, password):
        self.type(YAHOO_CONFIRM_PASSWORD_SELECTOR, password)

    def submit_yahoo_formular(self):
        self.click(YAHOO_SUBMIT_SELECTOR)

    def click_github_signin_button(self):
        self.click(GITHUB_LOGIN_SELECTOR)

    def change_handle_to_github_login_page(self):
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if 'https://github.com/login?client_id=040e38eb71b7778fd9f8&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D040e38eb71b7778fd9f8%26redirect_uri%3Dhttps%253A%252F%252Fosc-ultimate-demo.mageplaza.com%252Fsociallogin%252Fsocial%252Fcallback%252F%253Fhauth.done%253DGithub%26response_type%3Dcode%26scope%3Duser%253Aemail%26state%3DHA-3AI1QKYOC09BNSHLXFZJGM8P25DRWE674UVT' in url:
                login_page = self.driver.switch_to.window(currentWindow)
                break

    def insert_github_username(self, username):
        self.type(GITHUB_EMAIL_SELECTOR, username)

    def insert_github_password(self, password):
        self.type(GITHUB_PASSWORD_SELECTOR, password)

    def click_github_signin(self):
        self.click(GITHUB_SIGNIN_BUTTON_SELECTOR)
