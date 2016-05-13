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
from ingredient import Ingredient
from io import StringIO
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
        f_storage = open('Storage.txt', 'r')
        f_recipe = open('Recipes.txt', 'r')
        f_ingredients = open('Ingredients.txt', 'r')
        self.ingredients_list, succesfull_reads, failed_reads = self.IO.read_ingredients_from_file(f_ingredients)
        self.storage_list, succesfull_reads, failed_reads = self.IO.read_storage_from_file(f_storage, self.ingredients_list)
        self.recipes_list, succesfull_reads, failed_reads = self.IO.read_recipes_from_file(f_recipe, self.ingredients_list)
        f_storage.close()
        f_recipe.close()
        f_ingredients.close()
        
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
        self.input_file.write('INGREDIENTS\n\n')
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
        f = open('Ingredients_test.txt', 'r')
        ingredients_list, successfull_reads, failed_reads = self.IO.read_ingredients_from_file(f)
        f.close()
        self.assertEqual(2, successfull_reads,"Onnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(1, failed_reads, "Epaonnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(ingredients_list), "Listan pituus ei vastaa onnistuneita lukuja")
        if len(ingredients_list) > 0:
            ingredient = ingredients_list[0]
            self.assertEqual("Kala", ingredient.get_name(), "Raaka-aineen nimi ei tasmaa")
            self.assertEqual(3, ingredient.get_density(), "Raaka-aineen tiheys ei tasmaa")
            self.assertEqual(["Kala","Ruodot"], ingredient.get_allergens(), "")

    def test_read_recipes_from_file(self):
         
        self.input_file = StringIO()
        self.input_file.write('RECIPES\n\n')
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
    
    
    def test_read_recipes_from_actual_file(self):
        f1 = open('Ingredients_test.txt', 'r')
        ingredients_list, successfull_reads_i, failed_reads_i = self.IO.read_ingredients_from_file(f1)
        f1.close()
        
        self.assertEqual(2, successfull_reads_i, "Onnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(1, failed_reads_i, "Epaonnistuneiden lukujen maara ei tasmaa")
        
        f2 = open('Recipes_test.txt', 'r')
        recipes_list, successfull_reads, failed_reads = self.IO.read_recipes_from_file(f2, ingredients_list)
        f2.close()
        
        self.assertEqual(1, successfull_reads, "Onnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(0, failed_reads, "Epaonnistuneiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(recipes_list), "Listan pituus ei vastaa onnistuneita lukuja")
        
        ingredient1 = ingredients_list[0]
        ingredient2 = ingredients_list[1]

        if len(recipes_list) > 0:
            recipe = recipes_list[0]
            self.assertEqual("Kalakakku", recipe.get_name(), "Reseptin nimi ei tasmaa")
            self.assertEqual(["paista kala", "tee kakku"], recipe.get_instructions(), "Ohjeet eivat tasmaa")
            self.assertIs(ingredient1, recipe.get_ingredients()[0].get_ingredients(), "Ensimmainen raaka-aine ei tasmaa haluttua oliota")
            self.assertIs(ingredient2, recipe.get_ingredients()[1].get_ingredients(), "Toinen raaka-aine ei vastaa haluttua oliota")
        
    def test_read_storage_from_file(self):
        
        self.input_file = StringIO()
        self.input_file.write('STORAGE\n')
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
        
        ingredient3 = Ingredient()
        ingredient3.set_name("peruna")
        ingredient3.set_density(1)
        
        ingredients_list = [ingredient1,ingredient2, ingredient3]
        
        f = open('Storage_test.txt', 'r')
        storage_list, successfull_reads, failed_reads = self.IO.read_storage_from_file(f, ingredients_list)
        f.close()
        

        self.assertEqual(2,successfull_reads,"Onnistuineiden lukujen maara ei tasmaa")
        self.assertEqual(successfull_reads, len(storage_list), "Listan pituus ei vastaa onnistuneita lukuja")
        
        if len(storage_list) > 0:
            self.assertIs(ingredient1, storage_list[0].get_ingredients(), "Ensimmainen raaka-aine ei tasmaa haluttua olioita")
            self.assertIs(ingredient2, storage_list[1].get_ingredients(), "Toinen raaka-aine ei tasmaa haluttua oliota")
###################################################################################################################
    
    def test_check_for_ingredients_all_ingredients_available(self):
        
        self.Find_recipes = Find_recipes()
        
        recipe = self.recipes_list[0]
        
        ingredients_found, loop_count = self.Find_recipes.check_for_ingredients(recipe)
        self.assertEqual(2, ingredients_found,"Loytyneiden raaka-aineiden maara ei tasmaa")
        self.assertEqual(0, loop_count, "Raaka-aineiden, joita yritettiin valmistaa varastosta, maara ei tasmaa")
    
             
    def test_check_for_ingredients_more_ingredients_made_from_storage(self):
        self.Find_recipes = Find_recipes()
        recipe = self.recipes_list[2]
        ingredients_found, loop_count = self.Find_recipes.check_for_ingredients(recipe)
        self.assertEqual(2, ingredients_found,"Loytyneiden raaka-aineiden maara ei tasmaa")
        self.assertEqual(1, loop_count, "Raaka-aineiden, joita yritettiin valmistaa varastosta, maara ei tasmaa")
       
    
    def test_find_all_recipes(self):
        self.Find_recipes = Find_recipes()
        
        makeable_recipes = self.Find_recipes.find_all_recipes()
        self.assertEqual(3, len(makeable_recipes), "Valmistettavissa olevien rseptien maara ei tasmaa")
        
        self.assertEqual(makeable_recipes[0].get_name(), self.recipes_list[0].get_name(), "Reseptin nimi ei tasmaa")
             
    def test_find_missing_n_ingredients(self):
        self.Find_recipes = Find_recipes()
        
        missing_ingredients = 1
        makeable_recipes = self.Find_recipes.find_missing_n_ingredients(missing_ingredients)
        self.assertEqual(4, len(makeable_recipes), "Valmistettavissa olevien reseptien maara ei tasmaa kun yksi puuttuva raaka-aine sallitaan" )
        
    def test_find_must_not_include(self):
        self.Find_recipes = Find_recipes()
        
        forbidden_ingredients = ["riisi", "kala"]
        makeable_recipes = self.Find_recipes.find_must_not_include(forbidden_ingredients)
        self.assertEqual(2, len(makeable_recipes), "Valmistettavissa olevien reseptien maara ei tasmaa kun raaka-aineet riisi ja kala on kielletty")
        
    def test_find_must_include(self):
        self.Find_recipes = Find_recipes()
        
        mandatory_ingredients = ["mehu", "mansikka"]
        makeable_recipes = self.Find_recipes.find_must_include(mandatory_ingredients)
        print(mandatory_ingredients)
        #for recipe in makeable_recipes:
        #    print(recipe.get_name())
        self.assertEqual(1, len(makeable_recipes), "Valmistettavissa olevien reseptien maara ei tasmaa kun raaka-aineet mehu ja mansikka ovat pakolliset")
        
        mandatory_ingredients2 = ["riisi", "kala"]
        makeable_recipes = self.Find_recipes.find_must_include(mandatory_ingredients2)
        print(mandatory_ingredients2)
        #for recipe in makeable_recipes:
        #    print(recipe.get_name())
        self.assertEqual(1, len(makeable_recipes), "Valmistettavissa olevien reseptien maara ei tasmaa kun raaka-aine riisi on pakollinen")
        
    def test_find_no_allergens(self):
        self.Find_recipes = Find_recipes()
        
        allergens = ["tarkkelys"]
        makeable_recipes = self.Find_recipes.find_no_allergens(allergens)
        self.assertEqual(2, len(makeable_recipes), "Valmistettavissa olevien reseptien maara ei tasmaa kun allergeeni tarkkelys on kielletty")