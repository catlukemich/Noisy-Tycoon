import pygame

import input
import iso


# The base game class, instantiated for the game to run.
class Game:

    def __init__(self) -> None:
        self.loop = True
        self.screen = None
        self.clock = None # The clock used to work with time, ticks and delays
        self.input = None # Input system for delegating events in event loop
        self.scene = None # The main scene
        self.viewport = None # The main viewport

    def setupSelf(self):
        self.initLibraries()
        self.displayWindow()
        self.initApplication()

    def initLibraries(self):
        pygame.init()

    def displayWindow(self):
        self.screen = pygame.display.set_mode((1024, 768))

    def initApplication(self):
        self.clock = pygame.time.Clock() 
        self.input = input.Input()
        self.scene = iso.Scene() 
        self.viewport = iso.Viewport(self, self.scene)

    def runLoop(self):
        while self.loop:
            for event in pygame.event.get():
                self.handleEvent(event)
                
            print("im loopainga!!")
            # self.draw()


            pygame.display.update()

            self.clock.tick(40) # Arg is fps

    def handleEvent(self, event):
        # Default quit conditions:
        if event.type == pygame.QUIT: self.loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: self.loop = False

        # Delegate events to the input system:
        self.input.handleEvent(event)

    def draw(self):
        self.viewport.draw()
        surface = self.viewport.getSurface()
        self.screen.blit(surface, (0,0))


    def terminate(self):
        self.loop = False


    def getScreen(self):
        return self.screen
    
