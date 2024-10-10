@shoppingCart
Feature: All shopping cart related tests (#all test are passed if they are run with the tag)
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
    Then I verify if the product is the same
    When I empty my cart
    Then The removed item message is: "You have no items in your shopping cart."

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

  Scenario: Verify subtotal price
    Given I have successfully selected the desired product
    When I store the product base price
    When I chose the desired size
    When I chose the desired color
    When I chose the quantity "2"
    When I add the product to cart
    When I store the product subtotal price
    Then I verify if the price is correct
    When I empty my cart
    Then The removed item message is: "You have no items in your shopping cart."

  Scenario: Verify the total price
    Given I have successfully selected the desired product
    When I chose the desired size
    When I chose the desired color
    When I chose the quantity "5"
    When I add the product to cart
    When I calculate the product total price
    When I store the product total price
    Then I verify if the product value is correct
    When I empty my cart
    Then The removed item message is: "You have no items in your shopping cart."

  Scenario: Edit item in cart
    Given I have successfully selected the desired product
    When I chose the desired size
    When I chose the desired color
    When I chose the quantity "2"
    When I add the product to cart
    When I select the cart menu
    When I click details button
    When I click the edit item button
    When I change the size
    When I change the color
    When I change the quantity to "5" pieces
    When I update the cart
    Then The update message is: "Geo Insulated Jogging Pant was updated in your shopping cart."

  Scenario: Place an order
    Given I have successfully selected the desired product
    When I chose the desired size
    When I chose the desired color
    When I chose the quantity "2"
    When I add the product to cart
    When I insert the street "Victoriei, 3"
    When I insert the phone number "1234567890"
    When I check the box "My billing and shipping address are the same"
    When I accept the terms and conditions
    When I place the order
    Then The confirmation message is: "Thank you for your purchase!"

  Scenario: Sign out from account
    Given I am signed out from the account