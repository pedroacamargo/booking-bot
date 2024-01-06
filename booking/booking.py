import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = os.pathsep + r"/home/camargo/SeleniumDrivers/chrome-linux64"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()
        
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if const.SHUT_DOWN_MODE:
            self.close()
            self.quit()
        else:
            print(f"Shut down mode is {const.SHUT_DOWN_MODE}, therefore the tab won't close.")    


    def land_first_page(self):
        self.get(const.BASE_URL)


    def change_currency(self, currency = "BRL"):
        time.sleep(3)
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()
        
        currencies_elements = self.find_elements(
            By.CSS_SELECTOR,
            'button[data-testid="selection-item"]'
        )
        # time.sleep(2)
        # currencies = [e.text.split("\n") for e in currencies_elements]
        # cleaned_data = [item[1] for item in currencies if item != [''] and len(item) == 2]
        # ERROR = 7 # the error in currencies array (start at index 7)
        print("DEBUGG")
        if currency != None:            
            for e in currencies_elements:
                text = e.text.split("\n")
                print(text)
                if len(text) == 2:
                    if text[1] == currency:
                        e.click()
                        break;
