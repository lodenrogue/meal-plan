import math
from menu.lunch_menu import LunchMenu
from menu.snack_menu import SnackMenu
from menu.dinner_menu import DinnerMenu

class Menu():

    def __init__(self, calories, menu_type):
        self.calories = int(calories)
        self.menu_type = menu_type

        self.lunch_menu = LunchMenu()
        self.snack_menu = SnackMenu()
        self.dinner_menu = DinnerMenu(menu_type)


    def get_lunch(self):
        return self.lunch_menu.get_menu()


    def get_dinner(self):
        lunch = self.get_lunch()
        snack = self.get_snack()
        available_calories = self.calories - self._add_calories(lunch, snack)

        return self.dinner_menu.get_menu(available_calories)


    def get_snack(self):
        return self.snack_menu.get_menu()


    def _add_calories(self, meal1, meal2):
        meal1_calories = self._get_total_calories(meal1)
        meal2_calories = self._get_total_calories(meal2)
        return meal1_calories + meal2_calories


    def _get_total_calories(self, meal):
        return sum(item['calories'] for item in meal)
