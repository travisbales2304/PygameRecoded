import pygame as pg
import sys
from os import path
from settings import *
from SpriteHandler import *
from MapLoader import *
from DevDebug import *



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((ScreenWidth,ScreenHeight))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(10,50)


    def LoadMap(self):
        pass
    