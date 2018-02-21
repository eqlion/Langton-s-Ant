#!/usr/bin/env python3

class Ant():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = self.width // 2
        self.y = self.height // 2
        self.counter = 0

        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3
        # Pointing up at start
        self.position = 0

    def rotate_left(self):
        self.position = (self.position - 1 + 4) % 4

    def rotate_right(self):
        self.position = (self.position + 1) % 4

    def move(self):
        if self.position == self.UP:
            self.y += 1
        elif self.position == self.RIGHT:
            self.x += 1
        elif self.position == self.DOWN:
            self.y -= 1
        else:
            self.x -= 1

        if self.y > self.height - 1:
            self.y = 0
        elif self.y < 0:
            self.y = self.height - 1

        if self.x > self.width - 1:
            self.x = 0
        elif self.x < 0:
            self.x = self.width - 1

        self.counter += 1
