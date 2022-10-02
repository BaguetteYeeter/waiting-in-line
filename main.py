import pygame              #add the pygame library

from init import *         #add init.py   (init)
from screen import *       #add screen.py (screen.)
from config import *       #add config.py (read_config)
from game import *         #add game.py   (run_game)

def main():                                          #make the main function, TODO: new name?
    mainScreen.fill((0, 0, 0))                       #make the screen black
    run_game(mainScreen)                             #run the game loop in game.py

if __name__ == "__main__":             #if running this file, not importing
    init()                             #run the init function from init.py
    mainScreen = screen.pygame_init()  #run pygame_init from screen.py, it returns the mainScreen variable
    main()                             #run the main function from above
