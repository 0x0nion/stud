from src.main.ui.steps.basket_steps import BasketSteps
from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.steps.checkout_steps import CheckoutSteps


def test_add_item_and_check_in_cart(page):
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Onesie")

    basket = BasketSteps(page)
    basket.open_cart()

    basket.expect_item_in_cart("Sauce Labs Onesie")


def test_add_items_and_check_in_cart(page):
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Backpack")
    catalog.add_to_cart("Sauce Labs Fleece Jacket")
    catalog.add_to_cart("Sauce Labs Onesie")

    basket = BasketSteps(page)
    basket.open_cart()

    basket.expect_item_in_cart("Sauce Labs Onesie")
    basket.expect_item_in_cart("Sauce Labs Backpack")
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket")


def test_remove_items(page):
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Backpack")
    catalog.add_to_cart("Sauce Labs Fleece Jacket")
    catalog.add_to_cart("Sauce Labs Onesie")

    basket = BasketSteps(page)
    basket.open_cart()

    basket.remove_item("Sauce Labs Backpack")
    basket.remove_item("Sauce Labs Fleece Jacket")
    basket.remove_item("Sauce Labs Onesie")

    basket.expect_item_not_in_cart("Sauce Labs Backpack")
    basket.expect_item_not_in_cart("Sauce Labs Fleece Jacket")
    basket.expect_item_not_in_cart("Sauce Labs Onesie")


def test_checkout(page):
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")
    catalog.add_to_cart("Sauce Labs Backpack")
    catalog.add_to_cart("Sauce Labs Fleece Jacket")
    catalog.add_to_cart("Sauce Labs Onesie")

    basket = BasketSteps(page)
    basket.open_cart()
    basket.checkout()

    checkout = CheckoutSteps(page)
    checkout.start_checkout(first_name="Name", last_name="Lsat Name", postal_code="93422")
    checkout_total = checkout.get_item_total_after_continue()
    assert checkout_total == basket.get_items_total_sum


def test_checkout_invalid_form_data(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    checkout = CheckoutSteps(page)

    catalog.login("standard_user", "secret_sauce")
    basket.open_cart()
    items = basket.get_item_names()
    assert len(items) == 0, "Empty cart"

    basket.checkout()
    checkout.start_checkout("Kalatushkin","Pushkin", "")

    error_text = checkout.get_error_text()
    assert error_text != "", "Waiting error with empty cart"

