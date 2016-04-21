'''
Created on 20.4.2016

@author: Ilkka
'''
# -*- coding: utf-8 -*-
from recipe import Recipe

class Ingredient:
    
    def __init__(self, ingredient_name, density, allergen, recipes):
        self.name = None
        self.density = None
        self.recipes = None
        self.allergens = []
        
    def set_name(self, name):
        self.name = name

    def set_density(self, density):
        self.density = density
        
    
    
    def get_name(self):
        return self.name
    def get_density(self):
        return self.density
    def get_recipes(self):
        return self.recipes
    def get_allergens(self):
        return self.allergens
    
    