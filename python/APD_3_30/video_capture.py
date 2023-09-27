from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import math
from matplotlib.patches import Circle
import cv2
# from cv2 import VideoCapture
# from cv2 import waitKey

cap = cv2.VideoCapture('cockroach.mp4')
fig, ax = plt.subplots()

num = 0
while(cap.isOpened()):
    ret, img = cap.read()
    if(ret == True):# if the image is obtaained
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.array(img)
        plt.axis('off')
        ax.cla() #clear the picture (if you have some circle)
        
        ax.imshow(img)
        plt.savefig('OutFig/Out_' + str(num) + '.jpg')
        num = num + 1
    else:
        break
    
cap.release()
    
    