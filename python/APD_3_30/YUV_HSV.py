from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import sys
from colorsys import hsv_to_rgb, rgb_to_hsv
import numpy as np 
np.set_printoptions(threshold = sys.maxsize)

def my_rgb2yuv(RGB):
    RGB = RGB.astype(float)
    
    R = RGB[:, :, 0]
    G = RGB[:, :, 1]
    B = RGB[:, :, 2]
    
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    U = -0.169 * R - 0.331 * G + 0.5* B + 128
    V = 0.5 * R - 0.419 * G -0.081 * B + 128
    
    Y = Y.reshape((R.shape[0], R.shape[1], 1))
    U = U.reshape((G.shape[0], G.shape[1], 1))
    V = V.reshape((B.shape[0], B.shape[1], 1))
    
    YUV = np.concatenate([Y, U, V], axis=2)
    YUV = np.round(YUV).clip(0, 255).astype(int)
    
    return YUV
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
def YUV_modify(RGB, y_bias, u_bias, v_bias):
    YUV =   my_rgb2yuv(RGB)
    YUV[:, :, 0] = YUV[:, :, 0] + y_bias
    YUV[:, :, 1] = YUV[:, :, 1] + u_bias
    YUV[:, :, 2] = YUV[:, :, 2] + v_bias
    RGB = my_yuv2rgb(YUV)
    plt.figure()
    plt.imshow(RGB, vmin = 0, vmax = 255)
    plt.axis('off')
def HSV_modify(RGB, h_bias, s_bias, v_bias):
    
    RGB = RGB.astype(float)
    
    HSV = np.zeros((RGB.shape[0], RGB.shape[1], RGB.shape[2]))
    for i in range(RGB.shape[0]):
        for j in range(RGB.shape[1]):
            H, S, V = rgb_to_hsv(RGB[i, j, 0], RGB[i, j, 1], RGB[i, j, 2])
            HSV[i, j, 0] = H
            HSV[i, j, 1] = S
            HSV[i, j, 2] = V
            # print(H, S, V)
            # print(hsv_to_rgb(H, S, V))
    HSV[:, :, 0] = HSV[:, :, 0] + h_bias
    HSV[:, :, 1] = HSV[:, :, 1] + s_bias
    HSV[:, :, 2] = HSV[:, :, 2] + v_bias
    
    HSV[:, :, 0] = np.clip(HSV[:, :, 0], 0, 1)
    HSV[:, :, 1] = np.clip(HSV[:, :, 1], 0, 1)
    HSV[:, :, 2] = np.clip(HSV[:, :, 2], 0, 255)
    
    for i in range(HSV.shape[0]):
        for j in range(HSV.shape[1]):
            R, G, B = hsv_to_rgb(HSV[i, j, 0], HSV[i, j, 1], HSV[i, j, 2])
            RGB[i, j, 0] = R
            RGB[i, j, 1] = G
            RGB[i, j, 2] = B
            
    RGB = RGB.clip(0, 255).astype(int)
    
    plt.figure()
    plt.imshow(RGB, vmin = 0, vmax = 255)
    plt.axis('off')
    
img = Image.open('image1.jpg')
img = np.array(img)

plt.figure()
plt.imshow(img, vmin = 0, vmax = 255)
plt.axis('off')

H, S, V = rgb_to_hsv(10, 20, 30)
print(H, S, V)
print(hsv_to_rgb(H, S, V))

YUV_modify(img, y_bias = 100, u_bias = 0, v_bias = 0)

HSV_modify(img, h_bias = 0.0, s_bias = 0.0, v_bias =0.0)