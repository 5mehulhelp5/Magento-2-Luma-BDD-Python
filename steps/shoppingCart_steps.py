from behave import *


@given('I create a new account')
def step_execute_create_account(context):
    context.execute_steps('\n'
                          '        Given I am on create an account page\n'
                          '        When I click on crete account menu\n'
                          '        When I insert the first name "Mihai"\n'
                          '        When I insert the last name "Daneasa"\n'
                          '        When I insert the email\n'
                          '        When I insert the password "test@Magento1"\n'
                          '        When I confirm the password "test@Magento1"\n'
                          '        When I click the create account button\n'
                          '        Then The message is "Welcome, Mihai Daneasa!"\n'
                          '        '
                          )


@when('I close the demo navigation window')
def step_impl(context):
    context.shoppingCart_page.close_demo_navigation()


@given('I have successfully selected the desired product')
def step_execute_choose_a_product(context):
    context.execute_steps('\n'
                          '        Given I can access the products presentation page \n'
                          '        When I select the group to which the product is addressed \n'
                          '        When I select the product range \n'
                          '        When I click the category button \n'
                          '        When I select pants category \n'
                          '        When I select the product style menu \n'
                          '        When I select the desired style \n'
                          '        When I select the desired product \n'
                          '        '
                          )


@when('I store the product name')
def step_impl(context):
    context.store_product_name = context.shoppingCart_page.store_product_name()


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
    context.restore_product_name = context.shoppingCart_page.restore_product_name()


@then('I verify if the product is the same')
def step_impl(context):
    assert f'{context.restore_product_name}' == f'{context.store_product_name}', 'The product is not the same'


@when('I empty my cart')
def step_impl(context):
    context.shoppingCart_page.remove_items()


@when('I select the cart menu')
def step_impl(context):
    context.shoppingCart_page.select_cart_menu()


@when('I click details button')
def step_impl(context):
    context.shoppingCart_page.select_details_menu()


@when('I click the remove item button')
def step_impl(context):
    context.shoppingCart_page.remove_item_from_cart()


@when('I confirm the removal of the product')
def step_impl(context):
    context.shoppingCart_page.click_remove_item_button()


@then('The removed item message is: "{message}"')
def step_impl(context, message):
    assert message in context.shoppingCart_page.get_removed_item_message()


@when('I store the product base price')
def step_impl(context):
    context.base_price = context.shoppingCart_page.store_product_base_price()


@when('I store the product subtotal price')
def step_impl(context):
    context.subtotal_price = context.shoppingCart_page.store_product_subtotal_price()


@then('I verify if the price is correct')
def step_impl(context):
    assert f'{context.base_price}' == f'{context.subtotal_price}', 'The price is not correctly calculated'


@when('I calculate the product total price')
def step_impl(context):
    context.total_price = context.shoppingCart_page.calculate_product_total_price()


@when('I store the product total price')
def step_impl(context):
    context.total_value = context.shoppingCart_page.store_product_total_value()


@then('I verify if the product value is correct')
def step_impl(context):
    assert f'{context.total_price}' == f'{context.total_value}', 'The total value is not the same'


@when('I click the edit item button')
def step_impl(context):
    context.shoppingCart_page.click_edit_item_button()


@when('I change the size')
def step_impl(context):
    context.shoppingCart_page.change_the_size()


@when('I change the color')
def step_impl(context):
    context.shoppingCart_page.change_the_color()


@when('I change the quantity to "{value}" pieces')
def step_impl(context, value):
    context.shoppingCart_page.change_the_quantity(value)


@when('I update the cart')
def step_impl(context):
    context.shoppingCart_page.update_cart()


@then('The update message is: "{message}"')
def step_impl(context, message):
    assert message in context.shoppingCart_page.get_update_cart_message(), 'The cart is not updated.'


@when('I insert the street "{street}"')
def step_impl(context, street):
    context.shoppingCart_page.insert_street_address(street)


@when('I insert the phone number "{phone}"')
def step_impl(context, phone):
    context.shoppingCart_page.insert_phone_number(phone)


@when('I check the box "My billing and shipping address are the same"')
def step_impl(context):
    context.shoppingCart_page.check_billing_address()


@when('I accept the terms and conditions')
def step_impl(context):
    context.shoppingCart_page.accept_terms()


@when('I place the order')
def step_impl(context):
    context.shoppingCart_page.place_order()


@then('The confirmation message is: "{message}"')
def step_impl(context, message):
    assert message in context.shoppingCart_page.get_confirmation_message(), 'The message is not present'


@given('I am signed out from the account')
def step_execute_create_account(context):
    context.execute_steps('\n'
                          '        When I click on sign out menu\n'
                          '        When I click on sign out button\n'
                          '        Then The sign out message is "You are signed out"\n'
                          '        '
                          )
