from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
np.set_printoptions(threshold = sys.maxsize)

def my_yuv2rgb(YUV):
    YUV = YUV.astype(float)
    
    Y = YUV[:, :, 0]
    U = YUV[:, :, 1]
    V = YUV[:, :, 2]
    
    R = Y + (1.13983 * (V - 128))
    G = Y - (0.39465 * (U - 128)) - (0.58060 * (V - 128))
    B = Y + (2.03211 * (U - 128))

    R = R.reshape((R.shape[0], R.shape[1], 1))
    G = G.reshape((G.shape[0], G.shape[1], 1))
    B = B.reshape((B.shape[0], B.shape[1], 1))
    
    RGB = np.concatenate([R, G, B], axis=2)
    RGB = np.round(RGB).clip(0, 255).astype(int)
    
    return RGB

def show_yuv(y, u, v):
    
    YUV = np.concatenate([y*np.ones((255, 255, 1)),
                          u*np.ones((255, 255, 1)),
                          v*np.ones((255, 255, 1))], axis = 2)
    RGB = my_yuv2rgb(YUV);    
    
    plt.figure()
    plt.imshow(RGB, vmin = 0, vmax = 255)
    plt.axis('off')
    
def  show_all_yuv():
    y = 128*np.ones((255,255,1))
    u = np.ones((255,255,1))
    v = np.ones((255,255,1))
    
    for i in range(255):
        u[:, i, 0] = i
        v[i, :, 0] = 255-i
    
    YUV = np.concatenate([y,u,v],axis=2)
    RGB = my_yuv2rgb(YUV)
    
    plt.figure()
    plt.imshow(RGB, vmin=0, vmax=255)
    plt.axis('off')

show_yuv(128, 0, 255)

show_all_yuv()