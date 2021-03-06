'''
Created on Apr 20, 2016
@author: saarnii1
'''
# -*- coding: utf-8 -*-
from ingredient import Ingredient, Ingredient_holder
from recipe import Recipe

class IO(object):

    def read_ingredients_from_file(self, input_data):
        #Lukee raaka-aineet tiedostosta ja tallentaa saadut tiedot Ingredient olioon
        self.name = False
        self.density = False
        self.ingredient_list = []
        self.succesfull_reads = 0
        self.failed_reads = 0
        current_line = ''
        
        try:
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            if header_parts[0].strip() != "INGREDIENTS" :   
                raise OSError("Tuntematon tiedostotyyppi")
            
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            while current_line != '': 
                if header_parts[0].strip().lower() == '#ingredient':
                    self.ingredient = Ingredient()
                    current_line = input_data.readline()
                    header_parts = current_line.split(":")
                    
                    while current_line != '':
                        if current_line[0] == '#':
                            break
                        
                        elif header_parts[0].strip().lower() == 'name':
                            self.ingredient.set_name(header_parts[1].strip())
                            self.name = header_parts[1].strip()
                            
                        elif header_parts[0].strip().lower() == 'density':
                            if self.ingredient.set_density(header_parts[1].strip()):
                                self.density = True
                            else:
                                break
                            
                            
                        elif header_parts[0].strip().lower() == 'recipe':
                            self.ingredient.set_recipe(header_parts[1].strip())
                            
                        elif header_parts[0].strip().lower() == 'allergen':
                            self.ingredient.set_allergen(header_parts[1].strip()) 
                        
                                
                        current_line = input_data.readline()
                        header_parts = current_line.split(":")
                        
                    if not self.name or not self.density:
                        self.failed_reads += 1
                        if self.name:
                            print("Seuraavan raaka-aineen lukeminen epaonnistui:", self.name)
                        else:
                            print("Raaka-aineen luku epaonnistui")
                            
                    else:
                        self.ingredient_list.append(self.ingredient)
                        self.succesfull_reads += 1
                        self.name = False
                        self.density = False
                else:
                    current_line = input_data.readline()
                    header_parts = current_line.split(" ")
                       
            return self.ingredient_list, self.succesfull_reads, self.failed_reads
        except OSError:
            print("Tiedoston avaaminen ei onnistunut")
            
            
    def read_recipes_from_file(self, input_data, ingredients_list):
        #Lukee reseptit tiedostosta ja tallentaa saadut tiedot resepti olioon
        
        self.name = False
        self.instructions = False
        self.ingedients = False
        self.outcome = False
        self.recipes_list = []
        self.succesfull_reads = 0
        self.failed_reads = 0
        current_line = ''
        
        try:
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            if header_parts[0].strip() != "RECIPES" :   
                raise OSError("Tuntematon tiedostotyyppi")
            
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            while current_line != '': 
                if header_parts[0].strip().lower() == '#recipe':
                    self.recipe = Recipe()
                    current_line = input_data.readline()
                    header_parts = current_line.split(":")
                    
                    while current_line != '':
                        if current_line[0] == '#':
                            break
                        
                        elif header_parts[0].strip().lower() == 'name':
                            self.recipe.set_name(header_parts[1].strip())
                            self.name = header_parts[1].strip()
                            
                        elif header_parts[0].strip().lower() == 'instructions':
                            self.recipe.set_instructions(header_parts[1].strip())
                            self.instructions = True
                                                      
                        elif header_parts[0].strip().lower() == 'outcome':
                            if len(header_parts) != 3: break
                            self.recipe.set_outcome_amount(header_parts[1].strip())
                            self.recipe.set_outcome_unit(header_parts[2].strip())
                            self.outcome = True
                            
                        elif header_parts[0].strip().lower() == 'ingredient':
                            if len(header_parts) != 4:
                                self.ingredients = False
                                break
                            self.ingredient_holder = Ingredient_holder()
                            if self.ingredient_holder.set_ingredient(header_parts[1].strip(), ingredients_list):
                                self.ingredients = True
                            else:
                                self.ingredients = False
                                break
                            self.ingredient_holder.set_amount(header_parts[2].strip())
                            self.ingredient_holder.set_unit(header_parts[3].strip())
                            self.recipe.add_ingredients(self.ingredient_holder)
                                
                        current_line = input_data.readline()
                        header_parts = current_line.split(":")
                        
                    if not self.name or not self.instructions or not self.ingredients or not self.outcome:
                        if self.name:
                            print("Seuraavan reseptin lukeminen epaonnistui:", self.name)
                        else:
                            print("Reseptin luku epaonnistui")
                        self.failed_reads += 1
                            
                    else:
                        self.recipes_list.append(self.recipe)
                        self.name = False
                        self.instructions = False
                        self.ingredients = False
                        self.outcome = False
                        self.succesfull_reads += 1
                else:
                    current_line = input_data.readline()
                    header_parts = current_line.split(" ")
                        
            return self.recipes_list, self.succesfull_reads, self.failed_reads
        except OSError:
            print("Tiedoston avaaminen ei onnistunut")
        

    
    def read_storage_from_file(self, input_data, ingredients_list):
        #Lukee varaston lapi ja tallentaa saadut tiedot Ingredient_container olioon
        
        self.success = None
        self.storage_list = []
        self.succesfull_reads = 0
        self.failed_reads = 0
        current_line = ''
        
        try:
            current_line = input_data.readline()
            header_parts = current_line.split(":")
            
            if header_parts[0].strip() != "STORAGE" :   
                raise OSError("Tuntematon tiedostotyyppi")
            
            current_line = input_data.readline()
            header_parts = current_line.split(":")
            
            while current_line != '': 
                if len(header_parts) > 2:
                    self.ingredient_holder = Ingredient_holder()
                    if not self.ingredient_holder.set_ingredient(header_parts[0].strip(), ingredients_list):
                        self.ingredients = False
                    else:
                        self.ingredient_holder.set_amount(header_parts[1].strip())
                        self.ingredient_holder.set_unit(header_parts[2].strip())
                        self.success = True
                        
                if not self.success:
                    self.failed_reads += 1
                    print("varastorivin luku epaonnitui")
                    self.success = None
                elif self.success:
                    self.succesfull_reads += 1
                    self.storage_list.append(self.ingredient_holder)
                    self.success = None
                current_line = input_data.readline()
                header_parts = current_line.split(":")
                
            return self.storage_list, self.succesfull_reads, self.failed_reads
        
        except OSError:
            print("ketuiks meni")
                    
