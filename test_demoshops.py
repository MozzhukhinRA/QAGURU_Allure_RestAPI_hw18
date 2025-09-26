import allure
from allure_commons.types import AttachmentType
from selene import browser

from conftest import auth_session
from resource import AddToCardApi, CheckCardUi

assert_add_product = AddToCardApi()
assert_check_card = CheckCardUi()

@allure.title('Тестовый сценарий')
@allure.feature('API + UI test')
@allure.tag('api','ui')
@allure.story('API авторизация с добавлением товара в корзину и последующей проверкой через UI тесты')
@allure.severity(allure.severity_level.BLOCKER)
class TestSuit1:

    with allure.step('Добавление персонального компьютера и ноутбука через API'):
        def test_api(self, auth_session):
            api_pc_response, api_pc_option_response = assert_add_product.add_to_card_pc(auth_session)
            api_laptop_response = assert_add_product.add_to_card_laptop(auth_session)

            assert api_pc_response.status_code == 200
            assert api_pc_option_response.status_code == 200
            assert api_laptop_response.status_code == 200

            allure.attach(str(api_pc_response.status_code), name="Status method open page PC", attachment_type=AttachmentType.TEXT)
            allure.attach(str(api_pc_response.cookies), name="Cookies method open page PC", attachment_type=AttachmentType.TEXT)
            allure.attach(str(api_pc_option_response.status_code), name="Status method add to card PC", attachment_type=AttachmentType.TEXT)
            allure.attach(str(api_pc_option_response.cookies), name="Cookies method add to card PC", attachment_type=AttachmentType.TEXT)
            allure.attach(str(api_laptop_response.status_code), name="Status method add ro card laptop", attachment_type=AttachmentType.TEXT)
            allure.attach(str(api_laptop_response.cookies), name="Cookies method add ro card laptop", attachment_type=AttachmentType.TEXT)

            browser.open('https://demowebshop.tricentis.com/')

            for cookie in auth_session.cookies:
                browser.driver.add_cookie({
                    'name': cookie.name,
                    'value': cookie.value,
                    'domain': cookie.domain
                })
    with allure.step('Проверка корзины через UI, на наличие продуктов (ноутбук и пк'):
        def test_ui(self, auth_session):
            ui = CheckCardUi()
            ui.open_browser()
            ui.open_card()
            ui.assert_product_in_card()
