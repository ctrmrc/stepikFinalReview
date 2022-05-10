# stepikFinalReview
Python 3.10.1

Если не запускается и выдает ошибку ImportError: attempted relative import with no known parent package
ТО нужно убрать . (точку) в тестах

Тоесть:

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

Заменить на:

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.locators import LoginPageLocators
from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
