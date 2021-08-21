from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from utils.constants import *
from abc import ABC
import random
import urllib.request as request
import json
import os
import time


class TestBase(ABC):

    def wait_for_element_by_xpath(self, selector, timeout=60):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((By.XPATH, selector)))
        except:
            raise Exception("cannot find element")

    def click_create_button(self):
        try:
            self.click(CREATE_ACCOUNT_BUTTON)
        except:
            raise Exception("fail to click")

    def click_for_me(self):
        try:
            self.click(CREATE_ACCOUNT_FOR_ME)
        except:
            raise Exception("fail to click")

    def click_next_button(self):
        try:
            self.click(NEXT_BUTTON)
        except:
            raise Exception("fail to click")
    
    def click_agree_checkbox(self):
        try:
            self.click(AGREE_WITH_TERMS)
        except:
            raise Exception("fail to click")
    
    def create_account_button(self):
        try:
            self.click(NEXT_BUTTON)
        except:
            raise Exception("fail to click")

    def open_web_site(self, website):
        self.browser.get(website)

    def click(self, element):
        self.browser.find_element_by_xpath(element).click()

    def write_input(self, xpath, text):
        try:
            self.browser.find_element_by_xpath(xpath).send_keys(text)
        except:
            raise Exception(f"Fail to write on {xpath}.")
    
    def select_dropdown_by_xpath(self, index):
        try:
            dropdown = Select(self.broser.findElement(By.XPATH(MONTH_INPUT)))
            dropdown.select_by_index(index)
        except:
            raise Exception("cant select value on dropdown")

    def select_dropdown_by_value(self, gender):
        try:
            dropdown = Select(self.broser.findElement(By.XPATH(YEAR_INPUT)))
            dropdown.select_by_value(gender)
        except:
            raise Exception("cant select value on dropdown")

    def select_month(self, month):
        month-=1
        self.select_dropdown_by_xpath(month)
    
    def select_gender(self, gender):
        self.select_dropdown_by_value(gender)

    def read_raw(self, dontpad_url):
        with request.urlopen(dontpad_url + ".body.json?lastUpdate=0") as response:
            resp = response.read()
        return resp

    def read_google_code(self, full_json=False):
        content = json.loads(self.read_raw(os.environ["DONTPAD_URL"]).decode())
        if "body" in content:
            return content["body"] if not full_json else content
        return ""

    def wait_google_code(self):
        g_code = None
        retry = 0
        while not g_code or retry>60:
            g_code = self.read_google_code()
            if isinstance(g_code, str) and "G" in g_code and len(g_code) > 8:
                return g_code
            retry+=1
            time.sleep(1)
            print("not found code")
        raise Exception("Google code not provided")
    
    def write_google_code(self):
        g_code = self.wait_google_code()[2:8]
        self.write_input(CODE_RECEIVED_INPUT, g_code)