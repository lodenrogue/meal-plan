import math
from menu.item_creator import ItemCreator

BANANA_CALORIES = 121
BANANA_QUANTITY = 1
BANANA_UNIT_TYPE = 'Each'

ORANGE_CALORIES = 61.5
ORANGE_QUANTITY = 2
ORANGE_UNIT_TYPE = 'Each'

class SnackMenu():

    def get_menu(self):
        return [self._create_banana(), self._create_orange()]


    def _create_banana(self):
        name = 'Banana'
        quantity = BANANA_QUANTITY
        unit_type = BANANA_UNIT_TYPE
        calories = math.ceil(BANANA_CALORIES * BANANA_QUANTITY)

        return ItemCreator(name, quantity, unit_type, calories).create()


    def _create_orange(self):
        name = 'Orange'
        quantity = 2
        unit_type = ORANGE_UNIT_TYPE
        calories = math.ceil(ORANGE_CALORIES * quantity)

        return ItemCreator(name, quantity, unit_type, calories).create()
