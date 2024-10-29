import pygame
import assets
import updateable

class Sprite(updateable.Updateable):

    def __init__(self, image = None) -> None:
        if isinstance(image, str):
            self.image = assets.loadSpriteImage(image)
        else:
            self.image = image # The image is pygame.Surface
        
        self.location = [0, 0, 0]


    def draw(self,viewport):
        if self.image is None: return

        pos_x, pos_y = viewport.project(self.location)
        w, h = self.image.get_size()
        position = (pos_x - w / 2, pos_y - h / 2)

        surface = viewport.getSurface()
        surface.blit(self.image, position)
        

class SpriteSet(updateable.Updateable):
    
    def __init__(self) -> None:
        self.sprites = []
        
    def addSprite(self, sprite):
        self.sprites.append(sprite)
        
    def removeSprite(self, sprite):
        self.sprites.remove(sprite)
        
    def getSprites(self):
        return self.sprites
    