from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 

import math

np.set_printoptions(threshold = sys.maxsize)
# img = Image.open('Lenna.bmp')
img = Image.open('Lenna.jpg')
img = np.array(img)

plt.figure()
plt.imshow(img, vmin = 0, vmax = 255)
plt.axis('off')
# Image.fromarray(img).save('img.jpg')

[h, w, d] = img.shape

scale_x = 3
scale_y = 4

h_new = h * scale_y
w_new = w * scale_x
# img2 : only wide
img2 = np.zeros((h, w_new, d))
# img3 : wide height
img3 = np.zeros((h_new, w_new, d))

for j in range(h):
    for i in range(w):
        x = i
        y = j
        x2 = i*scale_x
        y2 = j
        
        img2[y2, x2, :] = img[y, x, :]
        
        if x < w-1:
            dif = img[y, x+1, :] - img[y, x, :]
            for x_shift in range(scale_x):
                img2[y2, x2 + x_shift, :] = img[y, x, :] + dif / scale_x * x_shift

img2 = img2.clip(0, 255).astype(int)
plt.figure()
plt.imshow(img2, vmin = 0, vmax = 255)
plt.axis('off')
# Image.fromarray(img2.astype(np.uint8)).save(img2.jpg)
# plt.figure()
# img2 = Image.fromarray(img).convert('L')
# img2.save('img2.jpg')