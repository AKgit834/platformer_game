import pygame as pg
from support import import_folder

class Spikes(pg.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
#		self.image = pg.Surface((64,64))
#		self.image.fill('red')
		self.import_enemy_asset()
		self.image=self.enemy_tile['spike'][0]
		self.rect  = self.image.get_rect(topleft=pos)

	def import_enemy_asset(self):
		full_path='/home/aaditya/system/vs/py/pygame/platformer/resources/enemy/'
		self.enemy_tile={'spike':[]}
		for t in self.enemy_tile.keys():
			full_path+=t
			self.enemy_tile[t]=import_folder(full_path)

	def update(self,shift):
		self.rect.x += shift
