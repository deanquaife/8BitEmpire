import pygame as pg
from settings import *

class Unit(pg.sprite.Sprite):
    def __init__(self, game, x, y, name, atk, hp, armour, res, move, role):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.name = name
        self.atk = atk
        self.hp = hp
        self.armour = armour
        self.res = res
        self.move = move
        self.role = role

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE