'''
Created on Apr 20, 2016
@author: saarnii1
'''
# -*- coding: utf-8 -*-
from ingredient import Ingredient


class IO:
    
    '''
    def write_to_inventory(self, data, filename):
        try:
            json_data = json.dumps(data, indent=4, skipkeys=True, sort_keys=True)
            inventory = open(filename, 'w')
            inventory.write(json_data)
            inventory.close()     
             
            line_tmp = line.split('!')      #tiedostossa siis raaka-aine, sen määrä ja muut tiedot erotettu huutomerkillä
            line_tmp[0] = ingredient
            line_tmp[1] = amount
            line_tmp[2] = unit
            line_tmp[3] = reseptit
            line_tmp[4] = allergeenit               
        except:         #OS error?
            print("Could not write to inventory")
        

    def read_from_inventory(self, filename):
        returndata = {}
        try:
            inventory = open(filename, 'r')
            text = inventory.read()
            inventory.close()
            returndata = json.loads(text)
        except:
            print("Could not open inventory")
        return returndata
        
    '''
    def read_ingredients_from_file(self, filename):
        self.name = False
        self.density = False
        self.ingredientList = []
        
        try:
            input_data = open(filename, 'w')
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            if header_parts[0].strip() != "INGREDIENTLIST" :   
                raise OSError("Tuntematon tiedostotyyppi")
            
            current_line = input_data.readline()
            header_parts = current_line.split(" ")
            
            while current_line != '': 
                if header_parts[0].strip().lower() == '#ingredient':
                    self.ingedient = Ingredient()
                    current_line = input_data.readline()
                    header_parts = current_line.split(":")
                    
                    while current_line != '':
                        if current_line[0] == '#':
                            break
                        
                        elif header_parts[0].strip().lower() == 'name':
                            self.ingredient.setName(header_parts[1].strip())
                            self.name = header_parts[1].strip()
                            
                        elif header_parts[0].strip().lower() == 'density':
                            if self.ingredient.setDensity(header_parts[1].strip()):
                                self.density = True
                                
                        elif header_parts[0].strip().lower() == 'instruction':
                            self.recipe.addInstruction(header_parts[1].strip())
                            self.instructions = True
                            
                        elif header_parts[0].strip().lower() == 'outcome':
                            if len(header_parts) != 3: break
                            self.recipe.setOutcomeSize(header_parts[1].strip())
                            self.recipe.setOutcomeUnit(header_parts[2].strip())
                            self.outcome = True   
                            
                        elif header_parts[0].strip().lower() == 'ingredient':
                            if len(header_parts) != 4:
                                self.ingredients = False
                                break
                            self.ingredientContainer = IngredientContainer()
                            if self.ingredientContainer.setIngredient(header_parts[1].strip(), ingredientsList):
                                self.ingredients = True
                            else:
                                self.ingredients = False
                                break
                            self.ingredientContainer.setQuantity(header_parts[2].strip())
                            self.ingredientContainer.setUnit(header_parts[3].strip())
                            self.recipe.addIngredient(self.ingredientContainer)
                                
                        current_line = input_data.readline()
                        header_parts = current_line.split(":")
                        
                    if not self.name or not self.instructions or not self.ingredients or not self.outcome:
                        if self.name:
                            print("Seuraavan reseptin lukeminen epäonnistui:", self.name)
                        else:
                            print("Reseptin luku epäonnistui, jatketaan silti.")
                            
                    else:
                        self.succesCount +=1
                        self.ingredientList.append(self.ingredient)
                        self.name = False
                        self.density = False
                else:
                    currentLine = input_data.readline()
                    header_parts = currentLine.split(" ")
                    
            input_data.close()     
            return self.ingredientList,self.succesCount,self.errorCount
        except OSError:
            print("Tiedoston avaaminen ei onnistunut")
            