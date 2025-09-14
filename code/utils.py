import pygame

class Menu:
    def __init__(self):
        pass
    
    def music_background(self):
        pygame.mixer.music.load("../music/music_fon.mp3")
        pygame.mixer.music.play(-1)