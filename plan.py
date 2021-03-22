import sys
import math
import argparse

from rich.console import Console

from table.html_table import HtmlTable
from table.rich_table import RichTable

from menu.menu import Menu


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
	lunch_table = HtmlTable(lunch).create_table('Lunch')
	dinner_table = HtmlTable(dinner).create_table('Dinner')
	snack_table = HtmlTable(snack).create_table('Snacks')

	print(lunch_table)
	print(dinner_table)
	print(snack_table)


def display_rich_table(lunch, dinner, snack):
	lunch_table = RichTable(lunch).create_table('Lunch')
	dinner_table = RichTable(dinner).create_table('Dinner')
	snack_table = RichTable(snack).create_table('Snacks')

	console = Console()
	console.print(lunch_table)
	console.print(dinner_table)
	console.print(snack_table)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("calories", help="file containing items")
    parser.add_argument("menu", help="payer 1 share percentage")
    parser.add_argument("-l", "--html", help="print tables in html", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    run(args.calories, args.menu, args.html)