@shoppingCart
Feature: All shopping cart related tests
  Scenario: Positive create an account
    Given I can access the create account page
    When I click the crete account menu
    When I complete the first name "Mihai"
    When I complete the last name "Daneasa"
    When I complete the email
    When I complete the password field "test@Magento1"
    When I complete the confirm password field "test@Magento1"
    When I press the create account button
    Then The message displayed is: "Welcome, Mihai Daneasa!"

  Scenario: Adding a product to shopping cart
    Given I am on the main page
    When I chose the group to which the product is addressed
    When I chose the product range
    When I click on the category button
    When I chose pants category
    When I chose the product style menu
    When I chose the desired style
    When I chose the desired product
    When I store the product name
    When I chose the desired size
    When I chose the desired color
    When I chose the quantity "1"
    When I add the product to cart
    Then I am redirected to cart page "https://osc-ultimate-demo.mageplaza.com/default/admindemo/"
    When I restore the product name
    Then I verify if "The product is the same"
    When I empty my cart


