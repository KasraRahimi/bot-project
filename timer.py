import time as t

class Timer:
    
    def __init__(self, duration):
        self.start = t.time()
        self.duration = duration
        self.end = t.time() + duration

    def timeRemaining(self, isInMinutes=False):
        timeLeft = self.end - t.time()
        if isInMinutes:
            return timeLeft / 60
        return timeLeft