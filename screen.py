import pygame

class screen:
    def pygame_init():
        global mainScreen
        pygame.init()
        mainScreen = pygame.display.set_mode((500, 500))
        return mainScreen
