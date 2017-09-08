#include pygame
import pygame

#init game
#in order to use pygame, we have to run the init method
pygame.init()

#create screen with a particular size
#screen size must be a tuple
screen_size = (512, 480)
#Actually tell pygame to set screen up and store it
pygame_screen = pygame = pygame.display.set_mode(screen_size)
#set up a pointless caption
pygame.display.set_caption("Goblin Chase")
#set up a var with our image
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')

#set up hero location
hero = {
		'x':100,
		'y':100,
		'speed':20

}
#create a game loop (while)
# create boolean for whether the game should be going or not
game_on = True
while game_on:

	#we are inside the main game loop.
	#it will keep running as long as bool is true
	#add a quit event (python needs an escape)
# pygame comes with an event loop! (sort of like JS)

for event in pygame.event.get():
	if (event.type == pygame.QUIT):
		#the user clicked the red x in the top left
		game_on = False

#fill in screen with a color (or image)
# ACTUALLY RENDER SOMETHING
#blit takes 2 arguments
#1. What do you want to draw?
#2. Where do you want to draw it?

pygame_screen.blit(background_image, [0,0])

#repeat 6 over and over.....

pygame.display.flip()