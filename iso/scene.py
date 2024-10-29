
class Scene:

    def __init__(self) -> None:
        self.sprites = []

    
    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def getSprites(self) -> list:
        return self.sprites