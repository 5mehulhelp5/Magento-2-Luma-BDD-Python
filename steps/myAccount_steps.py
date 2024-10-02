from behave import *


@given('I am creating a new account')
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


@given('I can access the my account page')
def step_impl(context):
    context.base_page.navigate_to_page()


@when('I access My account menu')
def step_impl(context):
    context.myAccount_page.access_account_menu()


@when('I press the My account button')
def step_impl(context):
    context.myAccount_page.click_account_button()


@when('I access the edit shipping address')
def step_impl(context):
    context.myAccount_page.access_edit_shipping_address()


@when('I edit the street "{street}"')
def step_impl(context, street):
    context.myAccount_page.street_input(street)


@when('I edit the country "{country}"')
def step_impl(context, country):
    context.myAccount_page.country_select(country)


@when('I edit the region "{region}"')
def step_impl(context, region):
    context.myAccount_page.region_select(region)


@when('I edit the phone number "{phone}"')
def step_impl(context, phone):
    context.myAccount_page.phone_input(phone)


@when('I edit the city "{city}"')
def step_impl(context, city):
    context.myAccount_page.city_input(city)


@when('I edit the zip code "{zip_code}"')
def step_impl(context, zip_code):
    context.myAccount_page.zip_code_input(zip_code)


@when('I press the save button')
def step_impl(context):
    context.myAccount_page.click_save_button()


@then('The edit shipping address message is "{message}"')
def step_impl(context, message):
    assert message in context.myAccount_page.get_save_address_message()


@when('I click on the sign out menu')
def step_impl(context):
    context.signOut_page.click_sign_out_menu()


@when('I click on the sign out button')
def step_impl(context):
    context.signOut_page.click_sign_out_button()


@then('The signout message is "{message}"')
def step_impl(context, message):
    assert message in context.signOut_page.get_sign_out_message_text()
