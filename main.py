import game
import tests

# Running the game:

if __name__ == "__main__":
    game = game.Game()
    game.setupSelf()

    test = tests.SpriteTest(game)
    test.doSetup()

    game.runLoop()