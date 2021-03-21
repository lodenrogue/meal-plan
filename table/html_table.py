from prettytable import PrettyTable

class HtmlTable():

    def __init__(self, menu):
        self.menu = menu

    
    def create_table(self):
        table = PrettyTable()
        table.field_names = ["Name", "Quantity", "Units", "Calories"]
        
        table.align["Name"] = "l"
        table.align["Quantity"] = "r"
        table.align["Units"] = "r"
        table.align["Calories"] = "r"

        for item in self.menu:
            name = item['name']
            quantity = '{:.2f}'.format(item['quantity'])
            units = item['unit_type']
            calories = str(item['calories'])

            table.add_row([name, quantity, units, calories])

        return table.get_html_string()