from dataclasses import dataclass

import requests
from selene import browser, have, be


@dataclass
class AddToCardApi:
    BASE_URL : str = 'https://demowebshop.tricentis.com/'

    def add_to_card_laptop(self):
        object_api = 'addproducttocart/catalog/31/1/1'
        request = requests.post(self.BASE_URL + object_api)
        print(request.text)
        print(request.cookies)

    def add_to_card_pc(self):
        object_api = 'addproducttocart/catalog/72/1/1'
        option = 'addproducttocart/details/72/1'
        request = requests.post(self.BASE_URL + object_api)
        request_option = requests.post(self.BASE_URL + option, data={
            'product_attribute_72_5_18': 53,
            'product_attribute_72_6_19': 54,
            'product_attribute_72_3_20': 57,
            'addtocart_72.EnteredQuantity': 1
            }
        )
        print(request.text)
        print(request_option.text)
        print(request.cookies)


@dataclass
class CheckCardUi:
    BASE_URL : str = 'https://demowebshop.tricentis.com/'

    def open_browser(self):
        browser.open(self.BASE_URL)


    def open_card(self):
        browser.element('.cart-label').click()

    def assert_product_in_card(self):
        browser.element('[src="https://demowebshop.tricentis.com/content/images/thumbs/0000172_build-your-own-cheap-computer_80.jpeg"]').should(be.visible)
        browser.element('.product-name').should(have.text('Build your own cheap computer'))

z = AddToCardApi()
z.add_to_card_pc()