import pytest
from helpers.clientregistration import ClientRegistration
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")
def initialize_client_registration_module(request):
    registration = ClientRegistration()
    request.cls.registration = registration


@pytest.mark.usefixtures("initialize_client_registration_module")
class Test_ClientRegistration:

    def test_submit_empty_form(self):
        try:
            self.registration.get_client_registration_page()
            self.registration.click_continue()
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Legal Business Name is required' in registration_result
        assert 'Company type is required' in registration_result
        assert 'First name is required' in registration_result
        assert 'Last name is required' in registration_result
        assert 'valid email address' in registration_result
        assert 'Company state is required' in registration_result

    def test_empty_legal_business_name(self):
        try:
            self.registration.set_parameter_form(legal_business_name='', company_type='Operating Company',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_middle_name='TestLMN',
                                                 legal_last_name='TestLLN', email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'
        assert 'Legal Business Name is required' in registration_result

    def test_enter_space_legal_business_name(self):
        try:
            self.registration.set_parameter_form(legal_business_name=Keys.SPACE, company_type='Operating Company',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_middle_name='TestLMN',
                                                 legal_last_name='TestLLN', email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Legal Business Name is required' in registration_result

    def test_company_type_other_description_empty(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Other',
                                                 other_description='', country_business='Australia',
                                                 legal_first_name='TestLFN', legal_last_name='TestLLN',
                                                 email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Description is required' in registration_result

    def test_company_type_other_enter_space(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Other',
                                                 other_description=Keys.SPACE, country_business='Australia',
                                                 legal_first_name='TestLFN', legal_last_name='TestLLN',
                                                 email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Other description is required' in registration_result

    def test_company_state_empty(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Operating Company',
                                                 country_business='United States', state_business='',
                                                 legal_first_name='TestLFN', legal_last_name='TestLLN',
                                                 email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Company state is required' in registration_result

    def test_empty_legal_first_name(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Operating Company',
                                                 country_business='Australia', legal_first_name='',
                                                 legal_middle_name='TestLMN',
                                                 legal_last_name='TestLLN', email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'
        assert 'First name is required' in registration_result

    def test_enter_space_legal_first_name(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Operating Company',
                                                 country_business='Australia', legal_first_name=Keys.SPACE,
                                                 legal_middle_name='TestLMN',
                                                 legal_last_name='TestLLN', email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Legal First Name is required' in registration_result

    def test_empty_legal_last_name(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Operating Company',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_middle_name='TestLMN',
                                                 legal_last_name='', email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'
        assert 'Last name is required' in registration_result

    def test_enter_space_legal_last_name(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Operating Company',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_middle_name='TestLMN',
                                                 legal_last_name=Keys.SPACE, email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Legal Last Name is required' in registration_result

    def test_verify_email_input_dot(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Broker-Dealer',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_last_name='TestLLN', email='.')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'specify a valid email domain' in registration_result

    def test_verify_email_input_dot_subdomain(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Broker-Dealer',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_last_name='TestLLN', email='@gmail.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'specify a valid email domain' in registration_result

    def test_verify_email_input_numbers(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Broker-Dealer',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_last_name='TestLLN', email='435353543')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'specify a valid email domain' in registration_result

    def test_verify_email_input_domain_numbers(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Broker-Dealer',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_last_name='TestLLN', email='email@123.123.123.123')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'valid email address' in registration_result

    def test_verify_email_input_missing_ampersat(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Broker-Dealer',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_last_name='TestLLN', email='emailgmail.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'valid email domain' in registration_result

    def test_verify_email_input_missing_topdomain(self):
        try:
            self.registration.set_parameter_form(legal_business_name='Testing_CT', company_type='Broker-Dealer',
                                                 country_business='Australia', legal_first_name='TestLFN',
                                                 legal_last_name='TestLLN', email='email@gmail')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'valid email domain' in registration_result

    def test_verify_multiple_parameters_error_display(self):
        try:
            self.registration.set_parameter_form(legal_business_name=Keys.SPACE, company_type='Operating Company',
                                                 country_business='Australia', legal_first_name=Keys.SPACE,
                                                 legal_last_name=Keys.SPACE, email='pilkid@mailpoof.com')
            registration_result = self.registration.get_error_text()
        except:
            assert False, 'Test Failed to throw error'

        assert 'Legal Business Name is required' in registration_result
        assert 'Legal First Name is required' in registration_result
        assert 'Legal Last Name is required' in registration_result
