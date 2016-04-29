'''
Created on Apr 20, 2016
@author: saarnii1
'''
# -*- coding: utf-8 -*-
from ingredient import Ingredient, Ingredient_container
from recipe import Recipe

class IO(object):

    def read_ingredients_from_file(self, input_data):
        self.name = False
        self.density = False
        self.ingredient_list = []
        self.succesfull_reads = 0
        self.failed_reads = 0
        current_line = ''
        
        try:
            #input_data = open(filename, 'w')
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            if header_parts[0].strip() != "INGREDIENTLIST" :   
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
                            #print(self.ingredient.get_name())
                            
                        elif header_parts[0].strip().lower() == 'density':
                            if self.ingredient.set_density(header_parts[1].strip()):
                                #print(self.ingredient.get_density())
                                self.density = True
                            else:
                                break
                            
                            
                        elif header_parts[0].strip().lower() == 'recipe':
                            self.ingredient.set_recipe(header_parts[1].strip())
                            self.instructions = True
                            
                        elif header_parts[0].strip().lower() == 'allergen':
                            self.ingredient.set_allergen(header_parts[1].strip()) 
                            #print(self.ingredient)
                        
                                
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
                    
            #input_data.close()     
            return self.ingredient_list, self.succesfull_reads, self.failed_reads
        except OSError:
            print("Tiedoston avaaminen ei onnistunut")
            
            
    def read_recipes_from_file(self, input_data, ingredients_list):
        self.name = False
        self.instructions = False
        self.ingedients = False
        self.outcome = False
        self.recipes_list = []
        self.succesfull_reads = 0
        self.failed_reads = 0
        current_line = ''
        
        try:
            #input_data = open(filename, 'w')
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            if header_parts[0].strip() != "RECIPELIST" :   
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
                            print(self.recipe.get_name())
                            
                        elif header_parts[0].strip().lower() == 'instructions':
                            self.recipe.set_instructions(header_parts[1].strip())
                            self.instructions = True
                            print(self.recipe.get_instructions())
                            
                            
                        elif header_parts[0].strip().lower() == 'outcome':
                            if len(header_parts) != 3: break
                            self.recipe.set_outcome_amount(header_parts[1].strip())
                            self.recipe.set_outcome_unit(header_parts[2].strip())
                            self.outcome = True
                            
                        elif header_parts[0].strip().lower() == 'ingredient':
                            if len(header_parts) != 4:
                                self.ingredients = False
                                break
                            self.ingredient_container = Ingredient_container()
                            if self.ingredient_container.set_ingredient(header_parts[1].strip(), ingredients_list):
                                self.ingredients = True
                            else:
                                self.ingredients = False
                                break
                            self.ingredient_container.set_amount(header_parts[2].strip())
                            self.ingredient_container.set_unit(header_parts[3].strip())
                            self.recipe.add_ingredients(self.ingredient_container)
                        
                                
                        current_line = input_data.readline()
                        header_parts = current_line.split(":")
                        
                    if not self.name or not self.instructions or not self.ingedients or not self.outcome:
                        if self.name:
                            print("Seuraavan reseptin lukeminen epaonnistui:", self.name)
                        else:
                            print("Reseptin luku epaonnistui")
                        self.failed_reads += 1
                            
                    else:
                        self.recipes_list.append(self.ingredient)
                        self.name = False
                        self.instructions = False
                        self.ingredients = False
                        self.outcome = False
                        self.succesfull_reads += 1
                else:
                    current_line = input_data.readline()
                    header_parts = current_line.split(" ")
                    
            #input_data.close()     
            return self.recipes_list, self.succesfull_reads, self.failed_reads
        except OSError:
            print("Tiedoston avaaminen ei onnistunut")
        

'''    
    def read_storage_from_file(self, input_data, ingredients_list):
        self.success = None
        self.storage_list = []
        self.succesfull_reads = 0
        self.failed_reads = 0
        current_line = ''
        
        try:
            #input_data = open(filename, 'w')
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            if header_parts[0].strip() != "STORAGELIST" :   
                raise OSError("Tuntematon tiedostotyyppi")
            
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            while current_line != '': 
                if len(header_parts) > 2:
                    self.ingedient_container = 
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
                            
                        elif header_parts[0].strip().lower() == 'recipe':
                            self.ingredient.set_recipe(header_parts[1].strip())
                            self.instructions = True
                            
                        elif header_parts[0].strip().lower() == 'outcome':
                            if len(header_parts) != 3: break
                            self.recipe.set_outcome_amount(header_parts[1].strip())
                            self.recipe.set_outcome_unit(header_parts[2].strip())
                            self.outcome = True
                        
                                
                        current_line = input_data.readline()
                        header_parts = current_line.split(":")
                        
                    if not self.name or not self.instructions or not self.ingedients or not self.outcome:
                        if self.name:
                            print("Seuraavan reseptin lukeminen epaonnistui:", self.name)
                        else:
                            print("Reseptin luku epaonnistui")
                            
                    else:
                        self.recipes_list.append(self.ingredient)
                        self.name = False
                        self.instructions = False
                        self.ingredients = False
                        self.outcome = False
                else:
                    current_line = input_data.readline()
                    header_parts = current_line.split(" ")
                    
            #input_data.close()     
            return self.resipes_list
        except OSError:
            print("Tiedoston avaaminen ei onnistunut")  
'''