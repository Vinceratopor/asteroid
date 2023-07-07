#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:29:51 2023

@author: stagiaire_letg
"""

import random

class Asteroid:
  def __init__(self,speed,angle,size):
    self.speed = speed
    self.angle = angle
    self.size = size

  def getSpeed(self):
    return self.speed
  def getAngle(self):
    return self.angle
  def getSize(self):
    return self.size

  def setSpeed(self,speed):
    self.speed = speed
  def setAngle(self,angle):
    self.angle = angle
  def setSpeed(self,size):
    self.size = size

  def gettingShot(self):
    Asteroid a1(self.speed,random.randint(1, 360), self.size-1)
