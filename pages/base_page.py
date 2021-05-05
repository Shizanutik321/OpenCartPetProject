from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=12):
        self.browser = browser
        self.url = url
        self.browser.implicity_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_contact_us_page_from_header(self):
        contact_us = self.browser.find_element(*BasePageLocators.CONTACT_US_BUTTON)
        contact_us.click()

    def go_to_register_page_from_header(self):
        account_dropdown = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_BUTTON_DROPDOWN)
        account_dropdown.click()
        register = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_REGISTER_BUTTON)

    def go_to_login_page_from_header(self):
        account_dropdown = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_BUTTON_DROPDOWN)
        account_dropdown.click()
        register = self.browser.find_element(*BasePageLocators.MY_ACCOUNT_LOGIN_BUTTON)

    # Only for authorized user! Otherwise redirect to login page!
    def go_to_wishlist_page_from_header(self):
        wishlist = self.browser.find_element(*BasePageLocators.WISH_LIST_BUTTON)
        wishlist.click()

    def go_to_cart_page_from_header(self):
        cart = self.browser.find_element(*BasePageLocators.CART_ICON_BUTTON)
        cart.click()

    # Only when there is some product in the cart! Otherwise redirect to cart!
    def go_to_checkout_page_from_header(self):
        checkout = self.browser.find_element(*BasePageLocators.CHECKOUT_BUTTON)
        checkout.click()
