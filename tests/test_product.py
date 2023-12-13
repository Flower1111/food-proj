from pages.base import ProductPage
from utils.utils import expected_filtered_food, expected_product_names, load_json_data

class TestProduct:
    def test_get_product_names(self):
        payload = load_json_data('resources', 'data.json')
        product_page = ProductPage(payload)
        assert product_page.get_product_names() == expected_product_names()

    def test_filter_food_by_price(self):
        payload = load_json_data('resources', 'data.json')
        product_page = ProductPage(payload)
        assert product_page.filter_food_by_price(14.99) == expected_filtered_food()
