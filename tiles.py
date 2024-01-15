import pygame as pg
from support import import_folder

class Tile(pg.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.import_level_asset()
		self.image=pg.Surface((size,size))
#		self.image.fill('grey')
		self.image = self.level_tile['tile'][0]
		self.rect=self.image.get_rect(topleft=pos)
	
	
	def import_level_asset(self):
		full_path='/home/aaditya/system/vs/py/pygame/platformer/resources/'
		self.level_tile={'tile':[]}
		for t in self.level_tile.keys():
			full_path+=t
			self.level_tile[t]=import_folder(full_path)
			
	
	def update(self,x_shift):
		self.rect.x +=x_shift
		
