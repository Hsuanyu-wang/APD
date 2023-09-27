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

N = 3
sigma = 1.5

bias = math.floor((N-1)/2)

Filter = np.zeros((N, N))
# print(np.shape(img))
[fh, fw] = np.shape(Filter)
# print((np.shape(Filter)))
edge_h = math.floor(((fh-1)/2))
edge_w = math.floor(((fw-1)/2))

for y in range(N):
    for x in range(N):
        Filter[y][x] = 1/(2*np.pi*(sigma**2))*math.exp(-((bias-y)**2 + (bias-x)**2)/(2*(sigma**2)) )

# img_pad = np.zeros((h + 2*edge_h, w + 2*edge_w, d))
# img_pad[edge_h:h+edge_h, edge_w:w+edge_w, :] = img[:, :, :]

print(Filter.flatten())
filter_sum = np.sum(np.reshape(Filter, [fw * fh, 1]))

# plt.figure()
# plt.axis('off')
# img_2 = np.clip(img_2, 0, 255).astype(int)
# plt.imshow(img_2, vmin = 0, vmax = 255)

for y in range(edge_h, h-edge_h):
    for x in range(edge_w, w-edge_w):
        for z in range(d):
            temp = np.multiply(img[y-edge_h:y+edge_h+1, x-edge_w:x+edge_w+1, z], Filter)
            temp = temp.flatten()
            img_2[y-edge_h, x-edge_w, z] = np.sum(temp) / filter_sum
    
plt.figure()
plt.axis('off')
img_2 = np.clip(img_2, 0, 255).astype(int)
plt.imshow(img_2, vmin = 0, vmax = 255)

plt.show()
