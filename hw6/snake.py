# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 20:13:51 2014

@author: bishiguro
"""
import pygame
import random

class Screen():
    def __init__(self, size = (700,700), screen_color= (255,255,255)): 
        self.size = size
        self.color = screen_color
    def screen_setup(self):
        size = (700,700)
        screen = pygame.display.set_mode(size) # ?
        pygame.display.set_caption("SNAKE")

class Grid():
    def __init__(self, screen,color=(0,0,0), width=50, height=50, margin = 5, num_rows=10, num_columns=10): 
        self.color = color
        self.width = width
        self.height = height
        self.margin = margin
        self.num_rows = num_rows
        self.num_columns = num_columns
        
    def grid_setup(self):
        grid = []
        for row in range(self.num_rows):
            grid.append([])
            for column in range(self.num_columns):
                grid[row].append(0)
    def draw_grid(self,screen): 
        for row in range(self.num_rows): 
            for column in range(self.num_columns): 
                pygame.draw.rect(screen,self.color,[(self.margin+self.width) * (self.num_columns+self.margin), (self.margin+self.height) * (self.num_rows+self.margin), self.width, self.height])
    
if __name__ == '__main__':
    prompt = raw_input("SNAKE \n Type 'play' to start a new game: ");
    if prompt.lower() == "play":
        game_screen = Screen()
        game_screen.screen_setup()
        
        game_grid = Grid(game_screen)
        game_grid.draw_grid()
        
        pygame.init()
        done = False
        clock = pygame.time.Clock() 
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True          
            game_screen.fill(game_screen.color)
            pygame.display.flip()
        pygame.quit()