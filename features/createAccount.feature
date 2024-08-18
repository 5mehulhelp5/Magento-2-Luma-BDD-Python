@createAccount
Feature: All the tests related to create an account
  Background:
    Given I am on create an account page
    When When I click on crete account menu

  Scenario: Input a wrong email format
    When I insert the first name "Mihai"
    When I insert the last name "Daneasa"
    When I insert the email "testare#test.com"
    When I insert the password "test@Magento1"
    When I confirm the password "test@Magento1"
    When I click the create account button
    Then The wrong email format message is "Please enter a valid email address (Ex: johndoe@domain.com)."

  Scenario: Special character in first name
    When I insert the first name "Mihai#"
    When I insert the last name "Daneasa"
    When I insert the email
    When I insert the password "test@Magento1"
    When I confirm the password "test@Magento1"
    When I click the create account button
    Then The firstname error message is "First Name is not valid!"

  Scenario: Special character in last name
    When I insert the first name "Mihai"
    When I insert the last name "Daneasa#"
    When I insert the email
    When I insert the password "test@Magento1"
    When I confirm the password "test@Magento1"
    When I click the create account button
    Then The lastname error message is "Last Name is not valid!"

  Scenario: Insert a short password
    When I insert the first name "Mihai"
    When I insert the last name "Daneasa"
    When I insert the email
    When I insert the password "123"
    When I confirm the password "123"
    When I click the create account button
    Then The short password error message is "Please enter 6 or more characters. Leading and trailing spaces will be ignored"

  Scenario: Insert a six character password
    When I insert the first name "Mihai"
    When I insert the last name "Daneasa"
    When I insert the email
    When I insert the password "123abc"
    When I confirm the password "123abc"
    When I click the create account button
    Then The six character password error message is "The password needs at least 8 characters. Create a new password and try again."

  Scenario: Insert an invalid password
    When I insert the first name "Mihai"
    When I insert the last name "Daneasa"
    When I insert the email
    When I insert the password "123abc78"
    When I confirm the password "123abc78"
    When I click the create account button
    Then The invalid password error message is "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters."

  Scenario: Digits in first name and last name
    When I insert the first name "Mihai1"
    When I insert the last name "Daneasa1"
    When I insert the email "testaredelta1@test.com"
    When I insert the password "test@Magento1"
    When I confirm the password "test@Magento1"
    When I click the create account button
    Then The message is "Welcome, Mihai1 Daneasa1!"
    When I click on sign out menu
    When I click on sign out button
    Then The sign out message is "You are signed out"

  Scenario: Account already created
    When I insert the first name "Mihai1"
    When I insert the last name "Daneasa1"
    When I insert the email "testare@test.com"
    When I insert the password "test@Magento1"
    When I confirm the password "test@Magento1"
    When I click the create account button
    Then The error message is "There is already an account with this email address. If you are sure that it is your email address, "

  Scenario: Positive create an account
    Given I am on create an account page
    When When I click on crete account menu
    When I insert the first name "Mihai"
    When I insert the last name "Daneasa"
    When I insert the email
    When I insert the password "test@Magento1"
    When I confirm the password "test@Magento1"
    When I click the create account button
    Then The message is "Welcome, Mihai Daneasa!"
    When I click on sign out menu
    When I click on sign out button
    Then The sign out message is "You are signed out"