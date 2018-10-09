import pygame

class Window:
    #constructor
    def __init__(self, width, height, displayName):
        if width is None or height is None:
            print("No width or height set for the main window, exiting")
            pygame.quit()
        else:
            screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption(displayName)
            pygame.display.flip()
