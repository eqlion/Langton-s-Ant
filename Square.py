#!/usr/bin/env python3

class Square():
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = state

    def flip(self):
        self.state = 1 if self.state == 0 else 0
