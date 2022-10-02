import pygame                #add the pygame library
from objects.player import * #include objects/player.py
from config import *         #include config.py
from screen import *

def run_game(mainScreen):                      #make the run_game function
    clock = pygame.time.Clock()                #make a clock
    player = Player()                          #make a player with the player object (player.py)
    player_group = pygame.sprite.Group(player) #make a sprite group with the player
    config = read_config()                     #read the config
    while True:                                #infinite loop
        resolution = get_res()
        mainScreen.fill((0, 0, 0))             #make the screen BLANK
        clock.tick(config["screen"]["fps"])    #run the loop fps times a second (adam f - circles pola & bryson bootleg)
        for event in pygame.event.get():       #get all events and iterate through them
            if event.type == pygame.QUIT:      #if the event is quit (press x button)
                return                         #exit the function
            if event.type == pygame.VIDEORESIZE:
                change_res((event.w, event.h))
                #mainScreen = screen.pygame_init()
        keys = pygame.key.get_pressed()        #get all pressed keys
        player.move(keys)                      #move the player according to keys
        player_group.draw(mainScreen)          #draw the player
        pygame.display.update()                #update the display
