from behave import *


@given('I can access the create account page')
def step_impl(context):
    context.base_page.navigate_to_page()


@when('I close the demo navigation window')
def step_impl(context):
    context.shoppingCart_page.close_demo_navigation()


@when('I click the crete account menu')
def step_impl(context):
    context.createAccount_page.click_create_account_menu()


@when('I complete the first name "{first_name}"')
def step_impl(context, first_name):
    context.createAccount_page.insert_first_name(first_name)


@when('I complete the last name "{last_name}"')
def step_impl(context, last_name):
    context.createAccount_page.insert_last_name(last_name)


@when('I complete the email')
def step_impl(context):
    context.createAccount_page.insert_random_email()


@when('I complete the password field "{password}"')
def step_impl(context, password):
    context.createAccount_page.insert_password(password)


@when('I complete the confirm password field "{password}"')
def step_impl(context, password):
    context.createAccount_page.confirm_password(password)


@when('I press the create account button')
def step_impl(context):
    context.createAccount_page.click_create_account_button()


@then('The message displayed is: "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_message_text()


@given('I am on the main page')
def step_impl(context):
    context.base_page.navigate_to_page()


@when('I chose the group to which the product is addressed')
def step_impl(context):
    context.searchAndFilterProducts_page.group_selection()


@when('I chose the product range')
def step_impl(context):
    context.searchAndFilterProducts_page.range_selection()


@when('I click on the category button')
def step_impl(context):
    context.searchAndFilterProducts_page.category_selection()


@when('I chose pants category')
def step_impl(context):
    context.searchAndFilterProducts_page.pants_category_selection()


@when('I chose the product style menu')
def step_impl(context):
    context.searchAndFilterProducts_page.style_menu_selection()


@when('I chose the desired style')
def step_impl(context):
    context.searchAndFilterProducts_page.style_selection()


@when('I chose the desired product')
def step_impl(context):
    context.searchAndFilterProducts_page.product_selection()


@when('I store the product name')
def step_impl(context):
    context.shoppingCart_page.store_product_name()


@when('I chose the desired size')
def step_impl(context):
    context.shoppingCart_page.chose_size()


@when('I chose the desired color')
def step_impl(context):
    context.shoppingCart_page.chose_color()


@when('I chose the quantity "{value}"')
def step_impl(context, value):
    context.shoppingCart_page.chose_quantity(value)


@when('I add the product to cart')
def step_impl(context):
    context.shoppingCart_page.add_product_to_cart()


@then('I am redirected to cart page "{url}"')
def step_impl(context, url):
    assert url in context.shoppingCart_page.verify_cart_page_url()


@when('I restore the product name')
def step_impl(context):
    context.shoppingCart_page.restore_product_name()


@then('I verify if "{message}"')
def step_impl(context, message):
    assert message in context.shoppingCart_page.verify_if_product_is_the_same()


@when('I empty my cart')
def step_impl(context):
    context.shoppingCart_page.remove_items()


@when('I close the shopping cart window')
def step_impl(context):
    context.shoppingCart_page.close_shopping_cart_window()


@when('I press the sign out menu')
def step_impl(context):
    context.signOut_page.click_sign_out_menu()


@when('I press the sign out button')
def step_impl(context):
    context.signOut_page.click_sign_out_button()


@then('The message displayed is "{message}"')
def step_impl(context, message):
    assert message in context.signOut_page.get_sign_out_message_text()


