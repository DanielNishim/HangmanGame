import images_handler


images = images_handler.ImgHandler()


class Hangman:
    def __init__(self, sprites) -> None:
        self.images = images.load_all(sprites)
        self.status = 0

    def update(self, screen):
        self.status = 6 if self.status >= 7 else self.status
        screen.blit(self.images[self.status], (150, 100))

    def fails(self):
        self.status += 1
        return self.status
