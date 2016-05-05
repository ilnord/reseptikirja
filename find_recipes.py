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
        self.IO = IO()
        f_storage = open('Storage.txt', 'r')
        f_recipe = open('Recipelist.txt', 'r')
        f_ingredients = open('Ingredientlist.txt', 'r')
        self.ingredients_list, succesfull_reads, failed_reads = self.IO.read_ingredients_from_file(f_ingredients)
        self.storage_list, succesfull_reads, failed_reads = self.IO.read_storage_from_file(f_storage, self.ingredients_list)
        self.recipes_list, succesfull_reads, failed_reads = self.IO.read_recipes_from_file(f_recipe, self.ingredients_list)
        print(self.ingredients_list)
        print(self.storage_list)
        print(self.recipes_list)
        f_storage.close()
        f_recipe.close()
        f_ingredients.close()
        self.makeable_recipes = []
       
    
     
    def check_ingredient_amount(self, recipe_ingredient, storage_ingredient):
        #Tarkistaa kunkin reseptin vaatiman raaka-aineen kohdalla, onko sita varastossa tarpeeksi
        print (recipe_ingredient.get_unit)
        print (storage_ingredient.get_unit)
        print("asd")
        if recipe_ingredient.get_unit() == storage_ingredient.get_unit():
            if recipe_ingredient.get_amount() < storage_ingredient.get_amount():
                return True
            else:
                return False
        else:
            wanted_unit = recipe_ingredient.get_unit()
            received_unit = storage_ingredient.get_unit()
            density = recipe_ingredient.get_density()
            received_amount = storage_ingredient.get_amount()
            storage_ingredient_transferred_amount = Unit_transfer.unit_transfer(self, received_unit, wanted_unit, received_amount, density)
            if recipe_ingredient.get_amount() < storage_ingredient_transferred_amount:
                return True
            else:
                return False
        
        
    def check_for_ingredients(self, recipe):
        #Tarkistaa, kuinka monta raaka-ainetta tarvittavista on saatavilla.
        #Kayttaa apunaan metodia check_ingredients_amount, joka tarkistaa kunkin raaka-aineen maaran riittavyyden
        
        ingredients_found = 0
        
        for recipe_ingredient in recipe.get_ingredients():
            for storage_ingredient in self.storage_list:
                if recipe_ingredient.get_ingredients() is storage_ingredient.get_ingredients():
                    if self.check_ingredient_amount(recipe_ingredient, storage_ingredient):
                        ingredients_found += 1
                    #elif recipe_ingredient.get_recipes() != None:
                        #if self.check_for_ingredients(recipe_ingredient.get_recipes()) \
                        #== len(recipe_ingredient.get_recipes().get_ingredients()):
                         #   ingredients_found += 1
                    break
        return ingredients_found
                    
    def find_all_recipes(self):
        #Etsii kaikki reseptit, jotka on valmistettavissa varastosta loytyvista raaka-aineista
        for recipe in self.recipes_list:
            if len(recipe.get_ingredients()) == self.check_for_ingredients(recipe):
                self.makeable_recipes.append(recipe)
        return self.makeable_recipes
     
        
    def missing_n_ingredients(self):
        #etsii reseptit, joiden valmistamiseksi puuttuu korkeintaa n raaka-ainetta
        pass
        
    def must_not_include(self):
        #etsii reseptit, jotka eivat saa sisaltaa tiettya raaka-ainetta
        pass
    
    def must_include(self):
        #etsii reseptit, joiden halutaan sisaltavan tiettya raaka-ainetta
        pass