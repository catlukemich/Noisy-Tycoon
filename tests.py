import pygame
import assets
import iso
import updateable
import listener
import world.terrain


class Test():

    def __init__(self, game) -> None:
        self.game = game

    def doSetup(self):
        pass # abstract


class SpriteTest(Test):

    def doSetup(self):
        class ExampleSprite(iso.Sprite):
            def update(self, clock):
                self.location[0] += 0.05
                
        sprite = ExampleSprite("assets/tiles/grass-1.png")
        sprite.location = [-1,-1, 0]
        self.game.scene.addSprite(sprite)
    
    
class ScrollingTest(Test):
    
    def __init__(self, game) -> None:
        super().__init__(game)
        self.key_scroller = None
    
    
    def doSetup(self):
        viewport = self.game.viewport
        self.key_scroller = iso.KeyboardScroller(viewport)
        self.game.addUpdateable(self.key_scroller)
    
    
class TerrainTest(SpriteTest):
    
    def doSetup(self):
        super().doSetup()
        import world
        terrain = world.terrain.Terrain(10, 10)
        self.game.scene.addSprite(terrain)
        

class WorldScrollingTest(TerrainTest, ScrollingTest):
    
    def __init__(self, game) -> None:
        super().__init__(game)
        self.mouse_scroller = None
    
    def doSetup(self):
        TerrainTest.doSetup(self)
        ScrollingTest.doSetup(self)
        
        self.mouse_scroller = iso.MouseScroller(self.game.viewport)
        self.mouse_scroller.enable()
        
        
class ViewportsTest(WorldScrollingTest):
    
    def doSetup(self):
        super().doSetup()
        viewport1 = iso.Viewport(self.game, self.game.scene, (100, 100), (200, 200))
        viewport1.setFrame((255, 0, 0), 2)
        self.game.addViewport(viewport1)
        
        viewport2 = iso.Viewport(self.game, self.game.scene, (300, 200), (150, 250))
        viewport2.setFrame((255, 255, 0), 2)
        self.game.addViewport(viewport2)
        
        viewport3 = iso.Viewport(self.game, self.game.scene, (620, 100), (350, 250))
        viewport3.setFrame((255, 255, 200), 2)
        self.game.addViewport(viewport3)
        
        all_viewports = [viewport1, viewport2, viewport3]
        
        active_viewport_idx = 0
        
        key_scroller = self.key_scroller
        mouser_scroller = self.mouse_scroller
        
        class ViewportSelector(updateable.Updateable, listener.Listener):
            def handleEvent(self, event):
                if event.type == pygame.KEYDOWN:
                    nonlocal active_viewport_idx
                    if event.key == pygame.K_RIGHT:
                        active_viewport_idx += 1
                    if event.key == pygame.K_LEFT:
                        active_viewport_idx -= 1
                    
                    active_viewport_idx = active_viewport_idx % len(all_viewports)
                    new_viewport = all_viewports[active_viewport_idx]
                    key_scroller.setViewport(new_viewport)
                    mouser_scroller.setViewport(new_viewport)
                    print(active_viewport_idx, flush=True)
                    
        selector = ViewportSelector()
        
        self.game.addListener(selector)

