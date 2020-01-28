# 32_Inheritance
from Chef import  Chef

class ChineseChef(Chef):

    def make_fried_rice(self):
        return print("The chef makes fried rice")

    # Sobrescribir el método que ya se tiene en la clase Chef
    def make_special_dish(self):
        return print("The chef makes oriental chicken")