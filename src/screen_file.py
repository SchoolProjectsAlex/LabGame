import pygame  # importera pygame

def create_screen():
# skapa skärmen
 screen = pygame.display.set_mode((900, 500))  # (widh,height)
 clock = pygame.time.Clock()  # hjälper till med tid och kontrollera framerate


 return create_screen