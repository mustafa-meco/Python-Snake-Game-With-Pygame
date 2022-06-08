import pygame, sys
from snake_game import SnakeGame
from snake_game_noBorders import SnakeGameNB
import settings as s

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((s.SCREEN_WIDTH, s.SCREEN_HIGHT), 0, 32)
font = pygame.font.Font(None, 25)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

global click
click = False

def main_menu():
    while True:
        screen.fill((0,0,0))
        draw_text("main menu", font, s.BLACK, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text("Play Snake With Borders", font, s.BLUE1, screen, 55, 120)
        draw_text("Play Snake Without Borders", font, s.BLUE2, screen, 55, 220)
        button_1 = pygame.Rect(50, 100, 250, 50)
        button_2 = pygame.Rect(50, 200, 250, 50)



        if button_1.collidepoint((mx, my)):
            if click:
                game(0)
        if button_2.collidepoint((mx, my)):
            if click:
                game(1)
        pygame.draw.rect(screen, s.RED, button_1, 2)
        pygame.draw.rect(screen, s.RED, button_2, 2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game(op):
    if op == 0:
        Game = SnakeGame(screen, mainClock)
    elif op == 1:
        Game = SnakeGameNB(screen, mainClock)
    running = True
    while running:
        screen.fill((0, 0, 0))
        game_over, score = Game.play_step()
        if game_over == True:
            break


        pygame.display.update()

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text("options", font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    main_menu()






