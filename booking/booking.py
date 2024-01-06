import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getDate

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


    def clear_cookies(self):
        self.find_element(
            By.ID,
            'onetrust-reject-all-handler'
        ).click()
        
    def clear_popup_sign_up(self):
        self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Dismiss sign-in info."]'
        ).click()


    def land_first_page(self):
        self.get(const.BASE_URL)


    def change_currency(self, currency = "BRL"):
        time.sleep(3)
        self.clear_cookies()
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()
        
        currencies_elements = self.find_elements(
            By.CSS_SELECTOR,
            'button[data-testid="selection-item"]'
        )
        time.sleep(2)

        if currency != None:            
            for e in currencies_elements:
                text = e.text.split("\n")
                if len(text) == 2:
                    if text[1] == currency:
                        e.click()
                        break;


    def select_place_to_go(self, place_to_go):
        time.sleep(3)
        self.clear_popup_sign_up()
        time.sleep(3)
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        
        time.sleep(2)
        first_result = self.find_element(
            By.XPATH,
            '/html/body/div[3]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/ul/li[1]/div'
        )
        first_result.click()
        print("Clicked successfully")


    def select_date(self, check_in_date, check_out_date):
        iterations = getDate.get_iterations_to_right(check_in_date)
        first = True
        print(iterations)
        while iterations > 0:
            if first:
                arrow_element = self.find_element(
                    By.XPATH,
                    '/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button'
                )
                first = False
            else:
                arrow_element = self.find_element(
                    By.XPATH,
                    '/html/body/div[3]/div[2]/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/button[2]'
                )
            
            arrow_element.click()
            iterations -= 1
        
        time.sleep(1)
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        time.sleep(2)
        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

