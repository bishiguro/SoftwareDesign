# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 20:13:51 2014

@author: bishiguro
"""
import pygame
from pygame.locals import *
import random
import time

class SnakeModel:
    def __init__(self):
        self.playing_field = PlayingField()
        self.snake = Snake(3)
        self.pellet = Pellet(random.randint(0,200),random.randint(0,200)) # should this be completely random?
        
    def update(self): # update playing field + snake + food pellets
        self.playing_field.update()        
        self.snake.update() 
        self.pellet.update()

class PlayingField:
    def __init__(self):
        playing_field = []
        for i in range(200): # for each row of the playing field grid
            for j in range(200): # for each column of the playing field grid
                playing_field.append(0) # grid initially set to a matrix of all 0's
    def update(self):
        pass # update grid!

class Snake: # a snake is a list of 1's
    def __init__(self,length): # pos of head of snake?
        snake = []
        for i in range(length):
            snake.append(1)
    def update(self):
        pass # update snake position and direction!

class Pellet:
    def __init__(self,x,y):
        self.x = x # position of pellet on playing field
        self.y = y
    def update(self):
        pass # update pellet! (location when eaten?)

class PyGameWindowView:
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
                
        margin = 5
        rows = 200
        columns = 200
        width = 10
        height = 10
        for row in range(200): # ?? 
            for column in range(200): 
                pygame.draw.rect(self.screen,(255,255,255),[(margin+width)*(columns+margin),(margin+height)*(rows+margin),width,height])
        # fill with food and snake
        pygame.display.update()

class PyGameKeyboardController:
    def __init__(self,model):
        self.model = model
    def handle_keyobard_event(self,event):
        if event.type != KEYDOWN:
            return # have the snake move in its current direction!
        if event.key == pygame.K_LEFT:
            return # change direction of snake 90 degrees to the left
        if event.key == pygame.K_RIGHT:
            return # change direction of snake 90 degrees to the right

if __name__ == '__main__':
    
    prompt = raw_input("S N A K E \n Type 'play' to start a new game: ");
    if prompt.lower() == "play":
        size = (700,700)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("S N A K E")
        
        model = SnakeModel()
        view = PyGameWindowView(model,screen)
        controller = PyGameKeyboardController(model)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False                      
            model.update()
            view.draw()
            time.sleep(0.01)
        pygame.quit()