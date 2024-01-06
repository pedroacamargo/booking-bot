from booking.booking import Booking
from selenium import webdriver

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="GBP")