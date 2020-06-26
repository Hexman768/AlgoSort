# AlgoSort
A engine designed to visualize sorting algorithms with python.

# Dependencies
The sorting engine requires python 3 and pygame in order to work properly.
 * To install pygame simply run ```sudo apt-get install pygame``` or download the source from [here](https://www.pygame.org/download.shtml)

# Usage
To create a new engine, simply create a new class that derives from the [BaseSort](https://github.com/Hexman768/AlgoSort/blob/master/BaseSort.py) class and introduce your own sort function. Deriving from the Base class will give you access to the swap function which enables the visualization of the sort.
To run a visualizer, simply create a new instance of an engine object and create a loop for the pygame instance.

# Example
Here is an example of creating a visualizer with the BubbleSort engine.

```
import pygame, sys
import random
from BubbleSort import BubbleSort

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
    engine1 = BubbleSort(array, clock, screen, WHITE, BLACK)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (engine1.sort()):
                print("DONE")

if __name__ == '__main__':
    main()
```
