import pygame
from pygame.locals import *
import sys # Imports the System Module
import random

class GameSprite(pygame.sprite.Sprite):

  def __init__(self, screen, filename, position):
    pygame.sprite.Sprite.__init__(self) # call the parent (Sprite) constructor
    self.screen = screen
    self.image = pygame.image.load(filename)
    self.position = position
    self.rect = self.image.get_rect() # the image's rectangle

  def update(self, dx, dy):
    x, y = self.position
    x += dx
    y += dy
    self.position = (x, y)
    self.rect = self.image.get_rect()
    self.rect.center = self.position # set new position of sprite

  def draw(self):
    self.screen.blit(self.image, self.rect)

class connectFour():
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza")
        self.black = GameSprite(self.screen, '4row_black.png', (150,400))
        self.red = GameSprite(self.screen, '4row_red.png', (850,400))

    def run(self, running):
        print "starting clock"
        clock = pygame.time.Clock()

        while running == True:
            print "ticking clock"
            clock.tick(30)
            print "filling screen with color"
            self.screen.fill((0, 255, 255))
            print "drawing black"
            self.black.draw()
            print "drawign red"
            self.red.draw()
            print "flipping screeen"
            pygame.display.flip()

play = raw_input("Would you like to play Connect4 by Mikey Jacobs and Ozan Mirza? (y/n): ")
if play == "y":
    game = connectFour(800, 600)
    game.run(True)
elif play == "n":
    sys.exit(0)
