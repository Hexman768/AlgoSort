import pygame, sys
import random
from HeapSort import HeapSort
from BubbleSort import BubbleSort

width = 800
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 10

WHITE = (255,255,255)
BLACK = (0,0,0)

def create_array():
    array = []
    for i in range(0, width):
        array.append(random.randint(0, height))
    return array

def sorted(array):
    for i in range(len(array)-1):
        if (array[i] > array[i+1]):
            return False
    return True

def main():
    array = create_array()
    engine1 = BubbleSort(array, clock, screen, WHITE, BLACK)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (not sorted(array)):
                engine1.sort()
                print(array)

if __name__ == '__main__':
    main()
