'''
Created on 19.4.2016
@author: Ilkka
'''
# -*- coding: utf-8 -*-
from find_recipes import Find_recipes
from recipe import Recipe
from ingredient import Ingredient
from IO import IO

class Main(object):
    
    def __init__(self):
        #Luodaan menut ja submenut
        self.main_menu_options = ["1. Hae resepteja", "2. Tarkastele tunnettuja resepeja", "3. Tarkastele tunnettuja raaka-aineita", \
                                  "4. Tarkastele tämänhetkista varastoa", "0. Sulje ohjelma"]
        self.search_menu_options = ["1. Etsi kaikki reseptit, jotka valmistettavissa varastossa olevista raaka-aineista", "2. Etsi kaikki reseptit, jotka sisaltavat tiettyja raaka-aineita", \
                                    "3. Etsi reseptit, jotka eivat sisalla tiettyja aineita", "4. Etsi reseptit, jotka eivat sisalla tiettya allergeenia",\
                                     "5. Etsi reseptit, joista puuttuu korkeintaa N-määrä raaka-aineita varastosta", "0. Takaisin"]
        self.inventory_menu_options = ["1. Etsi tietty raaka-aine", "2. Listaa varasto", "0. Takaisin"]
        self.recipes_menu_options = ["1. Etsi tietty resepti ja tulosta sen tiedot", "2. Listaa kaikki reseptit ja niiden tiedot", "0. Takaisin"]
        self.ingredients_menu_options = ["1. Etsi tietty raaka-aine", "2. Listaa raaka-aineet", "0. Takaisin"]
        
        self.Ingredient = Ingredient()
        self.Find_recipes = Find_recipes()
        self.Recipes = Recipe()
        self.IO = IO()
        self.test_mode = False
        self.makeable_recipes = []
        f_storage = open('Storage.txt', 'r')
        f_recipe = open('Recipes.txt', 'r')
        f_ingredients = open('Ingredients.txt', 'r')
        self.ingredients_list = self.IO.read_ingredients_from_file(f_ingredients)[0]
        self.storage_list = self.IO.read_storage_from_file(f_storage, self.ingredients_list)[0]
        self.recipes_list = self.IO.read_recipes_from_file(f_recipe, self.ingredients_list)[0]
        f_storage.close()
        f_recipe.close()
        f_ingredients.close()
        
    def run_menu(self, menu_options):
        
        for i in menu_options:
            print(i)
        
        while True:
            user_input = self.ask_for_input("Miten haluat edetä?  ")
            if user_input >= 0 and user_input < len(menu_options):
                return user_input
            else:
                print("Tuntematon arvo")
                
    def ask_for_input(self, question):
        user_input = input(question)
        if self.test_mode:
            user_input = question
        while True:
            try:
                user_input = int(user_input)  
                return user_input
            except ValueError:
                print("Annettu arvo ei ole kokonaisluku")
            user_input = input(question)
                
    def ask_for_input_string(self, question):
        user_input = input(question)
        return user_input
    
    def input_text_to_list(self, input_temp):
        input_list = input_temp.split(",")
        input_list = [i.strip(' ').lower() for i in input_list]
        return input_list
    def format_input(self, input_temp):
        formatted_input = input_temp.strip().lower()
        return formatted_input
    
    
    def main_menu(self):
        while True:
            user_input = self.run_menu(self.main_menu_options)
            if user_input == 1:
                self.search_menu()
            elif user_input == 2:
                self.recipes_menu()
            elif user_input == 3:
                self.ingredients_menu()
            elif user_input == 4:
                self.inventory_menu()
            elif user_input == 0:
                return 0
      
      
            
    def search_menu(self):
        while True:
            user_input = self.run_menu(self.search_menu_options)
            if user_input == 1:
                self.makeable_recipes = self.Find_recipes.find_all_recipes()
                for recipe in self.makeable_recipes:
                    self.print_recipes(recipe)
                self.makeable_recipes = []
                
            elif user_input == 2:
                input_temp = self.ask_for_input_string\
                    ("Mita kaikkia raaka-aineita haluat reseptien sisaltavan? Anna raaka-aineet pilkulla eroteltuna\n")
                must_include_ingredients = self.input_text_to_list(input_temp)
                self.makeable_recipes = self.Find_recipes.find_must_include(must_include_ingredients)
                if not self.makeable_recipes:
                    print("Valituilla raaka-aineilla ei loytynyt yhtakaan reseptia")
                for recipe in self.makeable_recipes:
                    self.print_recipes(recipe)
                self.makeable_recipes = []
                
            elif user_input == 3:
                input_temp = self.ask_for_input_string\
                    ("Mita raaka-aineita et halua reseptien sisaltavan? Anna raaka-aineet pilkulla eroteltuna\n")
                forbidden_ingredients = self.input_text_to_list(input_temp)
                self.makeable_recipes = self.Find_recipes.find_must_not_include(forbidden_ingredients)
                if not self.makeable_recipes:
                    print("Valituilla raaka-aineilla ei loytynyt yhtakaan reseptia")
                for recipe in self.makeable_recipes:
                    self.print_recipes(recipe)
                self.makeable_recipes = []
                
            elif user_input == 4:
                input_temp = self.ask_for_input_string\
                    ("Mita allergeeneja et halua reseptin sisaltavan? Anna allergeenit pilkulla eroteltuna\n")
                allergens = self.input_text_to_list(input_temp)
                self.makeable_recipes = self.Find_recipes.find_no_allergens(allergens)
                if not self.makeable_recipes:
                    print("Annetuilla allergeeneilla ei voida valmistaa yhtakaan reseptia")
                for recipe in self.makeable_recipes:
                    self.print_recipes(recipe)
                    
            elif user_input == 5:
                n = self.ask_for_input\
                    ("Kuina monta raaka-ainetta reseptista saa puuttua?\n")
                self.makeable_recipes = self.Find_recipes.find_missing_n_ingredients(n)
                if not self.makeable_recipes:
                    print("Annetulla puuttuvien raaka-aineiden maksimilla ei voi valmistaa yhtakaan reseptia")
                for recipe in self.makeable_recipes:
                    self.print_recipes(recipe)
                    
            elif user_input == 0:
                return 0
            
          
          
            
    def print_recipes(self, recipe):
        print(recipe.get_name().upper())
        print("Reseptin raaka-aineet:")
        for ingredient in recipe.get_ingredients():
            print(ingredient.get_ingredients().get_name(), ingredient.get_amount(), ingredient.get_unit())
        print("Reseptin ohjeet:" )
        for instruction in recipe.get_instructions():
            print(instruction)
        print("Valmista tuotetta syntyy ", recipe.get_outcome_amount(), recipe.get_outcome_unit())
        print("\n")
        
    def recipes_menu(self):
        user_input = self.run_menu(self.recipes_menu_options)
        found = False
        if user_input == 1:
            input_temp = self.ask_for_input_string\
                ("Minka reseptin tiedot haluat näkyviin?\n")
            wanted_recipe = self.format_input(input_temp)
            for recipe in self.recipes_list:
                if recipe.get_name() == wanted_recipe:
                    self.print_recipes(recipe)
                    found = True
            if found == False:
                print("Haluttua reseptia ei löytynyt")
                
            
        elif user_input == 2:
            for recipe in self.recipes_list:
                self.print_recipes(recipe)
                
        elif user_input == 0:
            return 0
        
        
        
    def print_ingredients(self, ingredient):
        print(ingredient.get_name().upper())
        print("Raaka-aineen tiheys: ", ingredient.get_density())
        print("\n")
        
        
        
    def ingredients_menu(self):
        user_input = self.run_menu(self.ingredients_menu_options)
        found = False
        if user_input == 1:
            input_temp = self.ask_for_input_string\
                ("Minkä raaka-aineen tiedot haluat näkyviin?\n")
            wanted_ingredient = self.format_input(input_temp)
            for ingredient in self.ingredients_list:
                if ingredient.get_name() == wanted_ingredient:
                    self.print_ingredients(ingredient)
                    found = True
            if found == False:
                print("Haluttua raaka-ainetta ei löytynyt")
                
        elif user_input == 2:
            for ingredient in self.ingredients_list:
                self.print_ingredients(ingredient)
                

        elif user_input == 0:
            return 0   
                 
                 
                 
                 
    def print_storage_item(self, storage_item):
        print (storage_item.get_ingredients().get_name().upper())
        print ("Määrä varastossa:", storage_item.get_amount(), storage_item.get_unit())
    
               
    def inventory_menu(self):
        user_input = self.run_menu(self.inventory_menu_options)
        if user_input == 1:
            input_temp = self.ask_for_input_string\
                ("Minka aineen varastotiedot tiedot haluat näkyviin?\n")
            wanted_storage_item = self.format_input(input_temp)
            for storage_item in self.storage_list:
                if storage_item.get_ingredients().get_name() == wanted_storage_item:
                    self.print_storage_item(storage_item)
                    
                    
        elif user_input == 2:
            for storage_item in self.storage_list:
                self.print_storage_item(storage_item)
                
                
        elif user_input == 0:
            return 0
        
        
        

    
if __name__ == "__main__":
    program = Main()
    program.main_menu()
    print("Exiting")