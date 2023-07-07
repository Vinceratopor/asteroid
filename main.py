#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:29:15 2023

@author: stagiaire_letg
"""
from asteroid import Asteroid 
import time

def main():
    print('Press space to start')
    
    
    
    #Initialisation
    # Création d'un astéroïde
    asteroid = Asteroid(100, 100, 3)
    # Au début de la boucle de jeu
    start_time = time.time()
    # Boucle de jeu
    while True:
        # Mise à jour du mouvement de l'astéroïde
        
        # À chaque mise à jour du jeu
        current_time = time.time()
        delta_time = current_time - start_time
        start_time = current_time
        
        asteroid.update(delta_time)


main()