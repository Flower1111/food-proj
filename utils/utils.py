import json
import os
import pathlib


PROJECT_ROOT = pathlib.Path(__file__).joinpath('..', '..').resolve()

def load_json_data(*json_relpath):
    with open(os.path.join(PROJECT_ROOT, *json_relpath)) as file:
        return json.load(file)

def expected_product_names():
    product_names = ["Pizza", "Sushi", "Burger", "Pad Thai"]
    return product_names

def expected_filtered_food():
    filtered_food = [
        {"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99},
        {"id": 4, "name": "Pad Thai", "category": "Thai", "price": 14.99},
    ]
    return filtered_food