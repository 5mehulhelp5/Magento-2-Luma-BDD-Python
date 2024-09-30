@shoppingCart
Feature: All shopping cart related tests
  Scenario: Positive create an account
    Given I create a new account

  Scenario: Adding a product to shopping cart
    Given I have successfully selected the desired product
    When I close the demo navigation window
    When I store the product name
    When I chose the desired size
    When I chose the desired color
    When I chose the quantity "1"
    When I add the product to cart
    Then I am redirected to cart page "https://osc-ultimate-demo.mageplaza.com/default/admindemo/"
    When I restore the product name
    Then I verify if "The product is the same"
    When I empty my cart

  Scenario: Remove an item from cart
    Given I have successfully selected the desired product
    When I chose the desired size
    When I chose the desired color
    When I chose the quantity "1"
    When I add the product to cart
    When I select the cart menu
    When I click details button
    When I click the remove item button
    When I confirm the removal of the product
    Then The removed item message is: "You have no items in your shopping cart."

  Scenario: Sign out from account
    When I close the shopping cart window
    When I press the sign out menu
    When I press the sign out button
    Then The message displayed is "You are signed out"

