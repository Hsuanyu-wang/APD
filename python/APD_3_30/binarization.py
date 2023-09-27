from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
import math

img = Image.open('img1.jpg').convert('L')
img = np.array(img)



plt.figure()
plt.axis('off')
img = img.clip(0, 255).astype(int)
plt.imshow(img, plt.cm.gray, vmin = 0, vmax = 255)

plt.figure()
plt.hist(img.flatten(), bins = 80, density = False, facecolor='b')
# # plt.hist(img, bins = 20, density = False, facecolor='b')

[h, w] = img.shape
img_bin = np.zeros((h, w))
img_erro = np.zeros((h, w))

threshold = 135
# binarization
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        img_bin[y][x] = (img[y][x] > threshold)
        
plt.figure()
plt.axis('off')
img_bin = img_bin.clip(0, 1).astype(int)
plt.imshow(img_bin, plt.cm.gray, vmin = 0, vmax = 1)

