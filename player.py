import pygame as pg
from support import import_folder
import sys

class Player(pg.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.import_character_asset()
		self.animation_speed=0.15
		self.frame_index=0
#		self.image = pg.Surface((32,64))
#		self.image.fill('red')
		self.image = self.animations['idle'][self.frame_index]
		self.rect  = self.image.get_rect(topleft=pos)
		self.direction=pg.Vector2(0,0)
		self.speed=10
		self.gravity=0.8
		self.jump_speed=-16
		self.status='idle'
		self.facing_right=True
		self.on_ground=False
		self.on_top=False
		self.on_left=False
		self.on_right=False
		self.health=100
		

		
	def import_character_asset(self):
		char_path='/home/aadityakaushik/mine/vs/py/pygame/platformer/resources/'
		self.animations={'idle':[],'walk':[],'jump':[]}
		for animation in self.animations.keys():
			full_path=char_path+animation
			self.animations[animation]=import_folder(full_path)
			
	def animate(self):
		animation=self.animations[self.status]
		self.frame_index+=self.animation_speed
		if self.frame_index>=len(animation):
			self.frame_index=0
		img=animation[int(self.frame_index)]
		if self.facing_right:
			self.image=img
		else:
			flipped_img=pg.transform.flip(img,True,False)
			self.image=flipped_img
		if self.on_ground and self.on_right:
			self.rect=self.image.get_rect(bottomright=self.rect.bottomright)
		elif self.on_ground and self.on_left:
			self.rect=self.image.get_rect(bottomleft=self.rect.bottomleft)
		elif self.on_ground:
			self.rect=self.image.get_rect(midbottom=self.rect.midbottom)
		elif self.on_top and self.on_right:
			self.rect=self.image.get_rect(topright=self.rect.topright)
		elif self.on_top and self.on_left:
			self.rect=self.image.get_rect(topleft=self.rect.topleft)
		elif self.on_top:
			self.rect=self.image.get_rect(midtop=self.rect.midtop)
		
	def get_status(self):
		if self.direction.y == 0 and self.direction.x == 0:
			self.status='idle'
		elif self.direction.x != 0:
			self.status='walk'
		elif self.direction.y<0:
			self.status='jump'
		
	def get_input(self):
		keys=pg.key.get_pressed()
		if keys[pg.K_d]:
			self.direction.x = 1
			self.facing_right=True
		elif keys[pg.K_a]:
			self.direction.x = -1
			self.facing_right=False
		else:
			self.direction.x = 0
		if keys[pg.K_SPACE] and self.on_ground:
			self.jump()
			
			
	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y
	
	def jump(self):
		self.direction.y = self.jump_speed
	
	def update(self):
		if self.health<0:
			print('game over !!')
			pg.quit()
			sys.exit()
			
		self.get_input()
		self.get_status()
		self.animate()
		
