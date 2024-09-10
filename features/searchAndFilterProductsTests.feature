@searchProducts
Feature: All tests related to search and filter products
  Background:
    Given I can access the products presentation page

  Scenario: Search for a product
    When I click on search bar
    When I search for product "pants"
    When I click on search button
    Then The search message is "The total item text is equal with the total items founded."

  Scenario: Product not found
    When I click on search bar
    When I search for product "Bees"
    When I click on search button
    Then The product not found message is "Your search returned no results."

  Scenario: Selecting products filter
    When I click on the "What's new" product category
    When I click the product category button
    When I select the product color
    When I select the color White
    When I select the product size
    When I select the size L
    Then The product filter message is "I found all the products."

  Scenario: Sorting products
    When I click on search bar
    When I search for product "pants"
    When I click on search button
    When I sort the products by "Price"
    Then The products sorting message is "The list is sorted."

  Scenario: Applying filters to products doesn't modify the page layout
    When I select the group to which the product is addressed
    When I select the product range
    When I click the category button
    When I select pants category
    When I select the product style menu
    When I select the desired style
    When I select the desired product
    When I store the product presentation images
    When I select the size 34
    When I select the color blue
    When I restore the product presentation images
    Then The filtering message is "The page layout is the same."