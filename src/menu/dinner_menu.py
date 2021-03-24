import math
from menu.item_creator import ItemCreator

CHICKEN_MENU_TYPE = 'chicken'
FISH_AND_CHICKEN_MENU_TYPE = 'fish-chicken'

BEANS_CONCHITA_CALORIES = 0.78
BEANS_CONCHITA_QUANTITY = 200
BEANS_CONCHITA_UNIT_TYPE = 'Grams'

BEANS_GOYA_CALORIES = 0.85
BEANS_GOYA_QUANTITY = 100
BEANS_GOYA_UNIT_TYPE = 'Grams'

BUNS_CALORIES = 130
BUNS_QUANTITY = 1
BUNS_UNIT_TYPE = "Each"

CHICKEN_ROUNDING_FACTOR = 0.05
CHICKEN_CALORIES = 2.34
CHICKEN_UNIT_TYPE = 'Ounces'

FISH_ROUNDING_FACTOR = 0.05
FISH_CALORIES = 1.82
FISH_UNIT_TYPE = 'Ounces'


class DinnerMenu():

    def __init__(self, menu_type):
        self.menu_type = menu_type


    def get_menu(self, calories):
        conchita_beans = self._create_conchita_beans()
        goya_beans = self._create_goya_beans()

        beans_sum = conchita_beans['calories'] + goya_beans['calories']
        main_course_calories = calories - beans_sum

        main_course = []
        
        if self.menu_type == CHICKEN_MENU_TYPE:
            main_course = self._create_chicken_menu(main_course_calories)

        elif self.menu_type == FISH_AND_CHICKEN_MENU_TYPE:
            main_course = self._create_fish_chicken_menu(main_course_calories)

        else:
            print('Invalid menu type: {}'.format(self.menu_type))
            exit(1)

        return main_course + [conchita_beans, goya_beans]


    def _create_fish_chicken_menu(self, calories):
        calories_per_item = math.floor(calories / 2)
        chicken = self._create_chicken(calories_per_item)
        fish = self._create_fish(calories_per_item)

        return [chicken, fish]


    def _create_fish(self, available_calories):
        name = 'Tilapia'
        quantity = math.floor(available_calories / FISH_CALORIES) * FISH_ROUNDING_FACTOR
        unit_type = FISH_UNIT_TYPE
        calories = math.floor(quantity * FISH_CALORIES / FISH_ROUNDING_FACTOR)

        return ItemCreator(name, quantity, unit_type, calories).create()


    def _create_chicken_menu(self, available_calories):
        buns = self._create_buns()

        chicken_available_cals = available_calories - buns['calories']
        chicken = self._create_chicken(chicken_available_cals)

        return [chicken, buns]


    def _create_chicken(self, available_calories):
        name = 'Chicken'
        quantity = math.floor(available_calories / CHICKEN_CALORIES) * CHICKEN_ROUNDING_FACTOR
        unit_type = CHICKEN_UNIT_TYPE
        calories = math.floor(quantity * CHICKEN_CALORIES / CHICKEN_ROUNDING_FACTOR)

        return ItemCreator(name, quantity, unit_type, calories).create()


    def _create_buns(self):
        name = 'Buns'
        quantity = BUNS_QUANTITY
        unit_type = BUNS_UNIT_TYPE
        calories = math.ceil(BUNS_CALORIES * quantity)

        return ItemCreator(name, quantity, unit_type, calories).create()


    def _create_conchita_beans(self):
        name = 'Conchita Beans 2'
        quantity = BEANS_CONCHITA_QUANTITY
        unit_type = BEANS_CONCHITA_UNIT_TYPE
        calories = math.ceil(BEANS_CONCHITA_CALORIES * quantity)

        return ItemCreator(name, quantity, unit_type, calories).create()


    def _create_goya_beans(self):
        name = 'Goya Beans'
        quantity = BEANS_GOYA_QUANTITY
        unit_type = BEANS_GOYA_UNIT_TYPE
        calories = math.ceil(BEANS_GOYA_CALORIES * quantity)

        return ItemCreator(name, quantity, unit_type, calories).create()
