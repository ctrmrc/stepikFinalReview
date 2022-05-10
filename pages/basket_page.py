from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        self.shouldnt_be_any_product_in_a_basket()
        self.should_be_empty_basket_text_on_basket_page()

    def shouldnt_be_any_product_in_a_basket(self):
        substring = BasketPageLocators.SUBSTRING_BASKET_EN_GB
        assert substring in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, "Net texta o pustoy korzine"

    def should_be_empty_basket_text_on_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Korzina ne pusta! Korzina doljna bit pusta!"

    def should_be_not_basket_text_on_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Korzina pusta! Korzina NE doljna bit pusta!"
