import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from PIL import Image
import numpy as np 
import math

img = Image.open('cockroach.jpg')
fig, ax = plt.subplots()
plt.axis('off')
ax.imshow(img, vmin = 0, vmax = 255)

circ = Circle((50, 100), 30, color = 'blue', fill = False)
ax.add_patch(circ)
plt.show()