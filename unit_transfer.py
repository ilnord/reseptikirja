'''
Created on 21.4.2016

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

mass_units = [G, KG, PORTION]                   #sovitan vaikka etta portion = 500g
volume_units = [TSP, TBLSP, CL, DL, L, PIECE]

mass_unit_relations = {G : 1, PORTION : 500, KG : 1000}
volume_unit_relations = {TSP : 5, TBLSP : 15, CL : 10, DL : 100, L : 10000, PIECE : 150}

class Unit_transfer:
    
    def __init__(self):
        self.transferred_amount = None
        
    def unit_transfer(self, received_unit, wanted_unit, density, received_amount):
        if received_unit in mass_units and wanted_unit in mass_units:
            self.transferred_amount = self.mass_to_mass(received_unit, wanted_unit, density, received_amount)
        elif received_unit in volume_units and wanted_unit in volume_units:
            self.transferred_amount = self.volume_to_volume(received_unit, wanted_unit, density, received_amount)
        elif received_unit in mass_units and wanted_unit in volume_units:
            self.transferred_amount = self.mass_to_volume(received_unit, wanted_unit, density, received_amount)
        elif received_unit in volume_units and wanted_unit in mass_units:
            self.transferred_amount = self.volume_to_mass(received_unit, wanted_unit, density, received_amount)
        return self.transferred_amount
     
    def mass_to_mass(self, received_unit, wanted_unit, density, received_amount):
        multiplier = mass_unit_relations[received_unit]/mass_unit_relations[wanted_unit]
        return received_amount * multiplier
    
    def volume_to_volume(self, received_unit, wanted_unit, density, received_amount):
        multiplier = volume_unit_relations[received_unit]/volume_unit_relations[wanted_unit]
        return received_amount * multiplier

    def mass_to_volume(self, received_unit, wanted_unit, density, received_amount):
        global transferred_amount
        if received_unit == G:
            if wanted_unit == TSP:
                self.transferred_amount = (received_amount/density)/5
                return self.transferred_amount 
            elif wanted_unit == TBLSP:
                self.transferred_amount == (received_amount/density)/15
                return transferred_amount
            elif wanted_unit == CL:
                transferred_amount == (received_amount/density)/10
                return transferred_amount
            elif wanted_unit == DL:
                transferred_amount == (received_amount/density)/100
                return transferred_amount
            elif wanted_unit == L:
                transferred_amount == (received_amount/density)/1000
                return transferred_amount
            return transferred_amount
        if received_unit == KG:
            if wanted_unit == TSP:
                transferred_amount = (received_amount/density)/0.005
                return transferred_amount
            elif wanted_unit == TBLSP:
                transferred_amount == (received_amount/density)/0.015
                return transferred_amount
            elif wanted_unit == CL:
                transferred_amount == (received_amount/density)/0.01
                return transferred_amount
            elif wanted_unit == DL:
                transferred_amount == (received_amount/density)/0.1
                return transferred_amount
            elif wanted_unit == L:
                transferred_amount == (received_amount/density)
                return transferred_amount
            else:
                IOError
            
    
    def volume_to_mass(self, received_unit, wanted_unit, density, received_amount):
        pass
    
             