from driver import Driver
from pages.createAccount_page import CreateAccount
from pages.signIn_page import SignIn

def before_all(context):
    context.browser = Driver()
    context.createAccount_page = CreateAccount()
    context.signIn_page = SignIn()

def after_all(context):
    context.browser.close()