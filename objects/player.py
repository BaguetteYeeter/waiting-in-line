import pygame               #add the pygame library
from config import *        #add config.py
config = read_config()      #read the config

class Player(pygame.sprite.Sprite):     #make a player thats a sprite
    def __init__(self):                 #make __init__ (used for objects)
        super().__init__()              #i dont know
        self.image = pygame.Surface((100, 100))              #make a blank surface with 100x100
        self.rect = pygame.Rect((50, 50), (100, 100))        #make a rectangle at 50,50 with 100x100
        pygame.draw.rect(self.image,(0, 50, 250), self.rect) #draw the rectangle on the surface (how did this even get into prod)
    def move(self, keys):                        #make a move function
        speed = int(300/config["screen"]["fps"]) #speed is 300/fps because i said so
        if keys[pygame.K_a]:                     #if a is pressed
            self.rect.x -= speed                 #go left by speed
        if keys[pygame.K_d]:                     #if d is pressed
            self.rect.x += speed                 #go right by speed
        if keys[pygame.K_w]:                     #if w is pressed
            self.rect.y -= speed                 #go up
        if keys[pygame.K_s]:                     #if s is pressed
            self.rect.y += speed                 #go down
