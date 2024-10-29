import abc

# Base abstract class for objects that want to listen for the events in the game loop
class Listener(abc.ABC):

    # The event received by the listener is of type pygame.event
    def handleEvent(self, event):
        pass #abstract