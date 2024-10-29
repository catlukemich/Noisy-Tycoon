import pygame

from .constants import Constants

# Class for the isometric viewport
class Viewport:

    # Create a viewport for a certain scene, many viewports can display parts of the same scene
    def __init__(self, game, scene, position, dimensions) -> None:
        self.game = game
        self.scene = scene
        self.sprites = []
        
        self.center = [0, 0, 0]

        # The viewport will be drawn to a new surface it owns, with the initial dimensions passed to the constructor:
        self.position = position
        self.dimensions = dimensions
        self.surface = pygame.surface.Surface(dimensions) 
        
        self.drawFrame = True
        self.frameColor = (0, 0, 255)
        self.frameWidth = 1

    
    def draw(self) -> pygame.surface.Surface:
        # Clear the surface by filling it
        self.surface.fill((0,0,0))

        sprites = self.scene.getSprites()
        self.sprites = self.cull(sprites)
        
        for sprite in self.sprites:
            sprite.draw(self)
            
        if self.drawFrame:
            w, h = self.surface.get_size()
            pygame.draw.line(self.surface, self.frameColor, (0,0), (w,0), self.frameWidth)
            pygame.draw.line(self.surface, self.frameColor, (0,0), (0,h - 1), self.frameWidth)
            pygame.draw.line(self.surface, self.frameColor, (0,h - 1), (w - 1,h - 1), self.frameWidth)
            pygame.draw.line(self.surface, self.frameColor, (w - 1,0), (w - 1,h - 1), self.frameWidth)

    def cull(self, sprites):
        w, h = self.surface.get_size()
        culled = []
        for sprite in sprites:
            from .sprite import SpriteSet
            if isinstance(sprite, SpriteSet):
                subsprites = sprite.getSprites()
                culled.extend(self.cull(subsprites))
                continue
            pos_x, pos_y = self.project(sprite.location)
            if (pos_x >= 0 and pos_x <= w and pos_y >= 0 and pos_y <= h):
                culled.append(sprite)

        return culled

    def project(self, location):
        loc_x, loc_y, loc_z = location
        center_x, center_y, center_z = self.center
        pos_x = (loc_x - center_x) * (Constants.TILE_WIDTH / 2) - (loc_y - center_y) * (Constants.TILE_WIDTH / 2)
        pos_y = (loc_x - center_x) * (Constants.TILE_HEIGHT / 2) + (loc_y - center_y) * (Constants.TILE_HEIGHT / 2) - (loc_z - center_z) * (Constants.TILE_HEIGHT / 2) # TODO Figure out loc_z impact.
        pos_x = round(pos_x)
        pos_y = round(pos_y)
        return [pos_x, pos_y]


    def getGame(self):
        return self.game

    def getCenter(self):
        return self.center

    def getSurface(self)  -> pygame.surface.Surface:
        return self.surface

    def getPosition(self):
        return self.position
    
    def setFrame(self, color, width = 1):
        if color == None:
            self.drawFrame = False
        else:
            self.drawFrame = True
            self.frameColor = color
            self.frameWidth = width
            

class MainViewport(Viewport):
    
    def __init__(self, game, scene) -> None:
        position = [0, 0]
        dimensions = game.getScreen().get_size()
        super().__init__(game, scene, position, dimensions)