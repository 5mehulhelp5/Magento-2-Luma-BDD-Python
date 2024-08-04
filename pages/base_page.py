from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver import Driver

class BasePage(Driver):

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator):
        return self.wait_for_element(locator, 10).text

    def change_to_faceboock_window(self):
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if ("https://www.facebook.com/login.php?skip_api_login=1&api_key=744024889374221&kid_directed_site=0&app_id=744024889374221&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D744024889374221%26redirect_uri%3Dhttps%253A%252F%252Fosc-ultimate-demo.mageplaza.com%252Fsociallogin%252Fsocial%252Fcallback%252F%253Fhauth_done%253DFacebook%26scope%3Demail%252C%2Bpublic_profile%26state%3DHA-TWB70L86ASUXRNM4ZYDFGK3PCQ5J2HV9OEI1%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7fd97cdf-3833-49a9-85eb-f22a7d66db6b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fosc-ultimate-demo.mageplaza.com%2Fsociallogin%2Fsocial%2Fcallback%2F%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-TWB70L86ASUXRNM4ZYDFGK3PCQ5J2HV9OEI1%23_%3D_&display=page&locale=en_US&pl_dbl=0" in url):
                self.driver.switch_to.window(currentWindow)
                break

    def change_to_linkedin_window(self):
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if ('https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=86n928xh7uro9z&redirect_uri=https%3A%2F%2Fosc-ultimate-demo.mageplaza.com%2Fsociallogin%2Fsocial%2Fcallback%2F%3Fhauth.done%3DLinkedIn&scope=r_liteprofile+r_emailaddress&state=HA-5O0FMR9H2QZYS4UXA8LNW1ITG6V37PCKJBED' in url):
                self.driver.switch_to.window(currentWindow)
                break

    def change_to_yahoo_window(self):
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if ('https://login.yahoo.com/?src=oauth&client_id=dj0yJmk9dXZGSk1oUzhLdHJKJmQ9WVdrOWFWbDNNMU5VTmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTk4&crumb=&redirect_uri=https%3A%2F%2Fosc-ultimate-demo.mageplaza.com%2Fsociallogin%2Fsocial%2Fcallback%2F&done=https%3A%2F%2Fapi.login.yahoo.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9dXZGSk1oUzhLdHJKJmQ9WVdrOWFWbDNNMU5VTmpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTk4%26redirect_uri%3Dhttps%253A%252F%252Fosc-ultimate-demo.mageplaza.com%252Fsociallogin%252Fsocial%252Fcallback%252F%26response_type%3Dcode%26scope%3Dprofile%26state%3DHA-OGZC3P80SB6ALKFDW9M7Q5TJ2REY1NX4IHUV' in url):
                self.driver.switch_to.window(currentWindow)
                break

    def change_to_github_window(self):
        for currentWindow in self.driver.window_handles:
            self.driver.switch_to.window(currentWindow)
            url = self.driver.current_url
            if ('https://github.com/login?client_id=040e38eb71b7778fd9f8&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D040e38eb71b7778fd9f8%26redirect_uri%3Dhttps%253A%252F%252Fosc-ultimate-demo.mageplaza.com%252Fsociallogin%252Fsocial%252Fcallback%252F%253Fhauth.done%253DGithub%26response_type%3Dcode%26scope%3Duser%253Aemail%26state%3DHA-3AI1QKYOC09BNSHLXFZJGM8P25DRWE674UVT' in url):
                login_page = self.driver.switch_to.window(currentWindow)
                break

    def change_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def scroll_down_page(self):
        for i in range(30):
            self.driver.execute_script(f"window.scrollTo(0, {i * 500});")

    def accept_cookies(self, locator):
        accept_cookies = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(accept_cookies).click(accept_cookies).perform()