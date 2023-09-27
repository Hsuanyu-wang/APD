from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
import numpy as np 
import math

image = Image.open('cockroach.jpg')
img = np.array(image)

plt.figure()
plt.axis('off')
plt.imshow(img, vmin = 0,  vmax = 255)

img = img.astype(float)
[h, w, d] = img.shape
img_2 = np.zeros((h, w, d))

color_1 = [37, 77, 175]
color_2 = [159, 28, 70]
color_range_1 = [50, 50, 50]
color_range_2 = [50, 50, 50]

for y in range(h):
    for x in range(w):
        if ((np.abs(color_1[0] - img[y, x, 0]) < color_range_1[0]) and \
            (np.abs(color_1[1] - img[y, x, 1]) < color_range_1[1]) and \
            (np.abs(color_1[2] - img[y, x, 2]) < color_range_1[2])):
            
            img[y, x, :] = [0, 0, 255]
            
        if ((np.abs(color_2[0] - img[y, x, 0]) < color_range_2[0]) and \
            (np.abs(color_2[1] - img[y, x, 1]) < color_range_2[1]) and \
            (np.abs(color_2[2] - img[y, x, 2]) < color_range_2[2])):
            
            img[y, x, :] = [255, 0, 0]
            
plt.figure()
plt.axis('off')
img = img.astype(np.uint8)
plt.imshow(img, vmin = 0, vmax = 255)
plt.show()