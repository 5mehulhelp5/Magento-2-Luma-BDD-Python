from driver import Driver
from pages.base_page import BasePage
from pages.createAccount_page import CreateAccount
from pages.signIn_page import SignIn
from pages.signOut_page import SignOut
from pages.myAccount_page import MyAccount
from pages.searchAndFilterProducts_page import SearchAndFilterProducts
from pages.shoppingCart_page import ShoppingCart


def before_all(context):

    context.browser = Driver()
    context.base_page = BasePage()
    context.createAccount_page = CreateAccount()
    context.signIn_page = SignIn()
    context.signOut_page = SignOut()
    context.myAccount_page = MyAccount()
    context.shoppingCart_page = ShoppingCart()
    context.searchAndFilterProducts_page = SearchAndFilterProducts()


def after_all(context):
    context.browser.close()
