import allure
import pytest
import requests
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config_open():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options



@pytest.fixture(scope='session')
def auth_session():
    LOGIN = 'roma.moz@mail.ru'
    PASSWORD = '5101po'
    BASE_URL = 'https://demowebshop.tricentis.com/'
    session = requests.Session()
    with allure.step('Авторизация в интернет магазине'):
        auth_response = session.post(
            url=BASE_URL + 'login',
            data={'Email': LOGIN, 'Password': PASSWORD, 'RememberMe': False},
            allow_redirects=False
        )

    return session

