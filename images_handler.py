import pygame
import os


class ImgHandler:
    def __init__(self):
        self.images = []

    def get_all(self):
        return self.images

    def load_all(self, path):
        paths = [os.path.join(path, nome) for nome in os.listdir(path)]
        for i in filter(self._checker, paths):
            self.images.append(pygame.image.load(i))
        return self.images

    def load_single(self, path):
        image = pygame.image.load(path)
        self.images.append(image)
        return image

    def _checker(self, path):
        extensions = [".png", "jpeg", ".jpg", ".gif"]
        if path[-4:] in extensions:
            return True
        return False


if __name__ == "__main__":
    hand = ImgHandler()
    hand.load_all(".\\images")
    print(hand.get_all())
