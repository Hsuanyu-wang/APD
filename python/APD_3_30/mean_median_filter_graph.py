from PIL import Image, ImageDraw, ImageFont
# from PIL import ImageFont
# from PIL import ImageDraw
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

[h, w, d] = img.shape
img = imnoise(img, 0.008)

plt.figure()
plt.imshow(img, vmin = 0, vmax = 255)
plt.axis('off')
Image.fromarray(img).save('img_noise.jpg')

N = 3
edge = int((N-1)/2)

img = img.astype(float)
img_2 = np.zeros((h, w, d))
# 
img_pad = np.zeros((h + edge * 2, w + edge * 2, d))
img_pad[edge:edge+h, edge:edge+w, :] = img[:, :, :]
# 
for y in range(edge, h-edge, 1):
    for x in range(edge, w-edge, 1):
        for d in range(3):
            temp = img_pad[y-edge:y+edge+1, x-edge:x+edge+1, d]
            temp = temp.flatten()
            img_2[y, x, d] = int(np.median(temp))
            # img_2[y, x, d] = int(np.mean(temp))
            
plt.figure()
img_2 = img_2.clip(0, 255).astype(int)
plt.imshow(img_2, vmin = 0, vmax = 255)
plt.axis('off')
Image.fromarray(img_2.astype(np.uint8)).save('img_2.jpg')

plt.figure(figsize = (8, 6))
plt.subplot(3, 2, 1)
plt.plot(img[:, :10, 0])
plt.title('R Before')

plt.subplot(3, 2, 2)
plt.plot(img_2[:, :10, 0])
plt.title('R After')

plt.subplot(3, 2, 3)
plt.plot(img[:, :10, 1])
plt.title('G Before')

plt.subplot(3, 2, 4)
plt.plot(img_2[:, :10, 1])
plt.title('G After')

plt.subplot(3, 2, 5)
plt.plot(img[:, :10, 2])
plt.title('B Before')

plt.subplot(3, 2, 6)
plt.plot(img_2[:, :10, 2])
plt.title('B After')