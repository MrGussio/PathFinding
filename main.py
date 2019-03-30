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
    def __repr__(self):
                return repr((self.x, self.y, self.g, self.h, self.total()))

    def total(self):
        return self.g+self.h

maze = np.zeros((width, height) , dtype=int)
nodes = np.zeros(0, dtype=Node)

def sortArray(input):
    output = np.zeros(len(input), dtype=Node)
    print(output)
    print(len(input))


#initialize maze
for y in range(height):
    y = height-1-y
    for x in range(width):
        if(im[y][x][0] == 255):
            maze[y][x] = 1
            if(y == 0): # starting node
                start = Node(x, y, 0, abs(x-end.x)+abs(y-end.y))
                nodes = np.append(nodes, start)
                print("start!")
            elif(y == height-1): #ending node
                end = Node(x, y, 999999, 0)
                nodes = np.append(nodes, end)
            else:
                nodes = np.append(nodes, Node(x, y, 999999, abs(x-end.x)+abs(y-end.y)))

while(1):
    array = sortArray(nodes)
    nodes = sorted(nodes, key=lambda node: node.total())
    print(nodes)
    break
