'''
Created on 20.4.2016

@author: Ilkka
'''
# -*- coding: utf-8 -*-
from recipe import Recipe

class Ingredient:
    
    def __init__(self, ingredient_name, density, allergen, recipes):
        self.ingredient_name = ingredient_name
        self.density = density
        self.allergen = allergen
        self.recipes = recipes
        
    def chance_amount(self, amount, unit):
        '''
        '''
    def add_recipes(self, name_recipe, Recipe):
        Recipe.name_recipe = name_recipe
    