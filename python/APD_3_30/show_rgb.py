from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
np.set_printoptions(threshold = sys.maxsize)

def show_rgb(r, g, b):
    R = r * np.ones((255, 255, 1))
    G = g * np.ones((255, 255, 1))
    B = b * np.ones((255, 255, 1))
    
    RGB = np.concatenate([R, G, B], axis = 2)
    
    plt.figure()
    plt.imshow(RGB, vmin = 0, vmax = 255)
    plt.axis('off')

show_rgb(1, 0, 0)
