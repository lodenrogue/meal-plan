from rich.table import Table


class RichTable():

	def __init__(self, menu):
		self.menu = menu


	def create_table(self, table_name):
		table = Table(title=table_name, show_lines=True)

		table.add_column('Name', style='cyan', no_wrap=True, width=17)
		table.add_column('Quantity', justify='right', no_wrap=True, width=10)
		table.add_column('Units', justify='right', no_wrap=True, width=10)
		table.add_column('Calories', justify='right', style='green', no_wrap=True, width=10)

		for item in self.menu:
			name = item['name']
			quantity = '{:.2f}'.format(item['quantity'])
			units = item['unit_type']
			calories = str(item['calories'])

			table.add_row(name, quantity, units, calories)

		return table