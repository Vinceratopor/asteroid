import pygame
import math

class Spaceship:
    def __init__(self, x, y):
        self.x = x  # Coordonnée x
        self.y = y  # Coordonnée y
        self.angle = 0  # Angle de rotation du vaisseau
        self.speed = 0  # Vitesse de déplacement du vaisseau
        self.acceleration = 0.1  # Accélération du vaisseau
        self.rotation_speed = 3  # Vitesse de rotation du vaisseau

    def rotate(self, direction):
        # Rotation du vaisseau dans une direction donnée (gauche ou droite)
        self.angle += direction * self.rotation_speed

    def accelerate(self):
        # Accélération du vaisseau dans la direction actuelle
        self.speed += self.acceleration

    def decelerate(self):
        # Ralentissement du vaisseau
        self.speed -= self.acceleration

    def update(self, delta_time):
        # Mise à jour de la position en fonction de l'angle et de la vitesse
        self.x += self.speed * delta_time * math.cos(math.radians(self.angle))
        self.y += self.speed * delta_time * math.sin(math.radians(self.angle))

