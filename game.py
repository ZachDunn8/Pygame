import pygame
import time
from math import fabs, hypot
from random import randint
pygame.init()
screen_size = (512, 480)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('link_model.png')
goblin_image = pygame.image.load('triforce.png')
pygame.mixer.music.load('zelda_06.wav')
pygame.mixer.music.play(-1)



hero = {
	"x":100,
	"y":100,
	"speed":3,
	"wins": 0
}



goblin = {
	"x": 200,
	'y': 200,
	"speed": 10
 
}

monster = {
	'x': 100,
	'y': 100,
	'speed': 3,
	'dx': 1,
	'dy': 1
}



keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276,
}

keys_down = {
	"up": False,
	"down": False,
	"right": False,
	"left": False

}
game_on = True
while game_on:
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			if event.key == keys['up']:
				keys_down['up'] = True
				print "Pressed up"
				#hero['y'] -= hero['speed']
			elif event.key == keys ['down']:
			#hero['y'] += hero ['speed']
				keys_down['down'] = True
			elif event.key == keys ['left']:
			#hero['x'] =+ hero ['speed']
				keys_down['left'] = True
				print "I pressed left"
			elif event.key == keys ['right']:
			#hero['x'] += hero ['speed']
				keys_down['right'] = True
		elif event.type == pygame.KEYUP:
			if event.key == keys['up']:
				keys_down['up'] = False
				#hero['y'] -= hero['speed']
			elif event.key == keys ['down']:
			#hero['y'] += hero ['speed']
				keys_down['down'] = False
			elif event.key == keys ['left']:
			#hero['x'] =+ hero ['speed']
				keys_down['left'] = False
			elif event.key == keys ['right']:
			#hero['x'] += hero ['speed']
				keys_down['right'] = False

		

	if goblin['x'] in range(0, 460):
		if goblin['y'] in range(0, 490):			


			if hero['x'] in range (0, 460):
				if hero['y'] in range (0, 490):	
					



					if keys_down['up']:
						hero['y'] -= hero['speed']
					elif keys_down['down']:
						hero['y'] += hero['speed']
					if keys_down['left']:
						hero['x'] -= hero['speed']
					elif keys_down['right']:
						hero['x'] += hero['speed']

	



	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if distance_between < 10:
		print "You got me!"
		hero['wins'] += 1
		pygame.mixer.music.load("zelda_win.wav")	
		pygame.mixer.music.play()

			
	#else:
	#	print "not touching"
	




	pygame_screen.blit(background_image, [0,0])

	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])


	pygame_screen.blit(hero_image, [hero['x'],hero['y']])
	pygame_screen.blit(goblin_image, [goblin['x'], goblin['y']])
	

	

	pygame.display.flip()