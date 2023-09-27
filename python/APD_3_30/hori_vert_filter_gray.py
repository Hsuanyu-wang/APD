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
img_h = np.zeros((h, w, d))
img_v = np.zeros((h, w, d))
img_2 = np.zeros((h, w, d))
img_3 = np.zeros((h, w, d))


Filter = [[1, 0, 1],
          [2, 0, -2],
          [-1, 0, -1] ]

[fh, fw] = np.shape(Filter)
edge_h = math.floor(((fh-1)/2))
edge_w = math.floor(((fw-1)/2))

img_pad = np.zeros((h + 2*edge_h, w + 2*edge_w, d))
img_pad[edge_h:h+edge_h, edge_w:w+edge_w, :] = img[:, :, :]

for y in range(edge_h, h-edge_h):
    for x in range(edge_w, w+edge_w):
        for z in range(3):
            # horizontal
            temp_h = np.multiply(img_pad[y-edge_h:y+edge_w+1, x-edge_h:x+edge_w+1, z], Filter)
            temp_h = temp_h.flatten()
            img_h[y-edge_h, x-edge_h, z] = np.sum(temp_h)
            
        #     # vertical
        #     temp_v = np.multiply(img_pad[y-edge_h:y+edge_w+1, x-edge_h:x+edge_w+1, z], np.matrix(Filter).T)
        #     temp_v = temp_v.flatten()
        #     img_v[y-edge_h, x-edge_h, z] = np.sum(temp_h)
            
            
        #     # horizontal + vertical
        #     temp1 = np.multiply(img_pad[y-edge_h:y+edge_w+1, x-edge_h:x+edge_w+1, z], Filter)
        #     temp1 = temp1.flatten()
            
        #     temp2 = np.multiply(img_pad[y-edge_h:y+edge_w+1, x-edge_h:x+edge_w+1, z], np.matrix(Filter).T)
        #     temp2 = temp2.flatten()
            
        # img_2[y-edge_h, x-edge_h, z] = (np.sum(temp1)**2 + np.sum(temp2)**2)**0.5
            
            # # gray
            # avg = 255 - (img_pad[y-edge_h, x-edge_h, :].mean())
            # img_3[y-edge_h, x-edge_h, :] = [avg, avg, avg]
    
plt.figure()
plt.axis('off')
img_h = np.clip(img_h, 0, 255).astype(int)
plt.imshow(img_h, vmin = 0, vmax = 255)

# plt.figure()
# plt.axis('off')
# img_v = np.clip(img_v, 0, 255).astype(int)
# plt.imshow(img_v, vmin = 0, vmax = 255)

# plt.figure()
# plt.axis('off')
# img_2 = np.clip(img_2, 0, 255).astype(int)
# plt.imshow(img_2, vmin = 0, vmax = 255)

# plt.figure()
# plt.axis('off')
# img_3 = np.clip(img_3, 0, 255).astype(int)
# plt.imshow(img_3, vmin = 0, vmax = 255)

plt.show()
