import pygame
from random import choice

from entities import hangman_ent
from entities import keyboard_ent
from entities import display_ent


class GamingScreen:
    def __init__(self):
        self.words = []

    def run(self, win, clock):
        with open("word_bag", "r") as f:
            self.words = f.read().split("\n")

        hangman = hangman_ent.Hangman("./images/hangman")
        keyboard = keyboard_ent.Keyboard("arial", 27)
        display = display_ent.Display(choice(self.words))

        run = True
        while run:
            clock.tick(30)
            win.fill((255, 255, 255))

            hangman.update(win)
            keyboard.update(win)
            keyboard.back_button(win)
            display.update(win)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    key_down = keyboard.check_collosion(x, y)
                    if key_down and not display.good_guess(key_down):
                        if hangman.fails() >= 7:
                            keyboard.disable()
                            display.revel()
                            keyboard.game_over()
                    if display.winner():
                        keyboard.disable()
                        keyboard.winner()
                    if keyboard.back_button_collision(x, y):
                        run = False

            pygame.display.update()
        return True
