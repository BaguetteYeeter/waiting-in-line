import pygame #add the pygame library

class screen:                                            #make a class called screen
    def pygame_init():                                   #make a function called pygame_init
        global mainScreen                                #make the screen accessible everywhere
        pygame.init()                                    #initialize pygame
        mainScreen = pygame.display.set_mode((500, 500)) #make the screen with resolution 500x500, TODO: use config
        return mainScreen                                #return the mainScreen variable
