import os
import pygame
import random
import time

class Crowd(pygame.sprite.Sprite):

    def __init__(self,x,y):
        rand = random.randint(1,5)
        self.image1 = pygame.image.load(f"assets/crowd_sprites/crowd{rand}_1.png")
        self.image2 = pygame.image.load(f"assets/crowd_sprites/crowd{rand}_2.png")
        self.image3 = pygame.image.load(f"assets/crowd_sprites/crowd{rand}_3.png")
        self.image1.set_colorkey((255,255,255))
        self.image2.set_colorkey((255,255,255))
        self.image3.set_colorkey((255,255,255))
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.index = 0

    def draw_crowd(self, surf):
        surf.blit(self.image, self.rect)

    def crowd_clap(self,permutations):
        clock.tickrate(60)
        for i in range(permutations):
            self.image = self.image2
            self.image = self.image3
        self.image = self.image1


crowd =pygame.sprite.Group()



