from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.steps.login_steps import LoginSteps
from src.main.ui.utils.constants import Urls


def test_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("standard_user", "secret_sauce")
    catalog = CatalogPage(page)
    assert catalog.get_product_count() > 0, "Waiting products"


def test_auth_invalid(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user", "secret_sauce")
    error = steps.get_error_text()
    assert "locked out" in error, "Wait block message"


def test_logout(page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)

    login.open_login_page().login("standard_user","secret_sauce")
    assert catalog.get_products_count() > 0, "Waiting products"

    catalog.logout()
    assert page.url == Urls.BASE, "Wait login page"


def test_logout_visual_user(page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)

    login.open_login_page().login("visual_user", "secret_sauce")
    assert catalog.get_products_count() > 0, "Wait products"

    catalog.logout()
    assert page.url == Urls.BASE, "Waiting login_page"

