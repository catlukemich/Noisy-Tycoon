import pygame


class Sprite:

    def __init__(self, image = None) -> None:
        if isinstance(image, str):
            self.image = pygame.image.load(image)
        else:
            self.image = image # The image is pygame.Surface
            


    def draw(self,viewport):
        if self.image is None: return

        surface = viewport.getSurface()
        surface.blit(self.image, (0,0))