from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
np.set_printoptions(threshold = sys.maxsize)
# =============================================================================
# flatten()
# =============================================================================
# img = Image.open('Lenna.jpg')
# img = np.array(img)

# N = 3
# edge = int((N-1)/2)

# temp = img[3-edge:1+edge+1, 3-edge:3+edge+1, 1]
# print(temp)
# temp = temp.flatten()
# print(temp)
# =============================================================================
# matrix : view type
# =============================================================================
# u = np.ones((5,5,1))
# v = np.zeros((5,5,1))

# print("u")
# print(u)
# print("v")
# print(v)

# w = np.concatenate((u, v), axis = 0)
# f = np.concatenate((u, v), axis = 1)
# g = np.concatenate((u, v), axis = 2)
# print("w")
# print(w)
# print("f")
# print(f)
# print("g")
# print(g)
# =============================================================================
# array : 0 start
# =============================================================================
# for x in range(0, 10, 1):
#     print(x)