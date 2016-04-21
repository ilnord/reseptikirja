'''
Created on 19.4.2016
@author: Ilkka
'''
# -*- coding: utf-8 -*-

class Main(object):
    
    def __init__(self):
        #Luodaan menut ja submenut
        self.main_menu_options = ["1.Hae resepteja", "2. Varasto", "3. Reseptit","4. Raaka-aineet", "0. Sulje ohjelma"]
        self.search_menu_options = ["1. Kerro lisätietoja reseptistä", "2. Reseptit, joissa raaka-aine esiintyy", \
                                    "3. Sopii allergikolle", "4. Reseptit, joihin varastotarvikkeet riittävät", "5. Reseptit, joista puuttuu N-määrä raaka-aineita varastosta", "6. Reseptit, joista löytyy N-määrä raaka-aineita varastosta", "0. Takaisin"]
        self.inventory_menu_options = ["1. Etsi tietty raaka-aine", "2. Listaa varasto", "0. Takaisin"]
        self.recipes_menu_options = ["1. Etsi tietty resepti", "2. Listaa reseptit", "0. Takaisin"]
        self.ingredients_menu_options = ["1. Etsi tietty raaka-aine", "2. Listaa raaka-aineet", "0. Takaisin"]
    
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
        user_input = int(user_input)  
        return user_input
    
    
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
                print("Etsi tehtävissä olevat reseptit")
            elif user_input == 2:
                print("Etsi ")
            elif user_input == 3:
                print("Tietoja")
            elif user_input == 4:
                print("Tietoja")
            elif user_input == 5:
                print("Tietoja")
            elif user_input == 1:
                print("Tietoja")
            elif user_input == 0:
                return 0
                
    def inventory_menu(self):
        user_input = self.run_menu(self.inventory_menu_options)
        if user_input == 1:
            print("Lisätietoja")
        elif user_input == 2:
            print("Varastotilanne")
        elif user_input == 0:
            return 0
        
    def recipes_menu(self):
        user_input = self.run_menu(self.recipes_menu_options)
        if user_input == 1:
            print("Lisätietoja")
        elif user_input == 2:
            print("Listataan reseptit")
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