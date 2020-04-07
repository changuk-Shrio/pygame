import pygame
from Setting import *
class Screen():
    def __init__(self,W,H,image):
        self.W=W
        self.H=H
        self.bg=pygame.image.load(image)
        self.screen=pygame.display.set_mode((self.W,self.H))
    def draw(self,s):
        self.screen.blit(self.bg, (0, 0))