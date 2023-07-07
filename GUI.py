#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:24:04 2023

@author: stagiaire_letg
"""

import pygame
import math

# Initialisation de Pygame
pygame.init()

# Définition des constantes de couleur
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)


class GUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def clear_screen(self):
        self.screen.fill(NOIR)

    def draw_asteroid(self, asteroid):
        pygame.draw.circle(self.screen, BLANC, (int(asteroid.x), int(asteroid.y)), asteroid.size)

    def draw_ship(self, ship):
        # Dessiner le vaisseau à partir de son centre et de son angle
        ship_points = [
            (ship.x + math.cos(math.radians(ship.angle)) * 20, ship.y + math.sin(math.radians(ship.angle)) * 20),
            (ship.x + math.cos(math.radians(ship.angle - 140)) * 10, ship.y + math.sin(math.radians(ship.angle - 140)) * 10),
            (ship.x + math.cos(math.radians(ship.angle + 140)) * 10, ship.y + math.sin(math.radians(ship.angle + 140)) * 10)
        ]
        pygame.draw.polygon(self.screen, BLANC, ship_points)

    def draw_missile(self, missile):
        pygame.draw.circle(self.screen, BLANC, (int(missile.x), int(missile.y)), 3)

    def update_screen(self):
        pygame.display.flip()

    def get_delta_time(self):
        return self.clock.tick(60) / 1000.0

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def close(self):
        pygame.quit()