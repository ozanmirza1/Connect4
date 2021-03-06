#! /usr/bin/env python2.7

import pygame
from pygame.locals import *
import sys
import random
import time
import os
import sys
import warnings
from GameSprite import GameSprite

if not sys.warnoptions:
    warnings.simplefilter("ignore")

class connectFour():
    def __init__(self, width, height):
        pygame.init()
        self.acticvated = True
        self.backgroundColor = (0, 255, 255)
        self.winner = None # "Red" / "Black" / "Tie"
        self.notPlaying = False
        self.lobster = pygame.font.Font('Lobster-Regular.ttf', 40)
        self.textsurface = self.lobster.render("THIS PROJECT IS BETTER THAN THE OTHERS", False, (255, 69, 0))
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza FPS: 30")
        self.black = GameSprite(self.screen, '4row_black.png', (75,700))
        self.red = GameSprite(self.screen, '4row_red.png', (925,700))
        self.arrows =  [GameSprite(self.screen, "Black_Down_Arrow.png", (245, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (345, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (445, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (545, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (645, 100)),
                        GameSprite(self.screen, "Black_Down_Arrow.png", (745, 100))]
        self.blocks = [[None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None],
                       [None, None, None, None, None, None]]

    def run(self, running):
        clock = pygame.time.Clock()
        up = ["Black Is Up!", "Red Is Up!"]
        blackisup = True
        aboutToPickRow = False
        clicked = False
        placeBlack = []
        placeRed = []
        count = 0
        grid = [[None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
        self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
        for i in range(0, len(self.blocks)):
            for j in range(0, len(self.blocks[i])):
                self.blocks[i][j] = GameSprite(self.screen, '4row_board.png', ((i * 100) + 250, (j * 100) + 200))

        while running == True and self.acticvated == True:
            clock.tick(30)
            pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza in assosication with Ethan Katz FPS: " + str(clock.get_fps()))
            self.screen.fill(self.backgroundColor)
            tie_checker = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                #elif not hasattr(event, 'key'): # if its not a key event then ignore it
                    #continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    pos = pygame.mouse.get_pos()
                    if blackisup == True and self.black.rect.collidepoint(pos) == True:
                        self.textsurface = self.lobster.render("Now Click On The Arrow That You Want The Coin To Fall In!", False, (255, 69, 0))
                        aboutToPickRow = True
                    elif blackisup == False and self.red.rect.collidepoint(pos) == True:
                        self.textsurface = self.lobster.render("Now Click On The Arrow That You Want The Coin To Fall In!", False, (255, 69, 0))
                        aboutToPickRow = True
                    clicked = False
            self.black.update(0, 0)
            self.red.update(0, 0)
            self.black.draw()
            self.red.draw()
            if aboutToPickRow == True:
                for i in range(0, len(self.arrows)):
                    self.arrows[i].update(0, 0)
                    self.arrows[i].draw()
                for i in range(0, len(self.arrows)):
                    if self.arrows[i].rect.collidepoint(pos) == True:
                        if blackisup == True:
                            for j in range(0, len(grid)):
                                if grid[i][5] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][5].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][5] = "BLACK"
                                    break
                                elif grid[i][5] != None and grid[i][4] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][4].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][4] = "BLACK"
                                    break
                                elif grid[i][4] != None and grid[i][3] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][3].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][3] = "BLACK"
                                    break
                                elif grid[i][3] != None and grid[i][2] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][2].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][2] = "BLACK"
                                    break
                                elif grid[i][2] != None and grid[i][1] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][1].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][1] = "BLACK"
                                    break
                                elif grid[i][1] != None and grid[i][0] == None:
                                    placeBlack.append((self.arrows[i].rect.centerx, self.blocks[j][0].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[1], False, (255, 69, 0))
                                    blackisup = False
                                    grid[i][0] = "BLACK"
                                    break
                                break
                            break
                        elif blackisup == False:
                            for j in range(0, len(grid)):
                                if grid[i][5] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][5].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][5] = "RED"
                                    break
                                elif grid[i][5] != None and grid[i][4] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][4].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][4] = "RED"
                                    break
                                elif grid[i][4] != None and grid[i][3] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][3].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][3] = "RED"
                                    break
                                elif grid[i][3] != None and grid[i][2] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][2].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][2] = "RED"
                                    break
                                elif grid[i][2] != None and grid[i][1] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][1].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][1] = "RED"
                                    break
                                elif grid[i][1] != None and grid[i][0] == None:
                                    placeRed.append((self.arrows[i].rect.centerx, self.blocks[j][0].rect.centery))
                                    aboutToPickRow = False
                                    self.textsurface = self.lobster.render(up[0], False, (255, 69, 0))
                                    blackisup = True
                                    grid[i][0] = "RED"
                                    break
                                break
                            break

                    else:
                        continue

            for i in range(0, len(placeBlack)):
                coin = GameSprite(self.screen, "4row_black.png", placeBlack[i])
                coin.rect.centerx = placeBlack[i][0] + 100
                coin.rect.centery = placeBlack[i][1]
                coin.update(5, 0)
                coin.draw()
            for i in range(0, len(placeRed)):
                coin = GameSprite(self.screen, "4row_red.png", placeRed[i])
                coin.rect.centerx = placeRed[i][0] + 100
                coin.rect.centery = placeRed[i][1]
                coin.update(5, 0)
                coin.draw()

            self.screen.blit(self.textsurface, ((self.screen_width / 2) - (self.textsurface.get_rect().width / 2), 20))

            for i in range(0, len(self.blocks)):
                for j in range(0, len(self.blocks[i])):
                    self.blocks[i][j].update(0, 0)
                    self.blocks[i][j].draw()

            pygame.display.flip()

            for i in range(0, len(grid)):
                for j in range(0, len(grid[i])):
                    if grid[i][j] != None:
                        tie_checker += 1
                        if tie_checker == 36:
                            running = False
                            self.playerTie()

            for i in range(0, len(grid)):
                for j in range(0, len(grid[i])):
                    if not i > 2:
                        if grid[i+1][j] == grid[i][j] and grid[i+2][j] == grid[i][j] and grid[i+3][j] == grid[i][j]:
                            if grid[i][j] == "BLACK":
                                running = False
                                self.blackPlayerWon()
                            elif grid[i][j] == "RED":
                                running = False
                                self.redPlayerWon()
                    elif not j > 2:
                        if grid[i][j+1] == grid[i][j] and grid[i][j+2] == grid[i][j] and grid[i][j+3] == grid[i][j]:
                            if grid[i][j] == "BLACK":
                                running = False
                                self.blackPlayerWon()
                            elif grid[i][j] == "RED":
                                running = False
                                self.redPlayerWon()
                    elif not j > 2 and not i > 2:
                        if grid[i+1][j+1] == grid[i][j] and grid[i+2][j+2] == grid[i][j] and grid[i+3][j+3] == grid[i][j]:
                            if grid[i][j] == "BLACK":
                                running = False
                                self.blackPlayerWon()
                            elif grid[i][j] == "RED":
                                running = False
                                self.redPlayerWon()
                    elif not j < 3 and not i > 2:
                        if grid[i+1][j-1] == grid[i][j] and grid[i+2][j-2] == grid[i][j] and grid[i+3][j-3] == grid[i][j]:
                            if grid[i][j] == "BLACK":
                                running = False
                                self.blackPlayerWon()
                            elif grid[i][j] == "RED":
                                running = False
                                self.redPlayerWon()

        while running == False or self.acticvated == False:
            pygame.display.set_caption("Go Back To Terminal!! ->")
            if self.winner == "Red":
                self.screen.fill((255, 0, 0))
            elif self.winner == "Black":
                self.screen.fill((0, 0, 0))
            elif self.winner == "Tie":
                self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif not hasattr(event, 'key'): # if its not a key event then ignore it
                    continue
            trophy = GameSprite(self.screen, 'winner.png', (self.screen_width / 2, self.screen_height / 2))
            trophy.centerx = self.screen_width / 2
            trophy.centery = self.screen_height / 2
            trophy.update(0, 0)
            trophy.draw()
            pygame.display.flip()
            count += 1
            if count == 20:
                time.sleep(10)
                self.retry

    def playerTie(self):
        self.winner = "Tie"
        self.notPlaying = True
        print "_____   ____________    |                              /\                    ==================                                |  "
        print "  |          |        __|                             /  \                            |                                        |  "
        print "  |          |                                       /    \                           |                                        |  "
        print "  |          |                                      /      \                          |         |===|      /==========\        |  "
        print "  |          |              _________              /        \                         |         |===|     /            \       |  "
        print "  |          |             /                      /          \                        |           |      /              \      |  "
        print "  |          |             |                     /            \                       |           |     |================      |  "
        print "  |          |             |                    /==============\                      |           |     |                      |  "
        print "  |          |             \________           /                \                     |           |     |                      |  "
        print "  |          |                      \         /                  \                    |           |     |                      |  "
        print "  |          |                      |        /                    \                   |           |     \                 /    |  "
        print "  |          |                      |       /                      \                  |           |      \               /   |===|"
        print "__|__        |              ________/      /                        \                 |           |       \_____________/    |===|"
        print "\nWait 10 seconds to restart!!"

    def redPlayerWon(self):
        self.winner = "Red"
        self.notPlaying = True
        print "|  /=======\                  |------------          |=\                          ________________                                                "
        print "| /         \                 |                      | =\                        /                \              |            /|    |------------ "
        print "|/           \                |                      |  =\                      /                  \             |           / |    |             "
        print "|             \               |                      |   =\                    /                    \            |          /  |    |             "
        print "|==============               |                      |    =\                  |                      |           |         /   |    |             "
        print "|             \               |                      |     =\                 |                      |           |        /    |    |             "
        print "|              \              |                      |      =\                |                      |           |       /     |    |             "
        print "|               \             |-----------           |      =/                |                      |           |      /      |    |------------ "
        print "|                \            |                      |     =/                 |                      |           |     /       |    |             "
        print "|                 \           |                      |    =/                   \                    /            |    /        |    |             "
        print "|                  \          |                      |   =/                     \                  /             |   /         |    |             "
        print "|                   \         |                      |  =/                       \                /              |  /          |    |             "
        print "|                    \        |                      | =/                         \              /               | /           |    |             "
        print "|                     \       |------------          |=/                           \____________/                |/            |    |-------------"
        print "\nWait 10 seconds to restart!!"

    def blackPlayerWon(self):
        self.winner = "Black"
        self.notPlaying = True
        print "|--------           |                            /\                      |----\        |      /            /|        "
        print "|        \          |                           /  \                     |     \       |     /            / |        "
        print "|         \         |                          /    \                    |      \      |    /            /  |        "
        print "|          \        |                         /      \                   |             |   /                |        "
        print "|           /       |                        /        \                  |             |  /                 |        "
        print "|------------       |                       /----------\                 |             |-/                  |        "
        print "|           \       |                      /            \                |             |-\                  |        "
        print "|          /        |                     /              \               |             |  \                 |        "
        print "|         /         |                    /                \              |             |   \                |        "
        print "|        /          |                   /                  \             |      /      |    \               |        "
        print "|       /           |                  /                    \            |     /       |     \              |        "
        print "|------/            |_____________    /                      \           |----/        |      \     ________|________"
        print "\nWait 10 seconds to restart!!"

    def retry(self):
        playAgain = raw_input("Would You Like To Play Again?(Yepper Pepper/Noper Doper): ")
        if playAgain == "Yepper Pepper":
            self.winner = None
            pygame.display.set_caption("Connect4 Game By Mikey Jacobs And Ozan Mirza FPS: 30")
            self.acticvated = True
            self.run(True)
        else:
            sys.exit(1)

os.system('clear')
time.sleep(0.25); print "|======\                _________            |\            |    |\            |   |-----------------        |-------\   -------|-------       /|        "
time.sleep(0.25); print "|       \              /         \           | \           |    | \           |   |                         |        \         |             / |        "
time.sleep(0.25); print "|        \            /           \          |  \          |    |  \          |   |                         |         \        |            /  |        "
time.sleep(0.25); print "|         \          /             \         |   \         |    |   \         |   |                         |                  |           /   |        "
time.sleep(0.25); print "|                   /               \        |    \        |    |    \        |   |                         |                  |          /    |        "
time.sleep(0.25); print "|                  |                 |       |     \       |    |     \       |   |                         |                  |         /     |        "
time.sleep(0.25); print "|                  |                 |       |      \      |    |      \      |   |---------------          |                  |        /------|--------"
time.sleep(0.25); print "|                  |                 |       |       \     |    |       \     |   |                         |                  |               |        "
time.sleep(0.25); print "|                  |                 |       |        \    |    |        \    |   |                         |                  |               |        "
time.sleep(0.25); print "|                   \                /       |         \   |    |         \   |   |                         |                  |               |        "
time.sleep(0.25); print "|         /          \              /        |          \  |    |          \  |   |                         |         /        |               |        "
time.sleep(0.25); print "|        /            \            /         |           \ |    |           \ |   |                         |        /         |               |        "
time.sleep(0.25); print "|-------/              \__________/          |            \|    |            \|   |------------------       |-------/          |               |        "
play = raw_input("\nWould you like to play Connect4 by Mikey Jacobs and Ozan Mirza in Assosiation With Ethan Katz? (Yepper Pepper/Noper Doper): ")
if play == "Yepper Pepper":
    print "\nRules:"
    time.sleep(1)
    print "* Decide Amougnst Yourselves Who Gets Black And Who Gets Red."
    time.sleep(1)
    print "* Who Ever Is Up, Click On Your Coin, Then Click On THe Arrow That You Want The Column To Be In."
    time.sleep(1)
    print "* The Next Player Goes, And So On"
    time.sleep(1)
    ok = raw_input("OK? (Yepper Pepper/Noper Doper): ")
    if ok == "Yepper Pepper":
        game = connectFour(1000, 800)
        game.run(True)
    else:
        sys.exit(0)
elif play == "Noper Doper":
    sys.exit(0)
else:
    sys.exit(1)
