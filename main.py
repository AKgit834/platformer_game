import pygame as pg
import sys
from settings import *
from level import Level


pg.init()
clock=pg.time.Clock()
screen=pg.display.set_mode((WIDTH,HEIGHT))
level=Level(level_map,screen)
background=pg.image.load('/home/aadityakaushik/Downloads/bg.jpg')
background=pg.transform.scale(background,(800,600))
while True:
    for e in pg.event.get():
        if e.type==pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
    screen.blit(background,(0,0))
#    screen.fill('black')
    level.run()
    clock.tick(60)
    pg.display.update()  	
    
