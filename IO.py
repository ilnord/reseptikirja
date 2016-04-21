'''
Created on Apr 20, 2016
@author: saarnii1
'''
# -*- coding: utf-8 -*-

import json

class Mod_inventory:
    
    def write_to_inventory(self, data, filename):
        try:
            json_data = json.dumps(data, indent=4, skipkeys=True, sort_keys=True)
            inventory = open(filename, 'w')
            inventory.write(json_data)
            inventory.close()     
             
            '''
            line_tmp = line.split('!')      #tiedostossa siis raaka-aine, sen määrä ja muut tiedot erotettu huutomerkillä
            line_tmp[0] = ingredient
            line_tmp[1] = amount
            line_tmp[2] = unit
            line_tmp[3] = reseptit
            line_tmp[4] = allergeenit
            '''               
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