from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
import math
import random

np.set_printoptions(threshold = sys.maxsize)

img = Image.open('Lenna.jpg')
img = np.array(img)

plt.figure()
plt.imshow(img, vmin = 0, vmax = 255)
plt.axis('off')
Image.fromarray(img).save('img.jpg')

[h, w, d] = img.shape

def imnoise(img, prob):
    img1 = np.copy(img)
    for y in range(h):
        for x in range(w):
            for z in range(d):
                if np.random.rand() < prob:
                    img1[y, x, z] = 0
                elif np.random.rand() > prob:
                    img1[y, x, z] = 255
                else:
                    img1[y, x, z] = img[y, x, z]
    return img1

img = imnoise(img, 0.08)

plt.figure()
plt.imshow(img, vmin = 0, vmax = 255)
plt.axis('off')
Image.fromarray(img).save('img_noise.jpg')