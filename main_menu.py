'''
Created on 19.4.2016
@author: Ilkka
'''
# -*- coding: utf-8 -*-
from find_recipes import Find_recipes

class Main(object):
    
    def __init__(self):
        #Luodaan menut ja submenut
        self.main_menu_options = ["1. Hae resepteja", "2. Tarkastele tunnettuja resepeja", "3. Tarkastele tunnettua varastoa", \
                                  "4. Tulosta kaikki tunnetut raaka-aineet", "0. Sulje ohjelma"]
        self.search_menu_options = ["1. Etsi kaikki reseptit, jotka valmistettavissa varastossa olevista raaka-aineista", "2. Etsi kaikki reseptit, jotka sisaltavat tiettyja raaka-aineita", \
                                    "3. Etsi reseptit, jotka eivat sisalla tiettyja aineita", "4. Reseptit, joihin varastotarvikkeet riittävät", "5. Reseptit, joista puuttuu N-määrä raaka-aineita varastosta", "6. Reseptit, joista löytyy N-määrä raaka-aineita varastosta", "0. Takaisin"]
        self.inventory_menu_options = ["1. Etsi tietty raaka-aine", "2. Listaa varasto", "0. Takaisin"]
        self.recipes_menu_options = ["1. Etsi tietty resepti ja tulosta sen tiedot", "2. Listaa kaikki reseptit", "0. Takaisin"]
        self.ingredients_menu_options = ["1. Etsi tietty raaka-aine", "2. Listaa raaka-aineet", "0. Takaisin"]
        self.Find_recipes = Find_recipes()
        self.test_mode = False
        self.makeable_recipes = []
        
    def run_menu(self, menu_options):
        
        for i in menu_options:
            print(i)
        
        while True:
            user_input = self.ask_for_input("Mitä haluaisit tehdä?  ")
            if user_input >= 0 and user_input < len(menu_options):
                return user_input
            else:
                print("Tuntematon arvo")
                
    def ask_for_input(self, question):
        user_input = input(question)
        if self.test_mode:
            user_input = question
        user_input = int(user_input)  
        return user_input
    def ask_for_input_string(self, question):
        user_input = input(question)
        return user_input
    
    def input_text_to_list(self, input_temp):
        input_list = input_temp.split(",")
        input_list = [i.strip(' ').lower() for i in input_list]
        return input_list
    
    
    def main_menu(self):
        while True:
            user_input = self.run_menu(self.main_menu_options)
            if user_input == 1:
                self.search_menu()
            elif user_input == 2:
                self.inventory_menu()
            elif user_input == 3:
                self.recipes_menu()
            elif user_input == 4:
                self.ingredients_menu()
            elif user_input == 0:
                return 0
            
    def search_menu(self):
        while True:
            user_input = self.run_menu(self.search_menu_options)
            if user_input == 1:
                self.makeable_recipes = self.Find_recipes.find_all_recipes()
                for recipe in self.makeable_recipes:
                    print (recipe.get_name())
                self.makeable_recipes = []
                
            elif user_input == 2:
                input_temp = self.ask_for_input_string\
                    ("Mita kaikkia raaka-aineita haluat reseptien sisaltavan? Anna raaka-aineet pilkulla eroteltuna")
                must_include_ingredients = self.input_text_to_list(input_temp)
                self.makeable_recipes = self.Find_recipes.find_must_include(must_include_ingredients)
                if not self.makeable_recipes:
                    print("Valituilla raaka-aineilla ei loytynyt yhtakaan reseptia")
                for recipe in self.makeable_recipes:
                    print (recipe.get_name())
                self.makeable_recipes = []
                
            elif user_input == 3:
                input_temp = self.ask_for_input_string\
                    ("Mita raaka-aineita et halua reseptien sisaltavan? Anna raaka-aineet pilkulla eroteltuna")
                forbidden_ingredients = self.input_text_to_list(input_temp)
                self.makeable_recipes = self.Find_recipes.find_must_not_include(forbidden_ingredients)
                if not self.makeable_recipes:
                    print("Valituilla raaka-aineilla ei loytynyt yhtakaan reseptia")
                for recipe in self.makeable_recipes:
                    print (recipe.get_name())
                self.makeable_recipes = []
                
            elif user_input == 4:
                print("Tietoja")
            elif user_input == 5:
                print("Tietoja")
            elif user_input == 1:
                print("Tietoja")
            elif user_input == 0:
                return 0
            

    def recipes_menu(self):
        user_input = self.run_menu(self.recipes_menu_options)
        if user_input == 1:
            input_temp = self.ask_for_input_string\
                ("Minka reseptin tiedot haluat nakyviin?")
            wanted_recipe = self.input_text_to_list(input_temp)
            
        elif user_input == 2:
            print("Listataan reseptit")
        elif user_input == 0:
            return 0            
    def inventory_menu(self):
        user_input = self.run_menu(self.inventory_menu_options)
        if user_input == 1:
            print("asd")
        elif user_input == 2:
            print("Varastotilanne")
        elif user_input == 0:
            return 0
        
        
        
    def ingredients_menu(self):
        user_input = self.run_menu(self.ingredients_menu_options)
        if user_input == 1:
            print("Lisätietoja")
        elif user_input == 2:
            print("Listataan raaka-aineet")
        elif user_input == 0:
            return 0
    
if __name__ == "__main__":
    program = Main()
    program.main_menu()
    print("Exit")