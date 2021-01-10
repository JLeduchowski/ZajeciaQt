from threading import Timer, Thread, Event
from datetime import datetime

class MyTimer():
    def __init__(self, function):
        self.seconds = 0
        self.function = function
        self.t = 1
        self.thread = Timer(self.t, self.handle_function)
        self.running = True

    def handle_function(self):
        if(self.running):
            self.setTime()
        else:
            self.sleep()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def setTime(self):
        self.function(self.seconds)
        self.seconds += 1

    def sleep(self):
        self.function(self.seconds)

    def stop(self):
        self.thread.cancel()

