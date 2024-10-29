import pygame

# Class for the isometric viewport
class Viewport:

    # Create a viewport for a certain scene, many viewports can display parts of the same scene
    def __init__(self, game, scene) -> None:
        self.game = game
        self.scene = scene
        self.sprites = []

        # Temporary, should align to the passed in size:
        w, h = game.getScreen().get_size()
        self.surface = pygame.surface.Surface((w, h)) # The viewport will be drawn to a new surface it owns.

    
    def draw(self) -> pygame.surface.Surface:
        # Clear the surface by filling it
        self.surface.fill((0,0,0))

        sprites = self.scene.getSprites()
        for sprite in sprites:
            sprite.draw(self)

    def getSurface(self)  -> pygame.surface.Surface:
        return self.surface

    