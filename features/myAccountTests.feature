@myAccount
Feature: All tests related to My Account
  Scenario: Positive create an account
    Given I can access the create an account page
    When I click on crete a new account menu
    When I input the first name "Mihai"
    When I input the last name "Daneasa"
    When I input the email
    When I input the password "test@Magento1"
    When I confirm the new password "test@Magento1"
    When I click on the create account button
    Then The create account message is "Welcome, Mihai Daneasa!"

  Scenario: Positive edit shipping address
    Given I can access the my account page
    When I access My account menu
    When I press the My account button
    When I access the edit shipping address
    When I edit the street "Principala"
    When I edit the country "Romania"
    When I edit the region "Alba"
    When I edit the phone number "0123456789"
    When I edit the city "Cugir"
    When I edit the zip code "515600"
    When I press the save button
    Then The edit shipping address message is "You saved the address."

  Scenario: Negative edit shipping address
    Given I can access the my account page
    When I access My account menu
    When I press the My account button
    When I access the edit shipping address
    When I edit the street "@#$%^^"
    When I edit the country "Romania"
    When I edit the region "Alba"
    When I edit the phone number "alfabeta"
    When I edit the city "@#$%"
    When I edit the zip code "gama"
    When I press the save button
    Then The edit shipping address message is "You entered incorrect values."

  Scenario: Sign out
    Given I can access the my account page
    When I click on the sign out menu
    When I click on the sign out button
    Then The signout message is "You are signed out"