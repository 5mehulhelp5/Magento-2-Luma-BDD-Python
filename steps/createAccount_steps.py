from behave import *


@given('I am on create an account page')
def step_impl(context):
    context.base_page.navigate_to_page()


@when('I click on crete account menu')
def step_impl(context):
    context.createAccount_page.click_create_account_menu()


@when('I insert the first name "{first_name}"')
def step_impl(context, first_name):
    context.createAccount_page.insert_first_name(first_name)


@when('I insert the last name "{last_name}"')
def step_impl(context, last_name):
    context.createAccount_page.insert_last_name(last_name)


@when('I insert the email "{email}"')
def step_impl(context, email):
    context.createAccount_page.insert_email(email)


@when('I insert the email')
def step_impl(context):
    context.createAccount_page.insert_random_email()


@when('I insert the password "{password}"')
def step_impl(context, password):
    context.createAccount_page.insert_password(password)


@when('I confirm the password "{password}"')
def step_impl(context, password):
    context.createAccount_page.confirm_password(password)


@when('I click the create account button')
def step_impl(context):
    context.createAccount_page.click_create_account_button()


@when('I click on sign out menu')
def step_impl(context):
    context.signOut_page.click_sign_out_menu()


@when('I click on sign out button')
def step_impl(context):
    context.signOut_page.click_sign_out_button()


@then('The wrong email format message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_invalid_mail_message_text()


@then('The firstname error message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_invalid_firstname_message_text()


@then('The lastname error message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_invalid_lastname_message_text()


@then('The short password error message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_short_password_message_text()


@then('The six character password error message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_six_digits_password_message_text()


@then('The invalid password error message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_invalid_password_message_text()


@then('The sign out message is "{message}"')
def step_impl(context, message):
    assert message in context.signOut_page.get_sign_out_message_text()


@then('The error message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_account_already_created_message_text()


@then('The message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_message_text()
