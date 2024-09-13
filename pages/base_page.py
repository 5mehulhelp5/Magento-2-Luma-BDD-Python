import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from driver import Driver


class BasePage(Driver):

    URL = 'https://osc-ultimate-demo.mageplaza.com/'

    def navigate_to_page(self):
        self.driver.get(self.URL)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def action_chain(self, locator):
        button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(button).click(button).perform()

    def type(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator):
        return self.wait_for_element(locator, 10).text

    def scroll_down_page(self):
        for i in range(30):
            self.driver.execute_script(f"window.scrollTo(0, {i * 500});")

    def select_from_dropdown(self, locator, value):
        menu = Select(WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator)))
        menu.select_by_visible_text(value)

    def store_page_layout(self, locator):
        self.scroll_down_page()
        presentation_images = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))
        listed_images = list(presentation_images)
        time.sleep(5)

        return len(listed_images)
