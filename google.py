from selenium import webdriver
from test_base import TestBase
from utils.constants import *
import time
import os

class AutomatedCreateAccount(TestBase):

	def __init__(self):
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_argument("--incognito")
		self.browser = webdriver.Chrome(desired_capabilities = self.chrome_options.to_capabilities(), executable_path=r'./chromedriver.exe')

	def setup(self):
		self.dummy_name = os.environ["DUMMY_NAME"]
		self.dummy_surname = os.environ["DUMMY_SURNAME"]
		self.dummy_mail = os.environ["DUMMY_MAIL"]
		self.dummy_pass = os.environ["DUMMY_PASS"]
		self.dummy_phone_number = os.environ["DUMMY_PHONE_NUMBER"]

	def test(self):
		self.setup()
		try:
			self.open_web_site(TARGET_WEBSITE)
			self.wait_for_element_by_xpath(CREATE_ACCOUNT_BUTTON)
			self.click_create_button()
			time.sleep(0.5)
			self.click_for_me()
			time.sleep(0.5)
			self.wait_for_element_by_xpath(NAME_INPUT)
			self.write_input(NAME_INPUT, self.dummy_name)
			time.sleep(0.2)
			self.write_input(SURNAME_INPUT, self.dummy_surname)
			time.sleep(0.2)
			self.write_input(MAIL_INPUT, self.dummy_mail)
			time.sleep(0.2)
			self.write_input(PASS_INPUT, self.dummy_pass)
			time.sleep(0.2)
			self.write_input(CONFIRM_PASS_INPUT, self.dummy_pass)
			time.sleep(0.2)
			self.click_next_button()
			self.wait_for_element_by_xpath(PHONE_CONFIRMATION_INPUT)
			self.write_input(PHONE_CONFIRMATION_INPUT, self.dummy_phone_number)
			self.click_next_button()
			self.wait_for_element_by_xpath(CODE_WAIT_DISPLAY)
			self.write_google_code()
			self.click_next_button()
			self.wait_for_element_by_xpath(DAY_INPUT)
			self.write_input(DAY_INPUT, "2")
			self.select_month(6)
			self.write_input(YEAR_INPUT, "1998")
			self.select_gender("Masculino")
			self.click_next_button()
			self.wait_for_element_by_xpath(AGREE_WITH_TERMS)
			self.click_agree_checkbox()
			self.create_account_button()
			time.sleep(30)
			
		except Exception as ex:
			print(str(ex))
		finally:
			self.browser.close()



driver = AutomatedCreateAccount()
driver.test()