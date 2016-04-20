'''
Created on Apr 19, 2016
@author: saarnii1
'''
# -*- coding: utf-8 -*-
import io

class read_inventory:
    '''
    Katsotaan varasto läpi eli selvitetään mitä kaikkia raaka-aineita on käytettävissä
    '''
    try:
        with open('inventory') as inventory:
            lineCount = 0
            characterCount = 0
            for line in inventory:
                '''
                line_tmp = line.split('!')      #tiedostossa siis raaka-aine, sen määrä ja muut tiedot erotettu huutomerkillä
                line_tmp[0] = ingredient
                line_tmp[1] = amount
                line_tmp[2] = unit
                line_tmp[3] = reseptit
                line_tmp[4] = allergeenit
                '''
                
                
    except OSError:
        print("Could not open inventory")
    


class find_recipes:
    
    '''
    Eli etsi_ruoka
    Määritellää tarkemmin sitä, mitä lähdetään hakemaan:
    määritellään ehdot sille, millä ehdoilla ohjelman kehittämä lista halutaan muodostaa.
    '''
        
    def no_conditions(self):
        '''
        etsi reseptit, kunkäyttäjä ei aseta ehtoja ruuan raaka-aineista ja määristä
        '''
        
    def missing_n_ingredients(self):
        '''
        etsi reseptit, joiden valmistamiseksi puuttuu korkeintaa n raaka-ainetta
        '''
        
    def must_not_include(self):
        '''
        etsi reseptit, jotka eivät saa sisältää tiettyö raaka-ainetta
        '''
    
    def must_include(self):
        '''
        etsi reseptit, joiden halutaan sisältävän tiettyä raaka-ainetta
        '''