import imageio
import numpy as np
import sys

filename = str(sys.argv[1])
im = imageio.imread(filename)

width = im.shape[0]
height = im.shape[1]

maze = np.array([])

print(maze)
