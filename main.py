# pyinstaller -w -i images\icon.ico main.py

from tkinter import S
import pygame

import gaming_screen
import images_handler


def menu(screen, clock, button_png):

    font = pygame.font.SysFont("consolas", 80)
    run = True
    while run:
        clock.tick(30)
        screen.fill((255, 255, 255))

        text = font.render("Hangman", 1, (10, 10, 10))
        screen.blit(text, (400 - text.get_width() / 2, 70))
        screen.blit(button_png, (300, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 300 < x < 500 and 200 < y < 280:
                    run = game.run(screen, clock)

        pygame.display.update()


images = images_handler.ImgHandler()

pygame.init()
win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()

game = gaming_screen.GamingScreen()


menu(win, clock, images.load_single("./images/play.png"))


pygame.quit()
