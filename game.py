import pygame

import input
import iso


# The base game class, instantiated for the game to run.
class Game:

    def __init__(self) -> None:
        self.loop = True
        self.screen = None
        self.clock = None # The clock used to work with time, ticks and delays
        self.scene = None # The main scene
        self.viewport = None # The main viewport
        self.viewports = [] # Other viewports
        self.updateables = [] # The objects that will update with the game itself.
        self.listeners = [] # Event listeners that want to know events from the game's event loop.

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
        self.addUpdateable(self.scene)
        self.viewport = iso.MainViewport(self, self.scene)

    def runLoop(self):
        while self.loop:
            for event in pygame.event.get():
                self.handleEvent(event)
                
            self.update(self.clock)
            self.draw()

            pygame.display.update()

            self.clock.tick(40) # Arg is fps

    def handleEvent(self, event):
        # Default quit conditions:
        if event.type == pygame.QUIT: self.loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: self.loop = False

        # Delegate events to the input system:
        for listener in self.listeners:
            listener.handleEvent(event)

    def update(self, clock):
        for updateable in self.updateables:
            updateable.update(clock)

    def draw(self):
        self.viewport.draw()
        surface = self.viewport.getSurface()
        self.screen.blit(surface, (0,0))
        
        for viewport in self.viewports:
            pos = viewport.getPosition()
            surf = viewport.getSurface()
            dims = surf.get_size()
            self.screen.set_clip((*pos, *dims))
            viewport.draw()
            self.screen.blit(surf, pos)
            self.screen.set_clip(None)

    def terminate(self):
        self.loop = False

    def getScreen(self):
        return self.screen
    
    def addViewport(self, viewport):
        self.viewports.append(viewport)
    
    def removeViewport(self, viewport):
        self.viewport.remove(viewport)
    
    def addUpdateable(self, updateable):
        self.updateables.append(updateable)

    def removeUpdateable(self, updateable):
        self.updateables.remove(updateable)
    
    def addListener(self, listener):
        self.listeners.append(listener)

    def removeListener(self, listener):
        self.listeners.remove(listener)

  
