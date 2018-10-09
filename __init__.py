#import PyGame Library
import pygame
import numpy
from WindowManager import Window

#game started true
gameON = True

#Game window imported and opened at chosen size
winWidth = 800
winHeight = 800
gameTitle = "Dungeon Crawler"
gameWindow = Window(winWidth,winHeight, gameTitle)

#while game is running, look for the event click on the X. Close if clicked.
while gameON:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameON = False
      pygame.quit()

#tiles/grid
gridWidth = 10
gridHeight = 10
tileWidth = winWidth / gridWidth
tileHeight = winHeight / gridHeight
dataGrid = numpy.zeros((gridWidth,gridHeight))
