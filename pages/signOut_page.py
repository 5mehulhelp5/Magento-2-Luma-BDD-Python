from help_selectors.signInSelectors import *
from pages.base_page import BasePage


class SignOut(BasePage):

    def click_sign_out_menu(self):
        self.click(SIGN_OUT_MENU_SELECTOR)

    def click_sign_out_button(self):
        self.click(SIGN_OUT_BUTTON_SELECTOR)

    def get_sign_out_message_text(self):
        return self.get_element_text(SIGN_OUT_MESSAGE_SELECTOR)
