import pygame
import math


LETTERS = [chr(97+i) for i in range(26)]
BLACK = (0, 0, 0)
RADIUS = 20


def formula(n): return 70+int(n*(700/13))


def distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Keyboard:
    def __init__(self, font, size) -> None:
        self.letters_pos = []
        self.font = pygame.font.SysFont(font, size)
        self.end = ""

        for i in range(26):
            y = 400 + (i//13) * 50
            self.letters_pos.append([True, LETTERS[i], formula(i % 13), y])

    def update(self, screen):
        for draw, letter, x, y in self.letters_pos:
            if draw:
                text = self.font.render(letter, True, BLACK)
                pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 2)
                screen.blit(text, (x - text.get_width() / 2,
                                   y - text.get_height() / 2))
        if self.end == "game_over":
            text = self.font.render("Game Over", True, (255, 20, 10))
            screen.blit(text, (450, 350))
        if self.end == "winner":
            text = self.font.render("You Win!", True, (20, 255, 10))
            screen.blit(text, (450, 350))

    def check_collosion(self, x, y):
        for letter in self.letters_pos:
            if not letter[0]:
                continue
            elif distance(x, letter[2], y, letter[3]) <= RADIUS:
                letter[0] = False
                return letter[1]
        return None

    def back_button(self, screen):
        text = self.font.render("<", 1, (0, 0, 0))
        pygame.draw.circle(screen, (0, 0, 0), (32, 32), 25, 2)
        screen.blit(text, (32 - text.get_width() / 2,
                           32 - text.get_height() / 2))

    def back_button_collision(self, x, y):
        if distance(x, 32, y, 32) <= 25:
            return True
        return False

    def disable(self):
        for i in self.letters_pos:
            i[0] = False

    def game_over(self):
        self.end = "game_over"

    def winner(self):
        self.end = "winner"


if __name__ == "__main__":
    hand = Keyboard()
    hand.print()
