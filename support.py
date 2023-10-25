from os import walk
import pygame as pg

def import_folder(path):
	surface_list=[]
	for _,__,img_files in walk(path):
		for img in img_files:
			full_path=path+'/'+img
			img_surf=pg.image.load(full_path).convert_alpha()
			img_surf = pg.transform.scale(img_surf, (60,60))
			surface_list.append(img_surf)
	return surface_list


