import os
import pygame
import random
import time
class Crowd(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        rand = random.randint(1,5)
        image1_big = pygame.image.load(f"images/crowd_sprites/crowd1_1.png")
        image2_big = pygame.image.load(f"images/crowd_sprites/crowd1_2.png")
        image3_big = pygame.image.load(f"images/crowd_sprites/crowd1_3.png")
        self.image1 = pygame.transform.scale(image1_big, (400,400))
        self.image2 = pygame.transform.scale(image2_big, (400, 400))
        self.image3 = pygame.transform.scale(image3_big, (230, 230))
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

    def draw_crowd(self, surf,x,y):
        self.image = self.image2
        surf.blit(self.image, (x,y))

    def draw_crowd_clapping(self, surf,x,y):
        self.image = self.image1
        surf.blit(self.image, (x,y))


    def crowd_clap(self,surf,permutations):
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
                    surf.blit(self.image, (100,100))
                if crowd_frame%2 == 0:
                    self.image = self.image3
                    surf.blit(self.image, (100, 100))



crowd = pygame.sprite.Group()



