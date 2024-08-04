@signIn
Feature: All signin related tests
  Scenario: Positive create an account
    Given I can access the create an account page
#    When I close the demo navigation page
    When I acces the crete account menu
    When I input the first name "Mihai"
    When I input the last name "Daneasa"
    When I input the email "testareabc@test.com"
    When I input the password "test@Magento1"
    When I confirm password "test@Magento1"
    When I click create account button
    Then The displayed message is "Welcome, Mihai Daneasa!"

  Scenario: Sign out scenario
    Given I am in the user account
    When I accesss the sign out menu
    When I click the sign out button
    Then The sign out displayed message is "You are signed out"

  Scenario: Sign in scenario Positive
    Given I can acces the sign in menu
    When I click on sign in menu
    When I fill the email "testare@test.com"
    When I fill the password "test@Magento1"
    When I click on sign in button
    Then The sign in message is "Welcome, Mihai Daneasa!"

  Scenario: Sign out scenario
    Given I am in the user page
    When I accesss the sign out menu
    When I click the sign out button
    Then The sign out displayed message is "You are signed out"

  Scenario: Invalid email sign in
    Given I can acces the sign in menu
    When I click on sign in menu
    When I fill the email "testalfabetaomega@test.com"
    When I fill the password "test@Magento1"
    When I click on sign in button
    Then The sign in error message is "Invalid login or password."

  Scenario: Invalid password
    Given I can acces the sign in menu
    When I click on sign in menu
    When I fill the email "testare2@test.com"
    When I fill the password "test@Magento123"
    When I click on sign in button
    Then The sign in error message is "Invalid login or password."

  Scenario: Incorrect email format sign in
    Given I can acces the sign in menu
    When I click on sign in menu
    When I fill the email "testare#test.com"
    When I fill the password "test@Magento123"
    When I click on sign in button
    Then The invalid email error message is "Please enter a valid email address (Ex: johndoe@domain.com)."

  Scenario: Faceboock sign in
    Given I can acces the sign in menu
    When I click on sign in menu
    When I click on Faceboock log in
    When I change to Faceboock login page
    When I scroll down the page
    When I accept cookies
    Then The Facebook error message is "Error Accessing App"
    When I change handle to home page


  Scenario: Linkedin sign in
    Given I can acces the sign in menu
    When I click on sign in menu
    When I click on Linkedin log in
    When I change to Linkedin login page
    Then The Linkedin error message is "The application is disabled"
    When I change handle again to home page

  Scenario: Yahoo sign in
    Given I can acces the sign in menu
    When I click on sign in menu
    When I click on Yahoo log in
    When I change to Yahoo login page
    When I introduce the email "mihaiteste@yahoo.com"
    When I click on first next button
    When I introduce the password "245228@Magento"
    When I click on second next button
    When I accept yahoo cookies
    When I change handle to main page
    When I click on Yahoo login page
    When I complete the password "test@magento1"
    When I complete the confirm password "test@magento1"
    When I click the submit button
    Then The Yahoo signin message is "Welcome, Mihai Daneasa!"

  Scenario: Sign out scenario
    Given I am in the user page
    When I accesss the sign out menu
    When I click the sign out button
    Then The sign out displayed message is "You are signed out"

  Scenario: Github sign in
    Given I can acces the sign in menu
    When I click on sign in menu
    When I click on Github log in
    When I change to Github login page
    When I introduce the Github username "mihaiteste"
    When I introduce the Github password "245228@Magento"
    When I click the Github signin button
    When I will change handle to main page
    Then The Github signin message is "Welcome, Mihai Daneasa!"