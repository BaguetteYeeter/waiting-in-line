import pygame             #add the pygame library

from init import *        #add init.py   (init)
from screen import *      #add screen.py (screen.)
from config import *      #add config.py (read_config)
from game import *        #add game.py   (run_game)

def main():                                          #make the main function, TODO: new name?
    mainScreen.fill((0, 0, 0))                       #make the screen black
    rect = pygame.Rect((50, 50), (100, 100))         #make a rectangle at (50,50) and width and height of 100
    pygame.draw.rect(mainScreen, (0, 50, 250), rect) #draw the rectangle to the screen in #0032FA
    pygame.display.update()                          #update the display
    run_game()                                       #run the game loop in game.py

if __name__ == "__main__":             #if running this file, not importing
    init()                             #run the init function from init.py
    mainScreen = screen.pygame_init()  #run pygame_init from screen.py, it returns the mainScreen variable
    main()                             #run the main function from above
