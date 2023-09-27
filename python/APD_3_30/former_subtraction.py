from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import math
from matplotlib.patches import Circle
import cv2

cap = cv2.VideoCapture('Video.avi')
fig, ax = plt.subplots()

num = 0
while(cap.isOpened()):
    ret, img = cap.read()
    if(ret == True):# if the image is obtaained
    
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.array(img).astype(int)
        [h, w, d] = img.shape
        
        if num >= 1:
            img_2 = np.abs(img - img_prev)
            
            threshold = 30
            min_x = w
            min_y = h
            max_x = 0
            max_y = 0
            count = 0
        
            for y in range(0, h, 1):
                for x in range(0, w, 1):
                    if ((img_2[y, x, 0] > threshold) or \
                        (img_2[y, x, 1]) > threshold or \
                        (img_2[y, x, 2] > threshold)):
                        
                        count = count + 1
                        
                        if(x < min_x):
                            min_x = x
                            
                        if(y < min_y):
                            min_y = y
                            
                        if(x > max_x):
                            max_x = x
                            
                        if(y > max_y):
                            max_y = y
            
            ax.cla() #clear the picture (if you have some circle)
            if count > 10:
                rect = plt.Rectangle((min_x, min_y), max_x-min_x, max_y-min_y, edgecolor='r', fill=False)
                ax.add_patch(rect)
                
            plt.axis('off')
            ax.imshow(img)
            
            plt.savefig('OutFig/Out_' + str(num) + '.jpg')
        
        img_prev = img
        num = num + 1
        
    else:
        break
    
cap.release()
    
    