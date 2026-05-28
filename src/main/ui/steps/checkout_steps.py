import allure
from playwright.sync_api import Page

from src.main.ui.pages.checkout_page import CheckoutPage


class CheckoutSteps:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_page = CheckoutPage(page)

    @allure.step("Start checkout: {first_name} {last_name} {postal_code}")
    def start_checkout(self, first_name, last_name, postal_code):
        self.checkout_page.start_checkout(first_name, last_name, postal_code)
        return self

    @allure.step("Finish checkout")
    def finish_checkout(self):
        self.checkout_page.finish_btn()
        return self

    @allure.step("Get error text in checkout")
    def get_error_text(self) -> str:
        return self.checkout_page.get_error_text()

    @allure.step("Get subtotal price")
    def get_item_total_after_continue(self) -> int:
        return self.checkout_page.get_subtotal_price()

