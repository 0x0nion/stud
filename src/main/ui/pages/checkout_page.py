from playwright.sync_api import Page, expect

from src.main.ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_btn = page.get_by_role("button", name="continue")
        self.subtotal = page.locator(".summary_subtotal_label")
        self.finish_btn = page.locator("#finish")
        self.complete_result = page.locator(".complete-header")
        self.text_error = page.locator("[data-test='error']")

    def start_checkout(self,first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_btn.click()

    def get_subtotal_price(self):
        return float(self.subtotal.inner_text().split("$")[1])

    def expect_finish_checkout(self):
        self.finish_btn.click()
        expect(self.complete_result).to_have_text("Thank you for your order!")

    def get_error_text(self) -> str:
        return self.text_error.inner_text()