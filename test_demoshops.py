from resource import AddToCardApi, CheckCardUi

assert_add_product = AddToCardApi()
assert_check_card = CheckCardUi()

class TestSuit:

    def test_open_browser(self):
        assert_check_card.open_browser()

    def test_add_product(self):
        assert_add_product.add_to_card_pc()
        assert_add_product.add_to_card_laptop()

    def test_check_card(self):
        assert_check_card.open_browser()
        assert_check_card.open_card()
        assert_check_card.assert_product_in_card()