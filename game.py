import pygame

def run_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
