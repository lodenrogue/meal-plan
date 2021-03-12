import sys
import math

from rich.console import Console
from rich.table import Table


CHICKEN_MENU_TYPE = 'chicken'
FISH_AND_CHICKEN_MENU_TYPE = 'fish-chicken'

PIZZA_CALORIES_PER_PIE = 1550
PIZZA_QUANTITY = 0.333333
PIZZA_UNIT_TYPE = 'Containers'

BANANA_CALORIES = 121
BANANA_QUANTITY = 1
BANANA_UNIT_TYPE = 'Each'

ORANGE_CALORIES = 61.5
ORANGE_QUANTITY = 2
ORANGE_UNIT_TYPE = 'Each'

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


def run(calories, menu_type):
	lunch = get_lunch()
	snack = get_snack()

	available_calories = int(calories) - add_calories(lunch, snack)
	dinner = get_dinner(available_calories, menu_type)

	display(lunch, dinner, snack)


def display(lunch, dinner, snack):
	lunch_table = create_table('Lunch', lunch)
	dinner_table = create_table('Dinner', dinner)
	snack_table = create_table('Snacks', snack)

	lunch_total_cals = get_total_calories(lunch)
	dinner_total_cals = get_total_calories(dinner)
	snack_total_cals = get_total_calories(snack)

	console = Console()
	console.print(lunch_table)
	console.print(dinner_table)
	console.print(snack_table)


def create_table(name, meal):
	table = Table(title=name, show_lines=True)

	table.add_column('Name', style='cyan', no_wrap=True, width=17)
	table.add_column('Quantity', justify='right', no_wrap=True, width=10)
	table.add_column('Units', justify='right', no_wrap=True, width=10)
	table.add_column('Calories', justify='right', style='green', no_wrap=True, width=10)

	for item in meal:
		name = item['name']
		quantity = '{:.2f}'.format(item['quantity'])
		units = item['unit_type']
		calories = str(item['calories'])

		table.add_row(name, quantity, units, calories)

	return table


def get_dinner(available_calories, menu_type):
	conchita_beans = create_conchita_beans()
	goya_beans = create_goya_beans()

	beans_sum = conchita_beans['calories'] + goya_beans['calories']
	main_course_avaliable_cals = available_calories - beans_sum

	main_course = []
	
	if menu_type == CHICKEN_MENU_TYPE:
		main_course = create_chicken_menu(main_course_avaliable_cals)

	elif menu_type == FISH_AND_CHICKEN_MENU_TYPE:
		main_course = create_fish_chicken_menu(main_course_avaliable_cals)

	else:
		print('Invalid menu type: {}'.format(menu_type))
		exit(1)

	return main_course + [conchita_beans, goya_beans]


def create_fish_chicken_menu(available_calories):
	calories_per_item = math.floor(available_calories / 2)
	chicken = create_chicken(calories_per_item)
	fish = create_fish(calories_per_item)

	return [chicken, fish]


def create_fish(available_calories):
	name = 'Tilapia'
	quantity = math.floor(available_calories / FISH_CALORIES) * FISH_ROUNDING_FACTOR
	unit_type = FISH_UNIT_TYPE
	calories = math.floor(quantity * FISH_CALORIES / FISH_ROUNDING_FACTOR)

	return create_item(name, quantity, unit_type, calories)


def create_chicken_menu(available_calories):
	buns = create_buns()

	chicken_available_cals = available_calories - buns['calories']
	chicken = create_chicken(chicken_available_cals)

	return [chicken, buns]


def create_chicken(available_calories):
	name = 'Chicken'
	quantity = math.floor(available_calories / CHICKEN_CALORIES) * CHICKEN_ROUNDING_FACTOR
	unit_type = CHICKEN_UNIT_TYPE
	calories = math.floor(quantity * CHICKEN_CALORIES / CHICKEN_ROUNDING_FACTOR)

	return create_item(name, quantity, unit_type, calories)


def create_buns():
	name = 'Buns'
	quantity = BUNS_QUANTITY
	unit_type = BUNS_UNIT_TYPE
	calories = math.ceil(BUNS_CALORIES * quantity)

	return create_item(name, quantity, unit_type, calories)


def create_goya_beans():
	name = 'Goya Beans'
	quantity = BEANS_GOYA_QUANTITY
	unit_type = BEANS_GOYA_UNIT_TYPE
	calories = math.ceil(BEANS_GOYA_CALORIES * quantity)

	return create_item(name, quantity, unit_type, calories)


def create_conchita_beans():
	name = 'Conchita Beans 2'
	quantity = BEANS_CONCHITA_QUANTITY
	unit_type = BEANS_CONCHITA_UNIT_TYPE
	calories = math.ceil(BEANS_CONCHITA_CALORIES * quantity)

	return create_item(name, quantity, unit_type, calories)


def add_calories(meal1, meal2):
	meal1_calories = get_total_calories(meal1)
	meal2_calories = get_total_calories(meal2)
	return meal1_calories + meal2_calories


def get_total_calories(meal):
	return sum(item['calories'] for item in meal)

def get_snack():
	return [create_banana(), create_orange()]


def create_orange():
	orange_name = 'Orange'
	orange_quantity = 2
	orange_unit_type = ORANGE_UNIT_TYPE
	orange_calories = math.ceil(ORANGE_CALORIES * orange_quantity)

	return create_item(orange_name, orange_quantity, orange_unit_type, orange_calories)


def create_banana():
	banana_name = 'Banana'
	banana_quantity = BANANA_QUANTITY
	banana_unit_type = BANANA_UNIT_TYPE
	banana_calories = math.ceil(BANANA_CALORIES * BANANA_QUANTITY)

	return create_item(banana_name, banana_quantity, banana_unit_type, banana_calories)


def get_lunch():
	name = 'Pizza'
	quantity = PIZZA_QUANTITY
	unit_type = PIZZA_UNIT_TYPE
	calories = math.ceil(PIZZA_CALORIES_PER_PIE * PIZZA_QUANTITY)

	return [create_item(name, quantity, unit_type, calories)]


def create_item(name, quantity, unit_type, calories):
	return {
		'name': name,
		'quantity': quantity,
		'unit_type': unit_type, 
		'calories': calories
	}


if __name__ == '__main__':
	calories = sys.argv[1]
	menu_type = sys.argv[2]
	run(calories, menu_type)
