from behave import *


@given('I can access the products presentation page')
def step_impl(context):
    context.base_page.navigate_to_page()


@when('I click on search bar')
def step_impl(context):
    context.searchAndFilterProducts_page.click_search_bar()


@when('I search for product "{product}"')
def step_impl(context, product):
    context.searchAndFilterProducts_page.search_a_product(product)


@when('I click on search button')
def step_impl(context):
    context.searchAndFilterProducts_page.click_search_button()


@then('The search message is "{message}"')
def step_impl(context, message):
    assert message in context.searchAndFilterProducts_page.verify_total_items_founded()


@then('The product not found message is "{message}"')
def step_impl(context, message):
    assert message in context.searchAndFilterProducts_page.verify_product_not_found()


@when('I click on the "What\'s new" product category')
def step_impl(context):
    context.searchAndFilterProducts_page.click_whats_new_menu()


@when('I click the product category button')
def step_impl(context):
    context.searchAndFilterProducts_page.click_product_category()


@when('I select the product color')
def step_impl(context):
    context.searchAndFilterProducts_page.click_product_color_menu()


@when('I select the color White')
def step_impl(context):
    context.searchAndFilterProducts_page.click_color_withe()


@when('I select the product size')
def step_impl(context):
    context.searchAndFilterProducts_page.click_product_size_menu()


@when('I select the size L')
def step_impl(context):
    context.searchAndFilterProducts_page.click_size_l()


@then('The product filter message is "{message}"')
def step_impl(context, message):
    assert message in context.searchAndFilterProducts_page.verify_the_results()


@when('I sort the products by "{value}"')
def step_impl(context, value):
    context.searchAndFilterProducts_page.sort_products_by_price(value)


@then('The products sorting message is "{message}"')
def step_impl(context, message):
    assert message in context.searchAndFilterProducts_page.verify_sorting


@when('I select the group to which the product is addressed')
def step_impl(context):
    context.searchAndFilterProducts_page.group_selection()


@when('I select the product range')
def step_impl(context):
    context.searchAndFilterProducts_page.range_selection()


@when('I click the category button')
def step_impl(context):
    context.searchAndFilterProducts_page.category_selection()


@when('I select pants category')
def step_impl(context):
    context.searchAndFilterProducts_page.pants_category_selection()


@when('I select the product style menu')
def step_impl(context):
    context.searchAndFilterProducts_page.style_menu_selection()


@when('I select the desired style')
def step_impl(context):
    context.searchAndFilterProducts_page.style_selection()


@when('I select the desired product')
def step_impl(context):
    context.searchAndFilterProducts_page.product_selection()


@when('I store the product presentation images')
def step_impl(context):
    context.searchAndFilterProducts_page.store_presentation_images()


@when('I select the size 34')
def step_impl(context):
    context.searchAndFilterProducts_page.size_selection()


@when('I select the color blue')
def step_impl(context):
    context.searchAndFilterProducts_page.color_selection()


@when('I restore the product presentation images')
def step_impl(context):
    context.searchAndFilterProducts_page.restore_presentation_images()


@then('The filtering message is "{message}"')
def step_impl(context, message):
    assert message in context.searchAndFilterProducts_page.verify_page_layout()
