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

mass_units = [G, KG, PORTION]
volume_units = [TSP, TBLSP, CL, DL, L, PIECE]
    
mass_unit_relations = {G : 1, PORTION : 500, KG : 1000}                                 #sovitaan, etta portion = 500g
volume_unit_relations = {TSP : 5, TBLSP : 15, CL : 10, DL : 100, L : 1000, PIECE : 150} #sovitaan, etta piece = 150ml



class Unit_transfer:
    
    def __init__(self):
        self.transferred_amount = None
        
    def unit_transfer(self, received_unit, wanted_unit, received_amount, density):
        if received_unit in mass_units and wanted_unit in mass_units:
            self.transferred_amount = self.mass_to_mass(received_unit, wanted_unit, received_amount, density)
        elif received_unit in volume_units and wanted_unit in volume_units:
            self.transferred_amount = self.volume_to_volume(received_unit, wanted_unit, received_amount, density)
        elif received_unit in mass_units and wanted_unit in volume_units:
            self.transferred_amount = self.mass_to_volume(received_unit, wanted_unit, received_amount, density)
        elif received_unit in volume_units and wanted_unit in mass_units:
            self.transferred_amount = self.volume_to_mass(received_unit, wanted_unit, received_amount, density)
        return self.transferred_amount
     
    def mass_to_mass(self, received_unit, wanted_unit, received_amount, density):
        multiplier = mass_unit_relations[received_unit]/mass_unit_relations[wanted_unit]
        return received_amount * multiplier
    
    def volume_to_volume(self, received_unit, wanted_unit, received_amount, density):
        multiplier = volume_unit_relations[received_unit]/volume_unit_relations[wanted_unit]
        return received_amount * multiplier

    def mass_to_volume(self, received_unit, wanted_unit, received_amount, density):
        #muutetaan verrokkiarvoihin litra ja kg
        mass_to_kg_multiplier = mass_unit_relations[received_unit]/mass_unit_relations[KG]
        volume_to_l_multiplier = volume_unit_relations[wanted_unit]/ volume_unit_relations[L]
        received_mass_kg = received_amount * mass_to_kg_multiplier
        received_volume_l = received_mass_kg/density
        return received_volume_l / volume_to_l_multiplier
    
    def volume_to_mass(self, received_unit, wanted_unit, received_amount, density):
        #muutetaan verrokkiarvoihin litra ja kg
        mass_to_kg_multiplier = mass_unit_relations[wanted_unit]/mass_unit_relations[KG]
        volume_to_l_multiplier = volume_unit_relations[received_unit]/ volume_unit_relations[L]
        received_volume_l = received_amount * volume_to_l_multiplier
        received_mass_kg = received_volume_l * density
        return received_mass_kg / mass_to_kg_multiplier