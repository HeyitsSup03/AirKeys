import time

class Debounce:
    def __init__(self, delay=0.5):
        self.last_time = 0
        self.delay = delay

    def ready(self):
        """
        Returns True if enough time has passed since the last ready signal.
        Used to prevent multiple key presses from a single gesture.
        """
        current = time.time()
        if current - self.last_time > self.delay:
            self.last_time = current
            return True
        return False
