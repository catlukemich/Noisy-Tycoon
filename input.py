class Input():

    def __init__(self) -> None:
        self.listeners = []


    def addListener(self, listener):
        self.listeners.append(listener)

    def removeListener(self, listener):
        self.listeners.remove(listener)

    def handleEvent(self, event):
        self.broadcastEvent(event)

    def broadcastEvent(self, event):
        for listener in self.listeners:
            listener.handleEvent(event)


class InputListener():

    # The event received by the listener is of type pygame.event
    def handleEvent(self, event):
        pass #abstract