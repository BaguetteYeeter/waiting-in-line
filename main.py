import pygame

from init import *
from screen import *
from config import *
from game import *

def main():
    mainScreen.fill((0, 0, 0))
    rect = pygame.Rect((50, 50), (100, 100))
    pygame.draw.rect(mainScreen, (0, 50, 250), rect)
    pygame.display.update()
    run_game()

if __name__ == "__main__":
    init()
    mainScreen = screen.pygame_init()
    main()
