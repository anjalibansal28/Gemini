import helpers.locators as locators
import helpers.credentials as credentials
import time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ClientRegistration:
    def __init__(self):
        #self.driver = driver
        dir_path = os.path.abspath(os.curdir)
        self.driver = webdriver.Chrome(executable_path=dir_path + '\\chromedriver.exe')
        self.driver.maximize_window()

    def get_client_registration_page(self):
        self.driver.get(credentials.sandbox_registration_url)
        self.driver.find_element_by_xpath(locators.create_new_account).click()
        if self.driver.find_element_by_xpath(locators.cookies):
            self.driver.find_element_by_xpath(locators.cookies).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element_by_xpath(locators.create_business_account).click()
        assert self.driver.title == '[Sandbox] Gemini - Institutional Client Registration'

    def set_legal_business_name(self, legal_business_name):
        self.driver.find_element_by_xpath(locators.legal_business_name).send_keys(legal_business_name)

    def set_company_type(self, company_type):
        self.driver.find_element_by_xpath(locators.company_type_dropdown).send_keys(company_type)
        self.driver.find_element_by_xpath(locators.company_type_dropdown).send_keys(Keys.RETURN)

    def set_other_description(self, other_description):
        self.driver.find_element_by_xpath(locators.other_description).send_keys(other_description)

    def set_country_business(self, country_business):
        self.driver.find_element_by_xpath(locators.country_business_dropdown).send_keys(country_business)
        self.driver.find_element_by_xpath(locators.country_business_dropdown).send_keys(Keys.RETURN)

    def set_state_business(self, state_business):
        self.driver.find_element_by_xpath(locators.state).send_keys(state_business)
        self.driver.find_element_by_xpath(locators.state).send_keys(Keys.RETURN)

    def set_legal_first_name(self, legal_first_name):
        self.driver.find_element_by_xpath(locators.legal_first_name).send_keys(legal_first_name)

    def set_legal_middle_name(self, legal_middle_name):
        self.driver.find_element_by_xpath(locators.legal_middle_name).send_keys(legal_middle_name)

    def set_legal_last_name(self, legal_last_name):
        self.driver.find_element_by_xpath(locators.legal_last_name).send_keys(legal_last_name)

    def set_email(self, email):
        self.driver.find_element_by_xpath(locators.email).send_keys(email)

    def click_continue(self):

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element_by_xpath(locators.continue_button).click()

    def set_parameter_form(self, legal_business_name, company_type, other_description='', country_business='',
                           state_business='', legal_first_name='', legal_middle_name='', legal_last_name='',
                           email=''):
        self.get_client_registration_page()
        self.set_legal_business_name(legal_business_name)
        self.set_company_type(company_type)
        if company_type == 'Other':
            self.set_other_description(other_description)
        self.set_country_business(country_business)
        if country_business == 'United States':
            self.set_state_business(state_business)
        self.set_legal_first_name(legal_first_name)
        self.set_legal_middle_name(legal_middle_name)
        self.set_legal_last_name(legal_last_name)
        self.set_email(email)
        self.click_continue()
        time.sleep(2)

    def get_page_text(self):
        body_text = self.driver.find_element_by_tag_name('body').text
        self.close_browser()
        if 'Thanks for Registering' in body_text:
            return True

    def get_error_text(self):
        error_message = ''
        if self.driver.find_element_by_xpath("//div[@class='Alert error']").is_displayed():
            error_message = self.driver.find_element_by_xpath("//div[@class='AlertBody']").text
        time.sleep(2)
        self.close_browser()
        return error_message

    def close_browser(self):
        self.driver.close()
        self.driver.quit()

    def hover_providing_personal_information(self):
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(.,'Why am I providing personal information?')]").click()
        body_text = self.driver.find_element_by_tag_name('body').text
        self.close_browser()
        return body_text
