from Lesson6.HW6.tests.base_test import BaseTest


class TestTotalAmount(BaseTest):

    def test_checkout_total(self):
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")

        self.inventory_page.add_products_to_cart()
        self.inventory_page.go_to_cart()

        self.cart_page.proceed_to_checkout()

        self.checkout_page.fill_checkout_form("Pavel", "Durov", "12345")

        assert self.checkout_page.get_total_amount() == "Total: $58.29"
        # assert "$58.29" in self.checkout_page.get_total_amount()
