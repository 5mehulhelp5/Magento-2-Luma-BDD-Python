from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from help_selectors.searchAndFilterProductsSelectors import *
from pages.base_page import BasePage
from selenium.common import TimeoutException


class SearchAndFilterProducts(BasePage):

    def click_search_bar(self):
        self.wait_for_element(SEARCH_BAR_SELECTOR, 5).click()

    def search_a_product(self, product):
        self.type(SEARCH_BAR_SELECTOR, product)

    def click_search_button(self):
        self.wait_for_element(SEARCH_BUTTON_SELECTOR, 5).click()

    def verify_total_items_founded(self):
        while True:
            total_items = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(TOTAL_SEARCHED_ITEMS_SELECTOR))
            total_items_founded = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(TOTAL_ITEMS_ON_PAGE_SELECTOR))
            total_items_on_page = self.driver.find_element(*TOTAL_ITEMS_ON_PAGE_SELECTOR)

            try:
                if total_items.text != total_items_on_page.text:
                    self.scroll_down_page()
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(NEXT_PAGE_SELECTOR)).click()
                    self.scroll_down_page()
                else:
                    break

            except TimeoutException:
                break

        assert f'{total_items.text}' in f'{total_items_founded.text}', 'Error, I can not find anything'

        return 'The total item text is equal with the total items founded.'

    def verify_product_not_found(self):
        message_container = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(SEARCH_ERROR_SELECTOR)).text

        assert f'{message_container}' == 'Your search returned no results.\nDid you mean\nbase\nbest', \
            'Error, The message is not the same'

        return 'Your search returned no results.'

    def click_whats_new_menu(self):
        self.wait_for_element(WHAT_IS_NEW_MENU_SELECTOR, 5).click()

    def click_product_category(self):
        self.wait_for_element(PRODUCT_CATEGORY_SELECTOR, 5).click()

    def click_product_color_menu(self):
        self.wait_for_element(PRODUCT_COLOR_SELECTOR, 5).click()

    def click_color_withe(self):
        self.wait_for_element(PRODUCT_COLOR_WHITE_SELECTOR, 5).click()

    def click_product_size_menu(self):
        self.wait_for_element(PRODUCT_SIZE_SELECTOR, 5).click()

    def click_size_l(self):
        self.wait_for_element(PRODUCT_SIZE_L_SELECTOR, 5).click()

    def verify_the_results(self):
        total_items = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(TOTAL_SEARCHED_ITEMS_SELECTOR))
        total_items_founded = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(PRODUCT_ITEM_SELECTOR))

        assert f'{int(total_items.text)}' == f'{len(total_items_founded)}', 'Error, the results don\'t match'

        return 'I found all the products.'

    def sort_products_by_price(self, value):
        self.select_from_dropdown(SORTING_MENU_SELECTOR, value)

    def verify_sorting(self):
        i = 1
        while True:
            try:
                product_price = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located(PRODUCT_PRICE_SELECTOR))
                price_list = []
                self.scroll_down_page()

                for i in range(len(product_price)):
                    current_price = product_price[i].text
                    current_price_without_dollar = current_price.replace('$', '')
                    actual_price = float(current_price_without_dollar)
                    price_list.append(actual_price)

                sorted_price_list = sorted(price_list)

                try:
                    if sorted_price_list == price_list:
                        WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located(NEXT_PAGE_SELECTOR)).click()
                        message = 'The list is sorted'
                    elif sorted_price_list != price_list:
                        message = 'The list is unsorted'
                    else:
                        break

                except TimeoutException:
                    break

            except Exception as e:
                return f'I have encountered a problem {str(e)}'
            i += 1

            assert 'The list is sorted' in message, 'The list is unsorted'

            return 'The list is sorted.'

    def group_selection(self):
        self.wait_for_element(MAN_MENU_SELECTOR, 5).click()

    def range_selection(self):
        self.wait_for_element(MAN_BOTTOMS_MENU_SELECTOR, 5).click()

    def category_selection(self):
        self.wait_for_element(PRODUCT_CATEGORY_1_SELECTOR, 5).click()

    def pants_category_selection(self):
        self.wait_for_element(MAN_PANTS_MENU_SELECTOR, 5).click()

    def style_menu_selection(self):
        self.wait_for_element(PRODUCT_STYLE_SELECTOR, 5).click()

    def style_selection(self):
        self.wait_for_element(PRODUCT_STYLE_SWEATPANTS_SELECTOR, 5).click()

    def product_selection(self):
        self.wait_for_element(PRODUCT_NAME_SELECTOR, 5).click()

    def store_presentation_images(self):
        self.store_page_layout(PRODUCT_PRESENTATION_IMAGES_SELECTOR)

    def size_selection(self):
        self.wait_for_element(PRODUCT_SIZE_34_SELECTOR, 5).click()

    def color_selection(self):
        self.wait_for_element(PRODUCT_COLOR_BLUE_SELECTOR, 5).click()

    def restore_presentation_images(self):
        self.store_page_layout(PRODUCT_PRESENTATION_IMAGES_SELECTOR)

    def verify_page_layout(self):
        assert self.store_presentation_images == self.restore_presentation_images, 'The page was modified.'

        return '{message}'
