from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 

import math

np.set_printoptions(threshold = sys.maxsize)

img = Image.open('Lenna.jpg')
img = np.array(img)

plt.figure()
plt.axis('off')
plt.imshow(img, vmin = 0, vmax = 255)

h, w, d = img.shape

img2 = np.zeros((h, w, d))
img3 = np.zeros((h, w, d))

angle = 30

theta = angle * (np.pi/180)

for y in range(h):
    for x in range(w):
        x_new = int(np.round(x * math.cos(theta) - y * math.sin(theta)))
        y_new = int(np.round(x * math.sin(theta) + y * math.cos(theta)))
        
        if x_new < w and y_new < h and x_new > 0 and  y_new > 0:
            img2[y_new, x_new, :] = img[y, x, :]
            img3[y, x, :] = img[y_new, x_new, :]

# =============================================================================
# rot_mid
# =============================================================================
h_new = int(np.round(h * math.cos(theta) + w * math.sin(theta)))
w_new = int(np.round(w * math.cos(theta) + h * math.sin(theta)))

img4 = np.zeros((h_new, w_new, d))

if angle >= 0:
    x_offset = int(np.round(h *  math.sin(theta)))
    y_offset = 0
else:
    x_offset = 0
    y_offset = int(np.round(w *  math.sin(-theta)))

for y in range(h_new):
    for x in range(w_new):
        x_big = int(np.round((x-x_offset) * math.cos(-theta) - (y-y_offset) * math.sin(-theta)))
        y_big = int(np.round((x-x_offset) * math.sin(-theta) + (y-y_offset) * math.cos(-theta)))
        
        # rotate + align center ?
        if y_big > 0 and y_big < w and x_big > 0 and x_big < h:
            # img4[y_big, x_big, :] = img[y, x, :]
            img4[y, x, :] = img[y_big, x_big, :]


img2 = img2.clip(0, 255).astype(int)
img3 = img3.clip(0, 255).astype(int)
img4 = img4.clip(0, 255).astype(int)

# plt.figure()
# plt.imshow(img, vmin = 0, vmax = 255)
# plt.axis('off')

plt.figure()
plt.imshow(img2, vmin = 0, vmax = 255)
plt.axis('off')

plt.figure()
plt.imshow(img3, vmin = 0, vmax = 255)
plt.axis('off')

plt.figure()
plt.imshow(img4, vmin = 0, vmax = 255)
plt.axis('off')
plt.savefig('rot_mid.jpg')