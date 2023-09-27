from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import math
from matplotlib.patches import Circle
import cv2

cap = cv2.VideoCapture('cockroach.mp4')
fig, ax = plt.subplots()

num = 0

color_1 = [37, 77, 175]
color_2 = [159, 28, 70]
color_range_1 = [50, 50, 50]
color_range_2 = [50, 50, 50]

while(cap.isOpened()):
    ret, img = cap.read()
    if(ret == True):# if the image is obtaained
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.array(img)
        [h, w, d] = img.shape
        
        
        pos_1 = []
        pos_2 = []
        
        for y in range(0, h, 1):
            for x in range(0, w, 1):
                if ((np.abs(color_1[0] - img[y, x, 0]) < color_range_1[0]) and \
                    (np.abs(color_1[1] - img[y, x, 1]) < color_range_1[1]) and \
                    (np.abs(color_1[2] - img[y, x, 2]) < color_range_1[2])):
                    
                    img[y, x, :] = [0, 0, 255]
                    pos_1.append([y, x])
                    
                if ((np.abs(color_2[0] - img[y, x, 0]) < color_range_2[0]) and \
                    (np.abs(color_2[1] - img[y, x, 1]) < color_range_2[1]) and \
                    (np.abs(color_2[2] - img[y, x, 2]) < color_range_2[2])):
                    
                    img[y, x, :] = [255, 0, 0]
                    pos_2.append([y, x])
        
        r = 15
        ax.cla() #clear the picture (if you have some circle)
        if len(pos_1) > 0:
            xy_blue = np.mean(pos_1, axis = 0)
            circ_1 = Circle((xy_blue[1], xy_blue[0]), r, color='blue', fill = False)
            ax.add_patch(circ_1)
            
        if len(pos_2) > 0:
            xy_red = np.mean(pos_2, axis = 0)
            circ_2 = Circle((xy_red[1], xy_red[0]), r, color='red', fill = False)
            ax.add_patch(circ_2)
            
        plt.axis('off')
        ax.imshow(img)
        plt.savefig('OutFig/Out_' + str(num) + '.jpg')
        num = num + 1
        
    else:
        break
    
cap.release()
    
    