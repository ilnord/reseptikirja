'''
Created on 20.4.2016

@author: Ilkka
'''
# -*- coding: utf-8 -*-
from recipe import Recipe

G = 0
KG = 1
TSP = 2
TBSP = 3
CL = 4
DL = 5
L = 6
PIECE = 7
PORTION = 8

class Ingredient:
    
    def __init__(self):
        self.name = None
        self.density = None
        self.recipes = None
        self.allergens = []
        
    def set_name(self, name):
        self.name = name
    def set_density(self, density):
        try:
            self.density = float(density)
            return True
        except ValueError:
            return False
    def set_allergen(self, allergen):
        self.allergens.append(allergen)
    def set_recipe(self, Recipe):
        self.recipes =Recipe
    
    def get_name(self):
        return self.name
    def get_density(self):
        return self.density
    def get_recipes(self):
        return self.recipes
    def get_allergens(self):
        return self.allergens
    
class Ingredient_container:
    def __init__(self):
        self.ingredient = None
        self.amount = None
        self.unit = None
    
    def set_ingredient(self,ingredient,ingredients_list):
        
        for i in ingredients_list:
                if i.get_name().strip().lower() == ingredient.lower():
                    self.ingredient = i
                    return True
                else:
                    # Ei raaka-ainetta talla nimella
                    pass
        return False

    def set_amount(self,amount):
        #Asettaa maaran
        try:
            self.amount = int(amount)
            return True
        except ValueError:
            return False
    
    def set_unit(self, unit):
        #Asettaa yksikon
        self.unit = unit
        
        
    def get_ingredients(self):
        return self.ingredient
    def get_amount(self):
        return self.amount
    def get_unit(self):
        return self.unit