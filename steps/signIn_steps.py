from behave import *


@given('I am on the create an account page')
def step_impl(context):
    context.base_page.navigate_to_page()


@when('I click on the crete account menu')
def step_impl(context):
    context.createAccount_page.click_create_account_menu()


@when('I fill the first name "{first_name}"')
def step_impl(context, first_name):
    context.createAccount_page.insert_first_name(first_name)


@when('I fill the last name "{last_name}"')
def step_impl(context, last_name):
    context.createAccount_page.insert_last_name(last_name)


@when('I fill the email field "{email}"')
def step_impl(context, email):
    context.createAccount_page.insert_email(email)


@when('I fill the password field "{password}"')
def step_impl(context, password):
    context.createAccount_page.insert_password(password)


@when('I fill the confirm password field "{password}"')
def step_impl(context, password):
    context.createAccount_page.confirm_password(password)


@when('I click on create account button')
def step_impl(context):
    context.createAccount_page.click_create_account_button()


@given('I can access the sign in menu')
def step_impl(context):
    context.base_page.navigate_to_page()


@when('I fill the email "{email}"')
def step_impl(context, email):
    context.signIn_page.insert_sign_in_email(email)


@when('I fill the password "{password}"')
def step_impl(context, password):
    context.signIn_page.insert_sign_in_password(password)


@when('I click on sign in menu')
def step_impl(context):
    context.signIn_page.click_signin_menu()


@when('I click on sign in button')
def step_impl(context):
    context.signIn_page.click_sign_in_button()


@when('I access the sign out menu')
def step_impl(context):
    context.signOut_page.click_sign_out_menu()


@when('I click the sign out button')
def step_impl(context):
    context.signOut_page.click_sign_out_button()


@when('I click on Faceboock log in')
def step_impl(context):
    context.signIn_page.click_facebook_signin_button()


@when('I change to Faceboock login page')
def step_impl(context):
    context.signIn_page.change_handle_to_feceboock_login_page()


@when('I scroll down the page')
def step_impl(context):
    context.signIn_page.scroll_down()


@when('I accept cookies')
def step_impl(context):
    context.signIn_page.accept_faceboock_cookies()


@when('I change handle to home page')
def step_impl(context):
    context.signIn_page.change_handle_to_main_page()


@when('I click on Linkedin log in')
def step_impl(context):
    context.signIn_page.click_linkedin_signin_button()


@when('I change to Linkedin login page')
def step_impl(context):
    context.signIn_page.change_handle_to_linkedin_login_page()


@when('I click on Yahoo log in')
def step_impl(context):
    context.signIn_page.click_yahoo_signin_button()


@when('I change to Yahoo login page')
def step_impl(context):
    context.signIn_page.change_handle_to_yahoo_login_page()


@when('I introduce the email "{email}"')
def step_impl(context, email):
    context.signIn_page.insert_yahoo_mail(email)


@when('I click on first next button')
def step_impl(context):
    context.signIn_page.click_first_next_button()


@when('I introduce the password "{password}"')
def step_impl(context, password):
    context.signIn_page.insert_yahoo_password(password)


@when('I click on second next button')
def step_impl(context):
    context.signIn_page.click_second_next_button()


@when('I accept yahoo cookies')
def step_impl(context):
    context.signIn_page.accept_yahoo_cookies()


@when('I click on Yahoo login page')
def step_impl(context):
    context.signIn_page.click_yahoo_signin_button()


@when('I complete the password "{password}"')
def step_impl(context, password):
    context.signIn_page.fill_password_field(password)


@when('I complete the confirm password "{password}"')
def step_impl(context, password):
    context.signIn_page.fill_confirm_password_field(password)


@when('I click the submit button')
def step_impl(context):
    context.signIn_page.submit_yahoo_formular()


@then('The Yahoo error message is "{message}"')
def step_impl(context, message):
    assert message in context.signIn_page.get_yahoo_error_message_text()


@when('I click on Github log in')
def step_impl(context):
    context.signIn_page.click_github_signin_button()


@when('I change to Github login page')
def step_impl(context):
    context.signIn_page.change_handle_to_github_login_page()


@when('I introduce the Github username "{username}"')
def step_impl(context, username):
    context.signIn_page.insert_github_username(username)


@when('I introduce the Github password "{password}"')
def step_impl(context, password):
    context.signIn_page.insert_github_password(password)


@when('I click the Github signin button')
def step_impl(context):
    context.signIn_page.click_github_signin()


@then('The displayed message is "{message}"')
def step_impl(context, message):
    assert message in context.createAccount_page.get_message_text()


@then('The sign out displayed message is "{message}"')
def step_impl(context, message):
    assert message in context.signOut_page.get_sign_out_message_text()


@then('The sign in error message is "{message}"')
def step_impl(context, message):
    assert message in context.signIn_page.get_invalid_email_or_password_message_text()


@then('The invalid email error message is "{message}"')
def step_impl(context, message):
    assert message in context.signIn_page.get_invalid_email_format_message_text()


@then('The Facebook error message is "{message}"')
def step_impl(context, message):
    assert message in context.signIn_page.get_faceboock_error_message_text()


@then('The Linkedin error message is "{message}"')
def step_impl(context, message):
    assert message in context.signIn_page.get_linkedin_error_message_text()
