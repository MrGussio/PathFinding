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
        self.parent = None
    def __repr__(self):
                return repr((self.x, self.y, self.g, self.h, self.total()))
    def total(self):
        return self.g+self.h
    def coords(self):
        return self.y*width+self.x

def getSurroundingNodes(input):
    output = []
    for case in nodes:
        if(case.x == input.x-1 and case.y == input.y):#left
            output = np.append(output, case)
        elif(case.x == input.x+1 and case.y == input.y):#right
            output = np.append(output, case)
        elif(case.x == input.x and case.y == input.y-1):#beneath
            output = np.append(output, case)
        elif(case.x == input.x and case.y == input.y+1):#above
            output = np.append(output, case)
    return output


maze = np.zeros((width, height) , dtype=int)
nodes = np.zeros(0, dtype=Node)
closed = np.zeros(0, dtype=Node)

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
            else:
                nodes = np.append(nodes, Node(x, y, 999999, abs(x-end.x)+abs(y-end.y)))
nodes = sorted(nodes, key=lambda node: node.coords())
total  = 0
while(1):
    sortedArray = sorted(nodes, key=lambda node: node.total())
    for node in sortedArray:
        if node not in closed:
            surrounding = getSurroundingNodes(node)
            for surround in surrounding:
                if(surround.g > node.g+1):
                    surround.g = node.g+1
            surrounding = sorted(surrounding, key=lambda node: node.total())
            surrounding[0].parent = node
            if(node == end): #got to the end
                break
    else:
        break
