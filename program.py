import pygame, sys
import random
from HeapSort import HeapSort

width = 800
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 1000

WHITE = (255,255,255)
BLACK = (0,0,0)

def create_array():
    array = []
    for i in range(0, width):
        array.append(random.randint(0, height))
    return array

def main():
    array = create_array()
    engine1 = HeapSort(array, clock, screen, WHITE, BLACK)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (engine1.sort()):
                print("DONE")

if __name__ == '__main__':
    main()
