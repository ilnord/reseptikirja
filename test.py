'''
Created on 23.4.2016

@author: Ilkka
'''
# -*- coding: utf-8 -*-
G = 0
KG = 1
TSP = 2
TBLSP = 3
CL = 4
DL = 5
L = 6
PIECE = 7
PORTION = 8

import unittest
from main_menu import Main
from IO import IO
from ingredient import Ingredient, Ingredient_container
from io import StringIO
from recipe import Recipe
from unit_transfer import Unit_transfer
from find_recipes import Find_recipes

class Test(unittest.TestCase):
    
    def setUp(self):
        
        #Main program setUp
        self.main_test = Main()
        self.main_test.test_mode = True
        #IO setUp
        self.IO = IO()
        self.Unit_transfer = Unit_transfer()
        
    def test_transfer_mass_to_mass(self):
        unit = KG 
        wanted_unit = G
        amount = 3
        density = 1
        received_amount = self.Unit_transfer.unit_transfer(unit, wanted_unit, amount, density)
        self.assertEqual(3000, received_amount, "Saatu maara ei tasmaa")
        
    def test_transfer_volume_to_volume(self):
        unit = TBLSP
        wanted_unit = L
        amount = 50
        density = 1
        
        received_amount = self.Unit_transfer.unit_transfer(unit, wanted_unit, amount, density)
        self.assertEqual(0.75, received_amount, "Saatu maara ei tasmaa")
    
    def test_transfer_mass_to_volume(self):
        unit = G
        wanted_unit = DL
        amount = 30
        density = 2
        
        received_amount = self.Unit_transfer.unit_transfer(unit, wanted_unit, amount, density)
        self.assertEqual(0.15, received_amount, "Saatu maara ei tasmaa")
    
    def test_transfer_volume_to_mass(self):
        unit = L
        wanted_unit = G
        amount = 0.01
        density = 4
        
        received_amount = self.Unit_transfer.unit_transfer(unit, wanted_unit, amount, density)
        self.assertEqual(40, received_amount, "Saatu maara ei tasmaa")
        
     
########################################################################################################################################
        
    
    def test_read_ingredients_from_file(self):
        
        self.input_file = StringIO()
        self.input_file.write('INGREDIENTLIST\n\n')
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Name             : Kala')
        self.input_file.write('\nDensity            : 3\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Kala\n')
        self.input_file.write('\nAllergen     : Ruodot\n')
        
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Name             : Kakku\n')
        self.input_file.write('\nDensity            : asd\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Kananmuna\n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        
        self.input_file.seek(0, 0)
        
        ingredients_list, successfull_reads, failed_reads = self.IO.read_ingredients_from_file(self.input_file)
        self.input_file.close()
        self.assertEqual(1, successfull_reads,"Onnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(1, failed_reads, "Epaonnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(ingredients_list), "Listan pituus ei vastaa onnistuneita lukuja")
        if len(ingredients_list) > 0:
            ingredient = ingredients_list[0]
            self.assertEqual("Kala", ingredient.get_name(), "Raaka-aineen nimi ei tasmaa")
            self.assertEqual(3, ingredient.get_density(), "Raaka-aineen tiheys ei tasmaa")
            self.assertEqual(["Kala","Ruodot"], ingredient.get_allergens(), "")
            
    def test_read_ingredients_from_actual_file(self):
        f = open('Ingredientlist.txt', 'r')
        ingredients_list, successfull_reads, failed_reads = self.IO.read_ingredients_from_file(f)
        f.close()
        self.assertEqual(1, successfull_reads,"Onnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(1, failed_reads, "Epaonnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(ingredients_list), "Listan pituus ei vastaa onnistuneita lukuja")
        if len(ingredients_list) > 0:
            ingredient = ingredients_list[0]
            self.assertEqual("Kala", ingredient.get_name(), "Raaka-aineen nimi ei tasmaa")
            self.assertEqual(3, ingredient.get_density(), "Raaka-aineen tiheys ei tasmaa")
            self.assertEqual(["Kala","Ruodot"], ingredient.get_allergens(), "")

    def test_read_recipes_from_file(self):
         
        self.input_file = StringIO()
        self.input_file.write('RECIPELIST\n\n')
        self.input_file.write('#Recipe\n')
        self.input_file.write('\nName            : Paistettu riisi\n')
        self.input_file.write('\nOutcome            : 4: portion\n')
        self.input_file.write('\nInstructions     : Keita riisi\n')
        self.input_file.write('\nInstructions     : Paista riisi')
        self.input_file.write('\nIngredient     : riisi : 500 : g')
        self.input_file.write('\nIngredient     : vesi : 1 : l')
         
        self.input_file.seek(0, 0) 
        
        ingredient1 = Ingredient()
        ingredient1.set_name("riisi")
        ingredient1.set_density(0.5)
        
        ingredient2 = Ingredient()
        ingredient2.set_name("vesi")
        ingredient2.set_density(1)

        
        ingredients_list = [ingredient1,ingredient2]
 
        recipes_list, successfull_reads, failed_reads = self.IO.read_recipes_from_file(self.input_file, ingredients_list)
        self.input_file.close()
        self.assertEqual(1, successfull_reads, "Onnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(0, failed_reads, "Epaonnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(recipes_list), "Listan pituus ei vastaa onnistuneita lukuja")
        
        if len(recipes_list) > 0:
            recipe = recipes_list[0]
            self.assertEqual("Paistettu riisi", recipe.get_name(), "Raaka-aineen nimi ei tasmaa")
            self.assertEqual(["Keita riisi", "Paista riisi"], recipe.get_instructions(), "Ohjeet eivat tasmaa")
            self.assertIs(ingredient1, recipe.get_ingredients()[0].get_ingredients(), "Ensimmainen raaka-aine ei tasmaa haluttua oliota")
            self.assertIs(ingredient2, recipe.get_ingredients()[1].get_ingredients(), "Toinen raaka-aine ei vastaa haluttua oliota")
    
    def test_read_storage_from_file(self):
         
        self.input_file = StringIO()
        self.input_file.write('STORAGELIST\n')
        self.input_file.write('riisi;10;kg\n')
        self.input_file.write('asdpoks\n')
        self.input_file.write('mehu;1;dl\n')

        self.input_file.seek(0, 0) 
        
        ingredient1 = Ingredient()
        ingredient1.set_name("riisi")
        ingredient1.set_density(0.5)
        
        ingredient2 = Ingredient()
        ingredient2.set_name("mehu")
        ingredient2.set_density(1)

        
        ingredients_list = [ingredient1,ingredient2]
 
        storage_list,successfull_reads, failed_reads = self.IO.read_storage_from_file(self.input_file,ingredients_list)
        self.input_file.close()
        self.assertEqual(2,successfull_reads,"Onnistuineiden lukujen maara ei tasmaa")
        self.assertEqual(1, failed_reads, "Epaonnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(storage_list), "Listan pituus ei vastaa onnistuneita lukuja")
        
        if len(storage_list) > 0:
            self.assertIs(ingredient1, storage_list[0].get_ingredients(), "Ensimmainen raaka-aine ei tasmaa haluttua olioita")
            self.assertIs(ingredient2, storage_list[1].get_ingredients(), "Toinen raaka-aine ei tasmaa haluttua oliota")
            
            
    def test_read_storage_from_actual_file(self):
        ingredient1 = Ingredient()
        ingredient1.set_name("riisi")
        ingredient1.set_density(0.5)
        
        ingredient2 = Ingredient()
        ingredient2.set_name("mehu")
        ingredient2.set_density(1)
        
        ingredients_list = [ingredient1,ingredient2]
        
        f = open('Storage.txt', 'r')
        storage_list, successfull_reads, failed_reads = self.IO.read_storage_from_file(f, ingredients_list)
        f.close()
        

        self.assertEqual(2,successfull_reads,"Onnistuineiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(storage_list), "Listan pituus ei vastaa onnistuneita lukuja")
        
        if len(storage_list) > 0:
            self.assertIs(ingredient1, storage_list[0].get_ingredients(), "Ensimmainen raaka-aine ei tasmaa haluttua olioita")
            self.assertIs(ingredient2, storage_list[1].get_ingredients(), "Toinen raaka-aine ei tasmaa haluttua oliota")
###################################################################################################################

    def test_check_for_ingredients(self):
        self.Find_recipes = Find_recipes()
        ingredient1 = Ingredient()
        ingredient1.set_name("riisi")
        ingredient1.set_density(0.5)
        
        ingredient2 = Ingredient()
        ingredient2.set_name("vesi")
        ingredient2.set_density(1)
        
        ingredients_list = [ingredient1,ingredient2]
        
        ingredient_container = Ingredient_container()
        ingredient_container2 = Ingredient_container()
        ingredient_container.set_ingredient(ingredient1.get_name(), ingredients_list)
        ingredient_container2.set_ingredient(ingredient2.get_name(), ingredients_list)
        

        recipe1 = Recipe()
        recipe1.set_name("Paistettu riisi")
        recipe1.set_outcome_amount(5)
        recipe1.set_outcome_unit("dl")
        recipe1.set_instructions("keita riisi")
        recipe1.set_instructions("paista riisi")
        recipe1.add_ingredients(ingredient_container)

        
        ingredients_found = self.Find_recipes.check_for_ingredients(recipe1)
        self.assertEqual(1, ingredients_found,"Loytyneiden raaka-aineiden maara ei tasmaa")
