import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, menu_file_path: str) -> None:
        dish_collection = {}
        with open(menu_file_path, encoding="UTF-8") as menu_file:
            menu_data = csv.DictReader(menu_file)
            for row in menu_data:
                dish_title = row["dish"]
                dish_price = float(row["price"])
                dish_ingredient = row["ingredient"]
                ingredient_quantity = int(row["recipe_amount"])

                if dish_title not in dish_collection:
                    dish_collection[dish_title] = Dish(dish_title, dish_price)

                dish_collection[dish_title].add_ingredient_dependency(
                    Ingredient(dish_ingredient), ingredient_quantity
                )

        self.dishes = set(dish_collection.values())
