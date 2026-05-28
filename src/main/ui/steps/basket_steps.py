import allure
from playwright.sync_api import Page

from src.main.ui.pages.basket_page import BasketPage


class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket_page = BasketPage(page)

    @allure.step("Open cart")
    def open_cart(self):
        self.basket_page.open()
        return self

    @allure.step("Check product in cart: {product_name}")
    def expect_item_in_cart(self, product_name: str):
        self.basket_page.expect_item_in_cart(product_name)
        return self

    @allure.step("Check product not in cart: {product_name}")
    def expect_item_not_in_cart(self, product_name: str):
        self.basket_page.expect_item_not_in_cart(product_name)
        return self

    @allure.step("Remove item: {product_name}")
    def remove_item(self, product_name: str):
        self.basket_page.remove_item(product_name)
        return self

    @allure.step("Checkout")
    def checkout(self):
        self.basket_page.checkout()
        return self

    @allure.step("Get products names from cart")
    def get_item_names(self) -> list[str]:
        return self.basket_page.get_item_names()

    @allure.step("Total sum")
    def get_items_total_sum(self) -> float:
        return self.basket_page.get_items_total_price()


