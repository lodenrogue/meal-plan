import math

PIZZA_CALORIES_PER_PIE = 1550
PIZZA_QUANTITY = 0.333333
PIZZA_UNIT_TYPE = 'Containers'

from menu.item_creator import ItemCreator

class LunchMenu():

    def get_menu(self):
        name = 'Pizza'
        quantity = PIZZA_QUANTITY
        unit_type = PIZZA_UNIT_TYPE
        calories = math.ceil(PIZZA_CALORIES_PER_PIE * PIZZA_QUANTITY)

        item = ItemCreator(name, quantity, unit_type, calories).create()
        return [item]