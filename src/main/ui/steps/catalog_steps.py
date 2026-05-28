import allure
from playwright.sync_api import expect

from src.main.ui.pages.catalog_page import CatalogPage


class CatalogSteps:
    def __init__(self, page):
        self.page = page
        self.catalog_page = CatalogPage(page)

    @allure.step("Log in")
    def login(self, username:str, password: str):
        self.catalog_page.login(username, password)
        return self

    @allure.step("Add product: {product_name}")
    def add_to_cart(self, product_name):
        button = self.catalog_page.add_to_cart(product_name)
        expect(button).to_have_text("Remove")
        return self

    @allure.step("Remove produc: {product_name}t")
    def remove_from_cart(self, product_name):
        button = self.catalog_page.remove_from_cart(product_name)
        expect(button).to_have_text("Add to cart")
        return self

    @allure.step("Sort products: {option}")
    def sort_items(self, option: str):
        self.catalog_page.sort_items(option)
        return self

    @allure.step("Count products")
    def get_products_count(self) -> int:
        return self.catalog_page.get_product_count()

    @allure.step("Get product names")
    def get_product_names(self) -> list[str]:
        return self.catalog_page.get_product_names()

    @allure.step("Get product price")
    def get_product_prices(self) -> list[float]:
        return self.catalog_page.get_product_prices()

    @allure.step("Get cart count")
    def get_cart_count(self) -> int:
        return self.catalog_page.get_cart_count()

    @allure.step("Open detail page: {product_name}")
    def open_product_details(self, product_name: str):
        return self.catalog_page.open_product_details(product_name)

    @allure.step("Logout")
    def logout(self):
        self.catalog_page.logout()
        return self

