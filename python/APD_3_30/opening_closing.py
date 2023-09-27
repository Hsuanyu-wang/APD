from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
import math

img = Image.open('img2.jpg').convert('L')
img = np.array(img)

# plt.figure()
# plt.hist(img.flatten(), bins = 80, density = False, facecolor='b')
# # plt.hist(img, bins = 20, density = False, facecolor='b')

[h, w] = img.shape
img_bin = np.zeros((h, w))
# img2 = np.zeros((h, w))

plt.figure()
plt.axis('off')
img = img.clip(0, 255).astype(int)     
plt.imshow(img, plt.cm.gray, vmin = 0, vmax = 255)

threshold = 140

for y in range(h):
    for x in range(w):
        img_bin[y][x] = (img[y][x] > threshold)
 
# plt.figure()
# plt.axis('off')
# img_bin = img_bin.clip(0, 1).astype(int)     
# plt.imshow(img_bin, plt.cm.gray, vmin = 0, vmax = 1)  


def dil(img_bin, time):
    N = 5
    edge = math.floor((N-1)/2)
    img_dil = np.zeros((h, w))
    for n in range(time):
        for y in range(edge, h-edge):
            for x in range(edge, w-edge):
                temp = img_bin[y-edge:y+edge+1, x-edge:x+edge+1]
                temp = temp.flatten()
                if np.sum(temp) < N*N:
                    img_dil[y, x] = 0
                else:
                    img_dil[y, x] = 1
        img_bin = img_dil.copy()
    return img_bin
                
def ero(img_bin, time):
    N = 3
    edge = math.floor((N-1)/2)
    img_ero = np.zeros((h, w))
    for n in range(time):
        for y in range(edge, h-edge):
            for x in range(edge, w-edge):
                temp = img_bin[y-edge:y+edge+1, x-edge:x+edge+1]
                temp = temp.flatten()
                if np.sum(temp) > 0:
                    img_ero[y, x] = 1
                else:
                    img_ero[y, x] = 0
        img_bin = img_ero.copy()
    return img_bin
            
def opening(img, m, n):
    imgt = np.zeros((h, w))
    imgt = ero(img, m)
    imgt = dil(imgt, n)
    return imgt

def closing(img, m, n):
    imgt = np.zeros((h, w))
    imgt = dil(img, m)
    imgt = ero(imgt, n)
    return imgt

img_bin = opening(img_bin, 6, 1)
# img_bin = closing(img_bin, 6, 3)
            
# plt.figure()
# plt.axis('off')
# img_bin = img_bin.clip(0, 1).astype(int)
# plt.imshow(img_bin, plt.cm.gray, vmin = 0, vmax = 1)
# # plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 1)