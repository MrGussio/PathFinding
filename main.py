import imageio
import numpy as np

filename = str(input())
im = imageio.imread(filename)

width = im.shape[0]
height = im.shape[1]
