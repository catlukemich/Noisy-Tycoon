import game
import tests

# Running the game:

if __name__ == "__main__":
    game = game.Game()
    game.setupSelf()

    # test = tests.SpriteTest(game)
    # test = tests.TerrainTest(game)
    # test = tests.WorldScrollingTest(game)
    test = tests.ViewportsTest(game)
    test.doSetup()

    game.runLoop()