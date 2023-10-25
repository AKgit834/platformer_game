import pygame as pg
from tiles import Tile
from settings import tile_size
from player import Player
from enemy import Spikes
from settings import WIDTH


class Level:
	def __init__(self,level_data,surface):
		self.display_surface=surface
		self.setup_level(level_data)
		self.world_shift=0
		self.current_x=0
	
	def setup_level(self,layout):
		self.tiles=pg.sprite.Group()
		self.player=pg.sprite.GroupSingle()
		self.spike=pg.sprite.Group()
		
		for idr,row in enumerate(layout):
			for idc,col in enumerate(row):
				x=idc*tile_size
				y=idr*tile_size
				if col == 'X':
					tile=Tile((x,y),tile_size)
					self.tiles.add(tile)
				if col == 'P':
					player=Player((x,y))
					self.player.add(player)
				if col == 'S':
					spike=Spikes((x,y))
					self.spike.add(spike)
	
					
	def scroll_x(self):
		player=self.player.sprite
		player_x=player.rect.centerx
		direction_x=player.direction.x
		if player_x<WIDTH/4 and direction_x<0:
			self.world_shift=10
			player.speed=0
		elif player_x>WIDTH-(WIDTH/4) and direction_x>0:
			self.world_shift=-10
			player.speed=0
		else:
			self.world_shift=0
			player.speed=10
	def horizontal_collision(self):
		player = self.player.sprite
		player.rect.x +=player.direction.x*player.speed
		
		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x<0:
					player.rect.left = sprite.rect.right
					player.on_left=True
					self.current_x=player.rect.left
				elif player.direction.x>0:
					player.rect.right=sprite.rect.left
					player.on_right=True
					self.current_x=player.rect.right
		for sprite in self.spike.sprites():
			if sprite.rect.colliderect(player.rect):
				player.health -= 1
				print(player.health)
				
		if player.on_left and (player.rect.left< self.current_x or player.direction.x>=0):
			player.on_left=False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x<=0):
			player.on_right=False
		
		
		
	def vertical_collision(self):
		player = self.player.sprite
		player.apply_gravity()
		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y<0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_top=True
				elif player.direction.y>0:
					player.rect.bottom=sprite.rect.top
					player.direction.y = 0
					player.on_ground=True
		if player.on_ground and player.direction.y<0 or player.direction.y>1:
			player.on_ground=False
		if player.on_top and player.direction.y>0:
			player.on_top=False
	
	def run(self):
		self.tiles.update(self.world_shift)
		self.spike.update(self.world_shift)
		self.tiles.draw(self.display_surface)
		self.scroll_x()
		self.player.update()
		self.horizontal_collision()
		self.vertical_collision()
		self.player.draw(self.display_surface)
		self.spike.draw(self.display_surface)


		
		
