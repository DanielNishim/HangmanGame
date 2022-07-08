import pygame


class Display:
    def __init__(self, word, font="consolas", size=30) -> None:
        self.word = word.lower()
        self.font = pygame.font.SysFont(font, size)
        self.guessed = []
        self.successes = 0

    def update(self, screen):
        word = self.show()
        text = self.font.render(word, True, (0, 0, 0))
        screen.blit(text, (400, 200))

    def good_guess(self, guess):
        self.guessed.append(guess)
        if not guess in self.word:
            return False
        self.successes += 1
        return True

    def show(self):
        return "".join([f"{letter} " if letter in self.guessed else "_ " for letter in self.word])

    def revel(self):
        for i in self.word:
            self.guessed.append(i)

    def winner(self):
        if self.successes >= len(set(self.word)):
            return True
        return False
