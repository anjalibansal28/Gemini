import os, time
import pytest
from helpers.clientregistration import ClientRegistration
from selenium import webdriver


@pytest.fixture(scope="function")
def initialize_client_registration_module(request):
    registration = ClientRegistration()
    request.cls.registration = registration


@pytest.mark.usefixtures("initialize_client_registration_module")
class Test_ClientRegistration:

    def test_valid_data_all_fields(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Operating Company',
                                            country_business='Australia', legal_first_name='TestLFN', legal_middle_name='TestLMN',
                                            legal_last_name='TestLLN', email='pilkid@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_company_type_other(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Other',
                                            other_description='Testing_Other', country_business='Australia',
                                            legal_first_name='TestLFN', legal_last_name='TestLLN',
                                            email='pilkid@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_country_buisness_US(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Non-Profit Organization',
                                            country_business='United States', state_business='TX',
                                            legal_first_name='TestLFN', legal_last_name='TestLLN',
                                            email='pilkid@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_special_characters_all_input_parameters(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Test_!@#$',
                                                 company_type='Non-Profit Organization',
                                                 country_business='United States', state_business='TX',
                                                 legal_first_name='Test_&*()', legal_last_name='Test_%^&*',
                                                 email='pilkid@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_numeric_all_input_parameters(self):
        try:
            self.registration.set_parameter_form(legal_business_name='123456',
                                                 company_type='Non-Profit Organization',
                                                 country_business='United States', state_business='TX',
                                                 legal_first_name='456789', legal_last_name='234567',
                                                 email='pilkid@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_large_data_all_input_parameters(self):
        try:
            self.registration.set_parameter_form(
                legal_business_name='Test_123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789',
                company_type='Non-Profit Organization',
                country_business='United States', state_business='TX',
                legal_first_name='Test_123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789',
                legal_last_name='Test_123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789',
                email='pilkid@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_1character_all_input_parameters(self):
        try:
            self.registration.set_parameter_form(legal_business_name='T', company_type='Non-Profit Organization',
                                                 country_business='United States', state_business='TX',
                                                 legal_first_name='T', legal_last_name='T', email='pilkid@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_email_alphanumeric(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT',
                                                 company_type='Non-Profit Organization',
                                                 country_business='United States', state_business='TX',
                                                 legal_first_name='TestLFN', legal_last_name='TestLLN',
                                                 email='pil123456@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_email_underscore(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT',
                                                 company_type='Non-Profit Organization',
                                                 country_business='United States', state_business='TX',
                                                 legal_first_name='TestLFN', legal_last_name='TestLLN',
                                                 email='pil_123456@mailpoof.com')
            registration_result = self.registration.get_page_text()
        except:
            assert False, 'Test Failed to complete registration successfully'
        if registration_result:
            assert True, 'Test Passed'

    def test_hover_personal_information_text(self):
        try:
            self.registration.get_client_registration_page()
            personal_information_text = self.registration.hover_providing_personal_information()
        except:
            assert False, 'Test Failed to provide personal information'

        if 'KYC protocol' in personal_information_text:
            assert True, 'Test Passed'
