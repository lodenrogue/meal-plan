
class ItemCreator():

    def __init__(self, name, quantity, unit_type, calories):
        self.name = name
        self.quantity = quantity
        self.unit_type = unit_type
        self.calories = calories


    def create(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'unit_type':self.unit_type, 
            'calories': self.calories
        }