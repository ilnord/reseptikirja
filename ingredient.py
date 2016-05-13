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
    #Raaka aine olio, joka pitaa sisallaan raaka-aineen muuttumattomat tiedot
    def __init__(self):
        self.name = None
        self.density = None
        self.recipes = None
        self.allergens = []
        
    def set_name(self, name):
        #Asettaa raaka-aineen nimen
        self.name = name
    
    def set_density(self, density):
        #Asettaa raaka-aineen tiheyden
        try:
            self.density = float(density)
            return True
        except ValueError:
            return False
        
    def set_allergen(self, allergen):
        #Asettaa raaka-aineen allergeenit
        self.allergens.append(allergen)
        
    def set_recipe(self, recipe):
        #Asettaa raaka-aineen reseptin
        self.recipe = recipe
    
    def get_name(self):
        #Palauttaa raaka-aineen nimen
        return self.name
    
    def get_density(self):
        #Palauttaa raaka aineen tiheyden
        return self.density
    
    def get_recipe(self):
        #Palauttaa raaka-aineen tiheyden
        return self.recipe
        
    def get_recipe_object(self, recipes_list):
        for i in recipes_list:
            if self.recipe == i.get_name():
                self.recipe_object = Recipe()
                self.recipe_object = i
                return self.recipe_object
                
    
    
    def get_allergens(self):
        #Palauttaa raaka-aineen allergeenit
        return self.allergens
    
class Ingredient_holder:
    #Raka aine olio, joka pitaa sisallaan raaka-aineen tilanteen mukaan muuttuvat tiedot
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
        #Palauttaa kyseessa olevan raaka-aineen
        return self.ingredient
    def get_amount(self):
        #Palauttaa raaka-aineen maaran
        return self.amount
    def get_unit(self):
        #Palauttaa raaka aineen yksikon
        return self.unit