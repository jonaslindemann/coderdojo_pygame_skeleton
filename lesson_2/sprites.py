import pygame as pg
from random import choice, randrange
from settings import *
vec = pg.math.Vector2

from game import *

class Player(GameSprite):
    def __init__(self, game):
        GameSprite.__init__(self, game, [game.all_sprites], layer=PLAYER_LAYER)
        
        # Läs in sprite bild

        self.load_images()
        
        # Justera sprite-rektangel (position och storlek på skärmen)
        
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 100)
        
    def load_images(self):
        
        # Läs in bild från spritesheet
        
        self.image = self.game.spritesheet.get_image(614, 1063, 120, 191)
        
        # Ange transparent bakgrund
        
        self.image.set_colorkey(BLACK)
                   
        