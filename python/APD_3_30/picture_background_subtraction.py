import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image
import numpy as np 
import math

img_back = Image.open('Picture_2_1.jpg')
plt.figure()
plt.axis('off')
plt.imshow(img_back, vmin = 0, vmax = 255)

img = Image.open('Picture_2_2.jpg')
plt.figure()
plt.axis('off')
plt.imshow(img, vmin = 0, vmax = 255)

img = np.array(img).astype(int)
img_back = np.array(img_back).astype(int)

[h, w, d] = img.shape
img_3 = np.zeros((h, w, d))
img_2 = np.abs(img - img_back)

threshold = 100
for y in range (h):
    for x in range (w):
        if ((img_2[y, x, 0] > threshold) or \
            (img_2[y, x, 1]) > threshold or \
            (img_2[y, x, 2] > threshold)):
            img_3[y, x, :] = [255, 255, 255]
            
plt.figure()
plt.axis('off')
img_2 = img_2.astype(np.uint8)
plt.imshow(img_2, vmin = 0, vmax = 255)

plt.figure()
plt.axis('off')
img_3 = img_3.astype(np.uint8)
plt.imshow(img_3, vmin = 0, vmax = 255)

plt.show()