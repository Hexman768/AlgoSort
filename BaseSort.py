import pygame, sys
import random

class BaseSort:
    def __init__(self, array, clock, screen, line_color, back_color):
        self.array = array
        self.clock = clock
        self.screen = screen
        self.line_color = line_color
        self.back_color = back_color
        self.default_operation()

    def default_operation(self):
        pygame.init()
        pygame.display.set_caption('Sorting Algorithm Visualizer')
        self.screen.fill(self.back_color)
        self.draw_array()

    def check_sort(self, forward):
        print("Checking")
        if (forward):
            for i in self.array:
                if (self.array[i] > self.array[i+1]):
                    return False
        else:
            for i in self.array:
                if (self.array[i] < self.array[i+1]):
                    return False
        print("Sorted")
        return True

    def swap(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp
        self.screen.fill(self.back_color)
        self.draw_array()

    def draw_array(self):
        for x in range(len(self.array)):
            pygame.draw.line(self.screen, self.line_color, (x,0), (x,self.array[x]))
        pygame.display.flip()
        self.clock.tick(1000)

