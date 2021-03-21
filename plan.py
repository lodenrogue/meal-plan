import sys
import math
import argparse

from rich.console import Console
from rich.table import Table

from table.html_table import HtmlTable
from menu import Menu


def run(calories, menu_type, is_html):
	menu = Menu(calories, menu_type)
	lunch = menu.get_lunch()
	snack = menu.get_snack()
	dinner = menu.get_dinner()

	if is_html:
		display_html_table(lunch, dinner, snack)
	else:
		display_rich_table(lunch, dinner, snack)
		

def display_html_table(lunch, dinner, snack):
	lunch_table = HtmlTable(lunch).create_table()
	dinner_table = HtmlTable(dinner).create_table()
	snack_table = HtmlTable(snack).create_table()

	print("<b>Lunch</b>")
	print("<br/>")
	print(lunch_table)
	print("<br/><br/>")

	print("<b>Dinner</b>")
	print("<br/>")
	print(dinner_table)
	print("<br/><br/>")


	print("<b>Snacks</b>")
	print("<br/>")
	print(snack_table)
	print("<br/><br/>")


def display_rich_table(lunch, dinner, snack):
	lunch_table = create_table('Lunch', lunch)
	dinner_table = create_table('Dinner', dinner)
	snack_table = create_table('Snacks', snack)

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


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("calories", help="file containing items")
    parser.add_argument("menu", help="payer 1 share percentage")
    parser.add_argument("-l", "--html", help="print tables in html", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    run(args.calories, args.menu, args.html)