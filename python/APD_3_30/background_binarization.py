from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import math

image = Image.open('Picture_1.jpg')
plt.figure()
plt.axis('off')
plt.imshow(image, vmin = 0, vmax = 255)

img = np.array(image)

img = img.astype(float)
[h, w, d] = img.shape
img_2 = np.zeros((h, w, d))
img_2 = img.copy()
img_3 = np.zeros((h, w, d))

color_1 = [60, 180, 60]
color_2 = [82, 255, 116]
color_range_1 = [100, 100, 100]

min_x = w
min_y = h
max_x = 0
max_y = 0

for y in range (h):
    for x in range (w):
        if ((np.abs(color_1[0] - img[y, x, 0]) < color_range_1[0]) and \
            (np.abs(color_1[1] - img[y, x, 1]) < color_range_1[1]) and \
            (np.abs(color_1[2] - img[y, x, 2]) < color_range_1[2])):
            
            img_2[y, x, :] = [0, 0, 255]
        else:
            img_3[y, x, :] = [255, 255, 255]
            
            if(x < min_x):
                min_x = x
                
            if(y < min_y):
                min_y = y
                
            if(x > max_x):
                max_x = x
                
            if(y > max_y):
                max_y = y
                           
plt.figure()
plt.axis('off')
img_2 = img_2.astype(np.uint8)
plt.imshow(img_2, vmin = 0, vmax = 255)

fig, ax = plt.subplots()# left_top, wide, hight
rect = plt.Rectangle((min_x, min_y), max_x-min_x, max_y-min_y, edgecolor='r', fill = False)
ax.add_patch(rect)
plt.axis('off')
img_3 = img_3.astype(np.uint8)
plt.imshow(img_3, vmin = 0, vmax = 255)
plt.figure()

plt.show()