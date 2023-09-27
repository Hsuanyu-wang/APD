from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold = sys.maxsize)

img = Image.open('image1.jpg').convert('L')
img = np.array(img)

def show(img, alpha, beta):
    
    img = img.astype(float)
    img = img*alpha + beta
    img = np.clip(img, 0, 255)
    img = img.astype(int)
    
    plt.figure()
    plt.imshow(img, plt.cm.gray, vmin = 0, vmax = 255)
    plt.axis('off')
    
    plt.figure()
    plt.hist(img.flatten(), bins = 20, density = True, facecolor='g')
    img2 = Image.fromarray(img).convert('L')
    img2.save('fileout.jpg')

show(img, alpha = 0.3, beta = 50)

