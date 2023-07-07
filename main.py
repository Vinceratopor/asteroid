#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:29:15 2023

@author: stagiaire_letg
"""
from asteroid import Asteroid 
from spaceship import Spaceship 
from missile import Missile 
from GUI import GUI 

import random
import time
import pygame

# Définition des constantes de couleur
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
largeur_fenetre = 800
hauteur_fenetre = 600

# Initialisation de Pygame
pygame.init()


def draw_elements(gui, spaceship, missiles, asteroids):
    gui.clear_screen()

    # Dessin du vaisseau spatial
    gui.draw_ship(spaceship)

    # Dessin des missiles
    for missile in missiles:
        gui.draw_missile(missile)

    # Dessin des astéroïdes
    for asteroid in asteroids:
        gui.draw_asteroid(asteroid)

    # Mise à jour de l'écran
    gui.update_screen()



# Fonction principale du jeu
def main():
    # Initialisation de la GUI
    gui = GUI(largeur_fenetre, hauteur_fenetre)

    # Création du vaisseau spatial
    spaceship = Spaceship(largeur_fenetre / 2, hauteur_fenetre / 2)

    # Création des astéroïdes
    asteroids = []
    for _ in range(5):
        x = random.uniform(0, largeur_fenetre)
        y = random.uniform(0, hauteur_fenetre)
        size = random.randint(10, 50)
        asteroid = Asteroid(x, y, size)
        asteroids.append(asteroid)

    # Création de la liste des missiles
    missiles = []

    # Boucle de jeu
    while True:
        # Vérification des événements
        if gui.check_quit_event():
            break

        # Effacer l'écran
        gui.clear_screen()

        # Mise à jour du vaisseau spatial
        spaceship.update(gui.get_delta_time())

        # Mise à jour des astéroïdes
        for asteroid in asteroids:
            asteroid.update(gui.get_delta_time())

        # Mise à jour des missiles
        for missile in missiles:
            missile.update(gui.get_delta_time())

        # Affichage des éléments
        draw_elements(gui, spaceship, missiles, asteroids)

    # Fermeture de la GUI
    gui.close()


main()