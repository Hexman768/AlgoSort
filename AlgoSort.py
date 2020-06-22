import pygame, sys
import random

width = 800
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 30

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED   = (255,0,0)

def check_sort(array):
    for i in array:
        if (array[i] > array[i+1]):
            return False
    return True

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    screen.fill(WHITE)
    draw_array(array)

def bubble_sort(array):
    sorted = False
    while not sorted:
        for i in range(len(array)-1):
            if (array[i] > array[i+1]):
                swap(array, i, i+1)
        sorted = check_sort(array)
    return True

def draw_array(array):
    for x in range(len(array)):
        pygame.draw.line(screen, BLACK, (x,0), (x,array[x]))
    pygame.display.flip()
    clock.tick(1000)

def create_array(array):
    for x in range(0, width):
        array.append(random.randint(0, height))

def main():
    pygame.init()
    pygame.display.set_caption('Sorting Algorithm Visualizer')

    array = []
    create_array(array)
    screen.fill(WHITE)
    draw_array(array)
    print("length of array " + str(len(array)))
    print("width " + str(width))

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        if (bubble_sort(array)):
            print(str(array))
            break

if __name__ == '__main__':
    main()
