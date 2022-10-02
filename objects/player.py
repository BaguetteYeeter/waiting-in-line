import pygame               #add the pygame library
from config import *        #add config.py
config = read_config()      #read the config
import random

class Player(pygame.sprite.Sprite):     #make a player thats a sprite
    def __init__(self):                 #make __init__ (used for objects)
        super().__init__()              #i dont know
        self.image = pygame.Surface((50, 50))              #make a blank surface with 100x100
        self.rect = pygame.Rect((0, 0), (50, 50))        #make a rectangle at 50,50 with 100x100
        pygame.draw.rect(self.image,(0, 50, 250), self.rect) #draw the rectangle on the surface (how did this even get into prod)
        self.velocity = [3, 3]
    def move(self, keys):                        #make a move function
        speed = 5
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])
        if self.rect.x <= 0:
            self.velocity[0] = 0-(self.velocity[0])
        if self.rect.y <= 0:
            self.velocity[1] = 0-(self.velocity[1])
        if self.rect.x >= config["screen"]["resolution"][0]-50:
            self.velocity[0] = 0-(self.velocity[0])
        if self.rect.y >= config["screen"]["resolution"][1]-50:
            self.velocity[1] = 0-(self.velocity[1])
        if (
            (self.rect.x == 0 and self.rect.y == 0) or
            (self.rect.x == 0 and self.rect.y >= config["screen"]["resolution"][1]-50) or
            (self.rect.x >= config["screen"]["resolution"][0]-50 and self.rect.y == 0) or
            (self.rect.x >= config["screen"]["resolution"][0]-50 and self.rect.y >= config["screen"]["resolution"][1]-50)
        ):
            print("CORNER!!!!!!!!!!")
