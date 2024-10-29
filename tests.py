import iso

class Test():

    def __init__(self, game) -> None:
        self.game = game
        self.doSetup()


    def doSetup(self):
        pass # abstract


class SpriteTest(Test):

    def doSetup(self):
        sprite = iso.Sprite("assets/test.png")
        self.game.scene.addSprite(sprite)