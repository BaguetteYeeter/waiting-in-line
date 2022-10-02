import pygame #add the pygame library

def run_game():                             #make the run_game function
    while True:                             #infinite loop
        for event in pygame.event.get():    #get all events and iterate through them
            if event.type == pygame.QUIT:   #if the event is quit (press x button)
                return                      #exit the function
