import random
import time

class MemFrame:
    def __init__(self, num):
        self.num = num
        self.PID = None
        self.used_space = 0
        self.state = "Free"

        self.string = ""

    def toString(self):
        self.string = f"{self.num}: {self.used_space}/5  |  PID: {self.PID}  |  Stat: {self.state}"
        return self.string
    
    def reset_values(self):
        self.PID = None
        self.used_space = 0
        self.state = "Free"

        self.string = self.toString()