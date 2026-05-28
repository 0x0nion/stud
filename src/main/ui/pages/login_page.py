from playwright.sync_api import Page

from src.main.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        super().__init__(page)
        # self.page = page
        # self.username_input = page.locator("#user-name")
        # self.password_input = page.locator("#password")
        # self.login_btn = page.get_by_role("button", name="Login")
        self.error_msg = page.locator("h3[data-test='error']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def get_error_mgs(self):
        return self.error_msg.inner_text()
