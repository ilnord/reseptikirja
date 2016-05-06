'''
Created on Apr 19, 2016
@author: saarnii1
'''
# -*- coding: utf-8 -*-

from recipe import Recipe
from IO import IO         
from ingredient import Ingredient
from unit_transfer import Unit_transfer

G = 0
KG = 1
TSP = 2
TBLSP = 3
CL = 4
DL = 5
L = 6
PIECE = 7
PORTION = 8


class Find_recipes:
    '''
    Eli etsi_ruoka
    Maaritellaan tarkemmin sita, mita lahdetaan hakemaan:
    maaritellaan milla ehdoilla ohjelman kehittama lista halutaan muodostaa.
    '''
    
    def __init__(self):
        self.IO = IO()
        self.Unit_transfer = Unit_transfer()
        f_storage = open('Storage.txt', 'r')
        f_recipe = open('Recipelist.txt', 'r')
        f_ingredients = open('Ingredientlist.txt', 'r')
        self.ingredients_list, succesfull_reads, failed_reads = self.IO.read_ingredients_from_file(f_ingredients)
        self.storage_list, succesfull_reads, failed_reads = self.IO.read_storage_from_file(f_storage, self.ingredients_list)
        self.recipes_list, succesfull_reads, failed_reads = self.IO.read_recipes_from_file(f_recipe, self.ingredients_list)
        #print(self.ingredients_list)
        #print(self.storage_list)
        #print(self.recipes_list)
        f_storage.close()
        f_recipe.close()
        f_ingredients.close()
        self.makeable_recipes = []
       
    
     
    def check_ingredient_amount(self, recipe_ingredient, storage_ingredient):
        #Tarkistaa kunkin reseptin vaatiman raaka-aineen kohdalla, onko sita varastossa tarpeeksi
        if recipe_ingredient.get_unit() == storage_ingredient.get_unit():
            if recipe_ingredient.get_amount() < storage_ingredient.get_amount():
                return True
            else:
                return False
        else:
            wanted_unit = recipe_ingredient.get_unit()
            #print(wanted_unit)
            received_unit = storage_ingredient.get_unit()
            #print(received_unit)
            density = recipe_ingredient.get_ingredients().get_density()
            #print(density)
            received_amount = storage_ingredient.get_amount()
            #print(received_amount)
            self.storage_ingredient_transferred_amount = self.Unit_transfer.unit_transfer(received_unit, wanted_unit, received_amount, density)
            #print(self.storage_ingredient_transferred_amount)
            if recipe_ingredient.get_amount() < self.storage_ingredient_transferred_amount:
                return True
            else:
                return False
        
        
    def check_for_ingredients(self, recipe):
        #Tarkistaa, kuinka monta raaka-ainetta tarvittavista on saatavilla.
        #Kayttaa apunaan metodia check_ingredients_amount, joka tarkistaa kunkin raaka-aineen maaran riittavyyden
        ingredients_found = 0
        
        for recipe_ingredient in recipe.get_ingredients():
            for storage_ingredient in self.storage_list:
                #print(recipe_ingredient.get_ingredients().get_name())
                #print(storage_ingredient.get_ingredients().get_name())
                if recipe_ingredient.get_ingredients().get_name() == storage_ingredient.get_ingredients().get_name():
                    print("loyty match")
                    if self.check_ingredient_amount(recipe_ingredient, storage_ingredient):
                        ingredients_found += 1
                    elif recipe_ingredient.get_ingredients().get_recipe() != None:
                        recipe_object = recipe_ingredient.get_ingredients().get_recipe_object(self.recipes_list)
                        print(recipe_object)
                        print("tarvittavat osumat =", len(recipe_object.get_ingredients()))
                        print(recipe_object.get_ingredients()[0].get_ingredients().get_name())
                        print(recipe_object.get_ingredients()[1].get_ingredients().get_name())
                        if self.check_for_ingredients(recipe_object) == len(recipe.get_ingredients()):
                            print("ASDASDASDASDASDASDASD")
                            ingredients_found += 1
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