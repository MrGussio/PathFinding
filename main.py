import imageio
import numpy as np
import sys

filename = str(sys.argv[1])
im = imageio.imread(filename)

width = im.shape[0]
height = im.shape[1]

maze = np.zeros((width, height) , dtype=int)

for x in range(width):
    for y in range(height):
        if(im[y][x][0] == 255):
            maze[y][x] = 1

print(maze)
