import pygame
from Setting import *

class Enemy():
    def __init__(self,speed):
        self.speed=speed
        self.rect=pygame.Rect(100,100,50,50)

    def draw_Enemy(self,screen):
        pygame.draw.rect(screen,YELLOW,self.rect)

    def move_Enemy(self,x,y):
        if self.rect.left!=x:
            self.rect.centerx+=self.speed
        if self.rect.top!=y:
            self.rect.centery+=self.speed