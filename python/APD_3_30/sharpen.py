from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
import math
    
np.set_printoptions(threshold = sys.maxsize)

image = Image.open('Lenna.jpg')

plt.figure()
plt.imshow(image, vmin = 0, vmax = 255)
plt.axis('off')

img = np.array(image)
img = img.astype(float)
[h, w, d] = img.shape
img_2 = np.zeros((h, w, d))

a = 0.08

Filter = [[0, -a, 0],
          [-a, 4*a+1, -a],
          [0, -a, 0]]


[fh, fw] = np.shape(Filter)
edge_h = math.floor(((fh-1)/2))
edge_w = math.floor(((fw-1)/2))

img_pad = np.zeros((h + 2*edge_h, w + 2*edge_w, d))
img_pad[edge_h:h+edge_h, edge_w:w+edge_w, :] = img[:, :, :]


        
for y in range(edge_h, h-edge_h):
    for x in range(edge_w, w+edge_w):
        for z in range(3):
            temp = np.multiply(img_pad[y-edge_h:y+edge_w+1, x-edge_h:x+edge_w+1, z], Filter)
            temp = temp.flatten()
            img_2[y-edge_h, x-edge_h, z] = np.sum(temp)
    
plt.figure()
plt.axis('off')
img_2 = np.clip(img_2, 0, 255).astype(int)
plt.imshow(img_2, vmin = 0, vmax = 255)

plt.show()
