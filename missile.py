#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:19:32 2023

@author: stagiaire_letg
"""
import math 

class Missile:
    def __init__(self, x, y, angle, speed, lifespan):
        self.x = x  # Coordonnée x
        self.y = y  # Coordonnée y
        self.angle = angle  # Angle de déplacement
        self.speed = speed  # Vitesse de déplacement
        self.lifespan = lifespan  # Durée de vie restante

    def update(self, delta_time):
        # Mettre à jour la position en fonction de l'angle et de la vitesse
        self.x += self.speed * delta_time * math.cos(math.radians(self.angle))
        self.y += self.speed * delta_time * math.sin(math.radians(self.angle))

        # Mettre à jour la durée de vie restante
        self.lifespan -= delta_time

    def is_expired(self):
        # Vérifier si le missile a expiré (durée de vie nulle ou négative)
        return self.lifespan <= 0
