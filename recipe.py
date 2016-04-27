'''
Created on 20.4.2016

@author: Ilkka
'''
# -*- coding: utf-8 -*-
class Recipe:
    
    def __init__(self):
        self.name = None
        self.instructions = []
        self.ingredients = []
        
    def set_name(self, name):
        self.name = name
        
    def set_instructions(self, instructions):
        self.instructions.append(instructions)
        
    def set_ingredients(self, ingredients):
        self.ingredients.append(ingredients)
        
    def set_outcome_amount(self, outcomeSize):
        self.outcomeSize = outcomeSize
        
    def set_outcome_unit(self, outcomeUnit):
        self.outcomeUnit = outcomeUnit

        
    def get_name(self):
        return self.name
    def get_instructions(self):
        return self.instructions
    def get_ingredients(self):
        return self.ingredients