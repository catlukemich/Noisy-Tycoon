import pygame
import updateable
import listener
from .constants import Constants


class Scroller(updateable.Updateable, listener.Listener):
    
    def __init__(self, viewport) -> None:
        self.viewport = viewport
    
    # Set the viewport this scroller should scroll:
    def setViewport(self, viewport):
        self.viewport = viewport
    
    def enable(self):
        game = self.viewport.getGame()
        game.addUpdateable(self)
        game.addListener(self)
        
    def disable(self):
        game = self.viewport.getGame()
        game.removeUpdateable(self)
        game.removeListener(self)


class KeyboardScroller(Scroller):
    
    def __init__(self, viewport) -> None:
        super().__init__(viewport)
    
    def update(self, clock):
        left = pygame.key.get_pressed()[pygame.K_LEFT]
        right = pygame.key.get_pressed()[pygame.K_RIGHT]
        up = pygame.key.get_pressed()[pygame.K_UP]
        down = pygame.key.get_pressed()[pygame.K_DOWN]
        
        center = self.viewport.getCenter()
        if left: 
            center[0] -= 0.1
            center[1] += 0.1
        if right:
            center[0] += 0.1
            center[1] -= 0.1
        if up:
            center[0] -= 0.1
            center[1] -= 0.1
        if down:
            center[0] += 0.1
            center[1] += 0.1
            
    def enable(self):
        game = self.viewport.getGame()
        game.addUpdateable(self)
        
        
    def disable(self):
        game = self.viewport.getGame()
        game.addUpdateable(self)
        

class MouseScroller(Scroller):
    
    def __init__(self, viewport) -> None:
        super().__init__(viewport)
        self.scrolling = False
        
    
    def handleEvent(self, event):
        if event.type == pygame.MOUSEMOTION and event.buttons[2]:
            prev_mouse_pos = event.pos
            # pygame.mouse.set_visible(False)
            self.scrolling = True
            center = self.viewport.getCenter()
            rel_x, rel_y = event.rel
            
            reverse = -1
            
            center[0] += rel_x / Constants.TILE_WIDTH  * reverse
            center[1] -= rel_x / Constants.TILE_WIDTH  * reverse
            center[0] += rel_y / Constants.TILE_HEIGHT * reverse
            center[1] += rel_y / Constants.TILE_HEIGHT * reverse
        
            pygame.mouse.set_pos(prev_mouse_pos)
        
        # pygame.mouse.set_visible(True)
        # if event.button == 3:
        #     if event.type == pygame.MOUSEBUTTONDOWN: self.scrolling = True   
        #     elif event.type == pygame.MOUSEBUTTONUP: self.scrolling = False
            
        # if self.scrolling:
                
        