from booking.booking import Booking
from selenium import webdriver

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="GBP")
    bot.select_place_to_go(place_to_go="New York")
    bot.select_date('2024-08-10','2024-08-18')
