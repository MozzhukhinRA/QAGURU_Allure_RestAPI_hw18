from dataclasses import dataclass
from itertools import product

from selene import browser, have, be


@dataclass
class AddToCardApi:
    BASE_URL : str = 'https://demowebshop.tricentis.com/'

    def add_to_card_laptop(self, session):
        object_api = 'addproducttocart/catalog/31/1/1'
        response = session.post(self.BASE_URL + object_api)
        return response

    def add_to_card_pc(self, session):
        object_api = 'addproducttocart/catalog/72/1/1'
        option = 'addproducttocart/details/72/1'
        response = session.post(self.BASE_URL + object_api)
        response_option = session.post(self.BASE_URL + option, data={
            'product_attribute_72_5_18': 53,
            'product_attribute_72_6_19': 54,
            'product_attribute_72_3_20': 57,
            'addtocart_72.EnteredQuantity': 1
            }
        )
        return response_option, response

@dataclass
class CheckCardUi:
    BASE_URL : str = 'https://demowebshop.tricentis.com/'

    def open_browser(self):
        browser.open(self.BASE_URL)
        browser.driver.refresh()


    def open_card(self):
        browser.element('#topcartlink').click()

    def assert_product_in_card(self):
        browser.element('[src="https://demowebshop.tricentis.com/content/images/thumbs/0000172_build-your-own-cheap-computer_80.jpeg"]').should(be.visible)

        browser.element('[src="https://demowebshop.tricentis.com/content/images/thumbs/0000224_141-inch-laptop_80.png"]').should(be.visible)

        product = browser.all('.product-name')

        product.should(have.size_greater_than_or_equal(2))

        product.first.should(have.text('Build your own cheap computer'))
        product.second.should(have.text('14.1-inch Laptop'))