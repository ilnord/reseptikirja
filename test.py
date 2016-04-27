'''
Created on 23.4.2016

@author: Ilkka
'''
# -*- coding: utf-8 -*-

import unittest
from main_menu import Main
from IO import IO
from ingredient import Ingredient
from io import StringIO

class Test(unittest.TestCase):
    
    def setUp(self):
        
        #Main program setUp
        self.main_test = Main()
        self.main_test.test_mode = True
        #IO setUp
        self.IO = IO()

    def test_read_ingredients_from_file(self):
        
        self.input_file = StringIO()
        self.input_file.write('INGREDIENTLIST\n\n')
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Name             : Kala\n')
        self.input_file.write('\nDensity            : 1\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        
        self.input_file.write('#Ingredient\n')
        self.input_file.write('Name             : Kala2\n')
        self.input_file.write('\nDensity            : asd\n')
        self.input_file.write('\nRecipe     : \n')
        self.input_file.write('\nAllergen     : Laktoosi\n')
        self.input_file.write('\nAllergen     : Maissi\n')
        
        self.input_file.seek(0, 0)
        
        ingredients_list, successfull_reads, failed_reads = self.IO.read_ingredients_from_file(self.input_file)
        self.input_file.close()
        self.assertEqual(1, successfull_reads,"vaara maara onnistuneita lukuja")
        self.assertEqual(1, failed_reads, "vaara maara epaonnistuneita lukuja")
        self.assertEqual(successfull_reads, len(ingredients_list), "Lista eripituinen kuin onnistuneet lukemiset")
        if len(ingredients_list) > 0:
            ingredient = ingredients_list[0]
            self.assertEqual("Kala", ingredient.get_name(), "Raaka-aineen nimi ei tasmaa")
            self.assertEqual(1, ingredient.get_density(), "Raaka-aineen tiheys ei tasmaa")
            self.assertEqual(["Laktoosi","Maissi"], ingredient.get_allergens(), "Raaka-aineen allergeenit eivat tasmaa")
