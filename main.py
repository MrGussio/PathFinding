import imageio
import numpy as np
import sys

filename = str(sys.argv[1])
im = imageio.imread(filename)

width = im.shape[0]
height = im.shape[1]
#node object
class Node:

    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h

maze = np.zeros((width, height) , dtype=int)
open = []
nodes = np.zeros((width, height), dtype=Node)

#initialize maze
for y in range(height):
    y = height-1-y
    for x in range(width):
        if(im[y][x][0] == 255):
            maze[y][x] = 1
            if(y == 0): # starting node
                start = Node(x, y, 0, abs(x-end.x)+abs(y-end.y))
                nodes[y][x] = start
                print("start!")
            elif(y == height-1): #ending node
                end = Node(x, y, 999999, 0)
                nodes[y][x] = end
            else:
                nodes[y][x] = np.append(open, (Node(x, y, 999999, abs(x-end.x)+abs(y-end.y))))

print(start.h)
