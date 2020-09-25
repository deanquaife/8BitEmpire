import pygame as pg
from settings import *

class Unit(pg.sprite.Sprite):
    def __init__(self, game, x, y, name, atk, hp, armour, res, move, dmg_type):
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
        self.max_HP = hp
        self.curr_HP = hp
        self.armour = armour
        self.res = res
        self.move = move
        self.dmg_type = dmg_type

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def kill(self):
        pg.sprite.Sprite.kill(self)

    """If current health is 0 or less after an action, return True"""
    def is_dead(self):
        return self.curr_HP <= 0

    """Attack an enemy; returns actual damage done after armour/resistance is taken into account"""
    def attack(self, enemy):
        if self.dmg_type == "physical":
            return max(self.atk - enemy.armour, 0)
        elif self.dmg_type == "magic":
            return max(self.atk - enemy.res, 0)

    """def is_adjacent(self, other):"""

    """def show_stats(self):"""