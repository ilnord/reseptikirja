'''
Created on Apr 19, 2016
@author: saarnii1
'''
# -*- coding: utf-8 -*-

from recipe import Recipe
from IO import IO         
from ingredient import Ingredient
from unit_transfer import Unit_transfer

class Find_recipes:
    '''
    Eli etsi_ruoka
    Maaritellaan tarkemmin sita, mita lahdetaan hakemaan:
    maaritellaan milla ehdoilla ohjelman kehittama lista halutaan muodostaa.
    '''
    
    def __init__(self):
        f_storage = open('Storagelist.txt', 'r')
        f_recipe = open('Recipelist.txt', 'r')
        self.storage_list = self.IO.read_storage_from_file(f_storage)
        self.recipes_list = self.IO.read_recipes_from_file(f_recipe)
        f_storage.close()
        f_recipe.close()
        self.makeable_recipes = []
       
 
    def find_all_recipes(self):
        for recipe in self.recipes_list:
            if len(recipe.get_ingredients()) == self.check_for_ingredients(recipe):
                self.makeable_recipes.append(recipe)
        return self.makeable_recipes
        
    
     
    def check_ingredient_amount(self, recipe_ingredient, storage_ingredient):
        if recipe_ingredient.get_unit() == storage_ingredient.get_unit():
            if recipe_ingredient.get_amount() < storage_ingredient.get_amount():
                return True
            else:
                return False
        else:
            wanted_unit = recipe_ingredient.get_unit
            received_unit = storage_ingredient.get_unit
            density = recipe_ingredient.get_density()
            received_amount = storage_ingredient.get_amount
            storage_ingredient_transferred_amount = Unit_transfer.unit_transfer(self, received_unit, wanted_unit, received_amount, density)
            if recipe_ingredient.get_amount() < storage_ingredient_transferred_amount:
                return True
            else:
                return False
        
        
    def check_for_ingredients(self, Recipe):
        ingredients_found = 0
        
        for recipe_ingredient in Recipe.get_ingredients():
            for storage_ingredient in self.storage_list:
                if recipe_ingredient.get_ingredient == storage_ingredient.get_ingredient:
                    if self.check_ingredient_amount(recipe_ingredient, storage_ingredient):
                        ingredients_found += 1
                    elif recipe_ingredient.get_recipes() != None:
                        if self.check_for_ingredients(recipe_ingredient.get_recipes()) \
                        == len(recipe_ingredient.get_recipes().get_ingredients()):
                            ingredients_found += 1
                    break
        return ingredients_found
                    
    
    def missing_n_ingredients(self):
        #etsi reseptit, joiden valmistamiseksi puuttuu korkeintaa n raaka-ainetta
        pass
        
    def must_not_include(self):
        #etsi reseptit, jotka eivat saa sisaltaa tiettya raaka-ainetta
        pass
    
    def must_include(self):
        #etsi reseptit, joiden halutaan sisaltavan tiettya raaka-ainetta
        pass