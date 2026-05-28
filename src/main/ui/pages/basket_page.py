from playwright.sync_api import Page, expect


class BasketPage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.checkout_btn = page.locator("#checkout")
        self.cart_item = page.locator(".cart_item")
        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator(".inventory_item_price")

    def open(self):
        self.shopping_cart_link.click()

    def get_item_names(self):
        return self.product_name.all_text_contents()

    def get_item_price(self):
        return self.product_price.all_text_contents()

    def expect_item_in_cart(self, product_name: str):
        card = self.page.locator(".inventory_item_name", has_text=product_name)
        expect(card).to_be_visible()

    def expect_item_not_in_cart(self, product_name: str):
        card = self.page.locator(".inventory_item_name", has_text=product_name)
        expect(card).not_to_be_visible()

    def remove_item(self, product_name):
        card = self.cart_item.filter(has_text=product_name)
        card.get_by_role("button", name="Remove").click()

    def get_items_total_price(self):
        prices_text = self.product_price.all_text_contents()
        return sum([float(i.replace("$", "")) for i in prices_text])

    def checkout(self):
        self.checkout_btn.click()