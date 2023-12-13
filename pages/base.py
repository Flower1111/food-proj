class ProductPage:
    def __init__(self, json_data):
        self.products = json_data["products"]

    def get_product_names(self):
        return [product["name"] for product in self.products]
    
    def filter_food_by_price(self, threshold):
        return [product for product in self.products if product["price"] >= threshold]