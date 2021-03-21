import math

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

CHICKEN_MENU_TYPE = 'chicken'
FISH_AND_CHICKEN_MENU_TYPE = 'fish-chicken'

BUNS_CALORIES = 130
BUNS_QUANTITY = 1
BUNS_UNIT_TYPE = "Each"

CHICKEN_ROUNDING_FACTOR = 0.05
CHICKEN_CALORIES = 2.34
CHICKEN_UNIT_TYPE = 'Ounces'

FISH_ROUNDING_FACTOR = 0.05
FISH_CALORIES = 1.82
FISH_UNIT_TYPE = 'Ounces'

class Menu():

	def __init__(self, calories, menu_type):
		self.calories = int(calories)
		self.menu_type = menu_type


	def get_lunch(self):
		name = 'Pizza'
		quantity = PIZZA_QUANTITY
		unit_type = PIZZA_UNIT_TYPE
		calories = math.ceil(PIZZA_CALORIES_PER_PIE * PIZZA_QUANTITY)

		return [self._create_item(name, quantity, unit_type, calories)]


	def get_dinner(self):
		lunch = self.get_lunch()
		snack = self.get_snack()
		available_calories = self.calories - self._add_calories(lunch, snack)

		conchita_beans = self._create_conchita_beans()
		goya_beans = self._create_goya_beans()

		beans_sum = conchita_beans['calories'] + goya_beans['calories']
		main_course_avaliable_cals = available_calories - beans_sum

		main_course = []
		
		if self.menu_type == CHICKEN_MENU_TYPE:
			main_course = self._create_chicken_menu(main_course_avaliable_cals)

		elif self.menu_type == FISH_AND_CHICKEN_MENU_TYPE:
			main_course = self._create_fish_chicken_menu(main_course_avaliable_cals)

		else:
			print('Invalid menu type: {}'.format(self.menu_type))
			exit(1)

		return main_course + [conchita_beans, goya_beans]


	def get_snack(self):
		return [self._create_banana(), self._create_orange()]


	def _create_fish_chicken_menu(self, available_calories):
		calories_per_item = math.floor(available_calories / 2)
		chicken = self._create_chicken(calories_per_item)
		fish = self._create_fish(calories_per_item)

		return [chicken, fish]

	def _create_fish(self, available_calories):
		name = 'Tilapia'
		quantity = math.floor(available_calories / FISH_CALORIES) * FISH_ROUNDING_FACTOR
		unit_type = FISH_UNIT_TYPE
		calories = math.floor(quantity * FISH_CALORIES / FISH_ROUNDING_FACTOR)

		return self._create_item(name, quantity, unit_type, calories)


	def _create_chicken_menu(self, available_calories):
		buns = self._create_buns()

		chicken_available_cals = available_calories - buns['calories']
		chicken = self._create_chicken(chicken_available_cals)

		return [chicken, buns]


	def _create_buns(self):
		name = 'Buns'
		quantity = BUNS_QUANTITY
		unit_type = BUNS_UNIT_TYPE
		calories = math.ceil(BUNS_CALORIES * quantity)

		return self._create_item(name, quantity, unit_type, calories)


	def _create_chicken(self, available_calories):
		name = 'Chicken'
		quantity = math.floor(available_calories / CHICKEN_CALORIES) * CHICKEN_ROUNDING_FACTOR
		unit_type = CHICKEN_UNIT_TYPE
		calories = math.floor(quantity * CHICKEN_CALORIES / CHICKEN_ROUNDING_FACTOR)

		return self._create_item(name, quantity, unit_type, calories)

	def _create_conchita_beans(self):
		name = 'Conchita Beans 2'
		quantity = BEANS_CONCHITA_QUANTITY
		unit_type = BEANS_CONCHITA_UNIT_TYPE
		calories = math.ceil(BEANS_CONCHITA_CALORIES * quantity)

		return self._create_item(name, quantity, unit_type, calories)


	def _create_goya_beans(self):
		name = 'Goya Beans'
		quantity = BEANS_GOYA_QUANTITY
		unit_type = BEANS_GOYA_UNIT_TYPE
		calories = math.ceil(BEANS_GOYA_CALORIES * quantity)

		return self._create_item(name, quantity, unit_type, calories)


	def _add_calories(self, meal1, meal2):
		meal1_calories = self._get_total_calories(meal1)
		meal2_calories = self._get_total_calories(meal2)
		return meal1_calories + meal2_calories


	def _get_total_calories(self, meal):
		return sum(item['calories'] for item in meal)


	def _create_orange(self):
		orange_name = 'Orange'
		orange_quantity = 2
		orange_unit_type = ORANGE_UNIT_TYPE
		orange_calories = math.ceil(ORANGE_CALORIES * orange_quantity)

		return self._create_item(orange_name, orange_quantity, orange_unit_type, orange_calories)


	def _create_banana(self):
		banana_name = 'Banana'
		banana_quantity = BANANA_QUANTITY
		banana_unit_type = BANANA_UNIT_TYPE
		banana_calories = math.ceil(BANANA_CALORIES * BANANA_QUANTITY)

		return self._create_item(banana_name, banana_quantity, banana_unit_type, banana_calories)


	def _create_item(self, name, quantity, unit_type, calories):
		return {
			'name': name,
			'quantity': quantity,
			'unit_type': unit_type, 
			'calories': calories
		}