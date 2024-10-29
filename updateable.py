import abc


class Updateable(abc.ABC):

    # The clock is instance of pygame.time.Clock
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock
    def update(self, clock):
        pass # abstract