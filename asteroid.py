#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:29:51 2023

@author: stagiaire_letg
"""

import random

class Asteroid:
    def __init__(self, x, y, size):
        self.x = x  # Coordonnée x
        self.y = y  # Coordonnée y
        self.size = size  # Taille de l'astéroïde

        self.speed_x = random.uniform(-2, 2)  # Vitesse de déplacement en x (aléatoire)
        self.speed_y = random.uniform(-2, 2)  # Vitesse de déplacement en y (aléatoire)

    def update(self, delta_time):
        # Mettre à jour la position en fonction de la vitesse et du temps écoulé
        self.x += self.speed_x * delta_time
        self.y += self.speed_y * delta_time

    def hit(self):
        # Méthode appelée lorsque l'astéroïde est touché
        # Implémentez ici le comportement souhaité lorsque l'astéroïde est touché par un tir
        # Par exemple, vous pouvez le diviser en plusieurs astéroïdes plus petits

        # Exemple de comportement : Diviser l'astéroïde en deux astéroïdes plus petits
        if self.size > 1:
            new_size = self.size - 1
            new_asteroid1 = Asteroid(self.x, self.y, new_size)
            new_asteroid2 = Asteroid(self.x, self.y, new_size)
            return [new_asteroid1, new_asteroid2]
        else:
            # Si l'astéroïde est de taille 1 ou plus petite, il est détruit
            return []
      
    
    
