import pygame
from dfs import *

class Statistics:
    def __init__(self,screen):
        self.BLOCK_SIZE = 20
        self.LEFT_INDENT = 100
        self.UPPER_INDENT = 10
        self.size = (self.LEFT_INDENT + 43 * self.BLOCK_SIZE, self.UPPER_INDENT + 22 * self.BLOCK_SIZE)
        self.screen = screen
        self.font_size = int(self.BLOCK_SIZE / 1.5)
        self.font = pygame.font.SysFont('arial', self.font_size)
        self.BLACK = (0, 0, 0)


    def print_stats(self,time_complexity,memory_complexity,iterations,name_of_alg):

        text_t = self.font.render('Time complexity '+name_of_alg +' (seconds): '+ str(time_complexity), True, self.BLACK)
        textRect_t = text_t.get_rect()
        textRect_t.center = (3* self.LEFT_INDENT,30 * self.UPPER_INDENT)
        self.screen.blit(text_t, textRect_t)
        text_m = self.font.render('Memory complexity ' + name_of_alg + ' (bytes): ' + str(memory_complexity), True, self.BLACK)
        textRect_m = text_m.get_rect()
        textRect_m.center = (3 * self.LEFT_INDENT , 32 * self.UPPER_INDENT)
        self.screen.blit(text_m, textRect_m)
        text_i = self.font.render('Iterations ' + name_of_alg + ' : ' + str(iterations), True, self.BLACK)
        textRect_i = text_i.get_rect()
        textRect_i.center = (3 * self.LEFT_INDENT , 34 * self.UPPER_INDENT)
        self.screen.blit(text_i, textRect_i)


