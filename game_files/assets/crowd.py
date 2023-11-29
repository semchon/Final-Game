import os
import pygame
import random
import time
class Crowd(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        rand = random.randint(1,5)
        image1_big = pygame.image.load(f"images/crowd_sprites/crowd{rand}_1.png")
        self.image1 = pygame.transform.scale(image1_big, (230,230))
        self.image2 = pygame.image.load(f"images/crowd_sprites/crowd{rand}_2.png")
        self.image3 = pygame.image.load(f"images/crowd_sprites/crowd{rand}_3.png")
        self.image1.set_colorkey((255,255,255))
        self.image2.set_colorkey((255,255,255))
        self.image3.set_colorkey((255,255,255))
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.index = 0
        self.time_bookmark = pygame.time.get_ticks()

    def draw_crowd(self, surf):
            surf.blit(self.image, self.rect)


    def crowd_clap(self,permutations):
        framerate = 500
        crowd_frame = 0
        images = [self.image1,self.image2,self.image3]
        for i in range(permutations):
            current_time = pygame.time.get_ticks()
            if current_time - self.time_bookmark >= framerate:
                crowd_frame += 1
                self.time_bookmark = current_time
                if crowd_frame%2 == 1:
                    self.image = self.image2
                if crowd_frame%2 == 0:
                    self.image = self.image3




        for i in range(permutations):
            self.image = self.image2
            self.image = self.image3
        self.image = self.image1


crowd = pygame.sprite.Group()



