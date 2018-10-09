import pygame

class Window:
    #constructor
    def __init__(self, width, height, displayName):
        self.screen = pygame.display.set_mode((width, height))
        self.setDisplayName(displayName)
        self.refresh()

    @staticmethod
    def setDisplayName(displayName):
        pygame.display.set_caption(displayName)

    @staticmethod
    def refresh():
        pygame.display.flip()
