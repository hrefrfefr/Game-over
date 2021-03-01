import pygame
import os
import sys
import time


def load_image(name, color_number=None):
    name = os.path.join('data', name)
    if not os.path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(name)
    if color_number is not None:
        image = image.convert()
        if color_number == -1:
            color_number = image.get_at((0, 0))
        image.set_color_number(color_number)
    else:
        image = image.convert_alpha()
    return image


class Gameover(pygame.sprite.Sprite):
    def __init__(self, group, image):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = -600

    def update(self):
        if self.rect.left < 0:
            self.rect.left += 8


def main():
    size = 600, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game over')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    _ = Gameover(all_sprites, load_image("gameover.png"))
    running = True
    time.sleep(5)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("blue"))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()


if __name__ == '__main__':
    main()