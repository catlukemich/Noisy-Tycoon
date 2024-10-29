
class Scene:

    def __init__(self) -> None:
        self.sprites = []

    
    # game.Updateable interface implementation
    def update(self, clock):
        for sprite in self.sprites:
            sprite.update(clock)

    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def getSprites(self) -> list:
        return self.sprites
    