#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
import random

from settings import *
from sprites import *
from game import *

class JumpyGame(Game):
    def __init__(self, title, width, height, fps):
        Game.__init__(self, title, width, height, fps)
        
        ## -- Initiera spel variabler
        
        # Variabel som anger att spelet är igång.

        self.running = True
        
        # Funktion som läser in spelets filer

        self.load_data()

    def load_data(self):
        
        ## -- Läs in speldata
        
        # Läs in bilder för sprites

        self.spritesheet = SpriteSheet(self.image_path(SPRITESHEET))

    def new(self):
        
        ## -- Starta nytt spel
        
        # Skapa sprite för spelare

        self.player = Player(self)
        
        # Starta spel loop
        
        self.run()
        
    def run(self):
        
        ## -- Spel loop
        
        # Variabel som anger om ett spel är igång, dvs
        # inte i startskärm eller game over
        
        self.playing = True
        
        # Spel loopen
        
        while self.playing:
            # Se till att spelet uppdateras 60 bilder i
            # sekunden FPS=60
            
            self.clock.tick(FPS)
            
            # Kontrollera om tangenter eller joysticks tryckts ned.
            
            self.events()
            
            # Uppdatera sprites
            
            self.update()
            
            # Rita upp fönster och sprites
            
            self.draw()

    def update(self):

        ## -- Uppdatera sprites

        self.update_sprites()

    def events(self):
        
        ## -- Hantera händelser i spelet (tangentbord / joysticks)
        
        for event in self.get_event():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
       
    def draw(self):

        ## -- Rita upp skärmen
        
        # Rensa skärm
        
        self.screen.fill(BGCOLOR)
        
        # Rita upp alla sprites
        
        self.draw_sprites()
        
        # Växla till synlig rityta
        
        self.flip_display()
        
    def show_start_screen(self):
    
        ## -- Visa startskärm
        
        pass
    
    def show_go_screen(self):
        
        # -- Visa Game Over skärm
        
        pass
          
# Skapa vårt spel
          
g = JumpyGame(TITLE, WIDTH, HEIGHT, FPS)

# Visa startskärm

g.show_start_screen()

# Loopa tills dess spelet avslutas.

while g.running:
    g.new()
    g.show_go_screen()
    
g.quit()
