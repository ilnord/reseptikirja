'''
Created on 20.4.2016

@author: Ilkka
'''
G = 0
KG = 1
TSP = 2
TBLSP = 3
CL = 4
DL = 5
L = 6
PIECE = 7
PORTION = 8

# -*- coding: utf-8 -*-
class Recipe:
    
    def __init__(self):
        self.name = None
        self.instructions = []
        self.ingredients = []
        
    def set_name(self, name):
        #Asettaa reseptin nimen
        self.name = name
        
    def set_instructions(self, instructions):
        #Asettaa (ja lisaa) reseptille ohjeita
        self.instructions.append(instructions)
        
    def add_ingredients(self, Ingredient_container):
        #Lisaa reseptiin ainesosia
        self.ingredients.append(Ingredient_container)

        
    def set_outcome_amount(self, outcome_amount):
        #Asettaa arvon, joka kertoo paljonko valmista tuotetta syntyy
        self.outcome_amount = outcome_amount
        
    def set_outcome_unit(self, outcome_unit):
        #Kertoo valmistuvan tuotteen maaran yksikon
        self.outcome_unit = outcome_unit

        
    def get_name(self):
        #Palauttaa reseptin nimen
        return self.name
    def get_instructions(self):
        #Palauttaa reseptin ohjeet
        return self.instructions
    def get_ingredients(self):
        #Palauttaa reseptin vaatimat raaka-aineet
        return self.ingredients
    def get_outcome_unit(self):
        #Kertoo, missa yksikossa valmista ruokaa mitataan
        return self.outcome_unit
    def get_outcome_amount(self):
        #Kertoo, paljonko valmista ruokaa syntyy
        return self.outcome_amount