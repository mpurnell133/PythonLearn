#import PyGame Library
import pygame
import numpy
import random

from WindowManager import Window

#game started true
gameON = True

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#Game window imported and opened at chosen size
winWidth = 950
winHeight = 950
gameTitle = "Dungeon Crawler"
gameWindow = Window(winWidth,winHeight, gameTitle)

#tiles/gridpxarray = pygame.PixelArray(surface)
gridLength = 10
gridHeight = 10
tileLength = winWidth / gridLength
tileHeight = winHeight / gridHeight
dataGrid = numpy.zeros((gridLength,gridHeight))




#start at the top left of the Window
startX = 0
startY = 0
#iterate through row, keep index for reference
for indexR, r in enumerate(dataGrid):
        print("row " + str(indexR))

        #iterate through all columns for each row
        for indexC, c in enumerate(dataGrid[indexR]):
            print("column " + str(indexC))

            print(random.randint(1, 10))
            if random.randint(1, 10) >= 6:
                pygame.draw.rect(gameWindow.screen, WHITE, [startX, startY, tileLength, tileHeight])
            else:
                pygame.draw.rect(gameWindow.screen, BLACK, [startX, startY, tileLength, tileHeight])

            if (indexC + 1) == gridLength:
                startY += tileHeight
                startX = 0
            else:
                startX += tileLength

gameWindow.refresh()

#while game is running, look for the event click on the X. Close if clicked.
while gameON:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameON = False
      pygame.quit()
