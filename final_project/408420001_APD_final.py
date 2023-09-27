from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
# from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import sys
import math
import random
import numpy as np
import itertools  
np.set_printoptions(threshold = sys.maxsize)
# from colorsys import hsv_to_rgb, rgb_to_hsv

# =============================================================================
# input processing
# =============================================================================
image = Image.open('cat-3846780_640.jpg')
img = np.array(image)
img = img.astype(float)
img = img.clip(0, 255).astype(int)
[h,w,d] = img.shape

plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img, vmin = 0, vmax = 255)


# gray

img_g = Image.open('cat-3846780_640.jpg').convert('L')
img_g = np.array(img_g)
img_g = img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
[hg,wg] = img_g.shape
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("gray-scale.jpg", bbox_inches='tight', pad_inches = 0)

img_bin = np.copy(img_g)

# # =============================================================================
# # 1.naive method
# # =============================================================================
img_nmsk = np.zeros((h,w))
for y in range(h):
    for x in range(w):
        img_nmsk[y,x] = 128
img_nmsk.astype(float)
img_nmsk = img_nmsk.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_nmsk, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("naive mask.jpg", bbox_inches='tight', pad_inches = 0)

# naive process

img_niv = np.copy(img_g)
for y in range(h):
    for x in range(w):  
        img_niv[y,x] = img_niv[y,x] + img_nmsk[y,x]
img_niv.astype(float)
img_niv = img_niv.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_niv, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("naive_process.jpg", bbox_inches='tight', pad_inches = 0)
# plt.title('processing by naive mosaic mask')  
  
# naive reverse

for y in range(h):
    for x in range(w):  
        img_niv[y,x] = img_niv[y,x] - img_nmsk[y,x]
img_niv.astype(float)
img_niv = img_niv.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_niv, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("naive_retrieval.jpg", bbox_inches='tight', pad_inches = 0)

# =============================================================================
# 1-2. xor method
# =============================================================================
img_niv_xor = np.copy(img_g)
for y in range(h):
    for x in range(w):  
        img_niv_xor[y,x] = img_niv_xor[y,x] ^ img_nmsk[y,x]
img_niv_xor.astype(float)
img_niv_xor = img_niv_xor.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_niv_xor, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("xor_process.jpg", bbox_inches='tight', pad_inches = 0)

for y in range(h):
    for x in range(w):  
        img_niv_xor[y,x] = img_niv_xor[y,x] ^ img_nmsk[y,x]
img_niv_xor.astype(float)
img_niv_xor = img_niv_xor.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_niv_xor, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("naive_xor_retrieval.jpg", bbox_inches='tight', pad_inches = 0)

# =============================================================================
# 2.designed mosaic key
# =============================================================================
img_msq = np.zeros((h, w))
img_msq = img_msq.astype(float)
img_msq = img_msq.clip(0, 255).astype(int)
for y in range(h):
    for x in range(w):
        if(y%2==0 and x%2!=0):
            img_msq[y,x] = 255
        elif(y%2!=0 and x%2==0):
            img_msq[y,x] = 255

plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_msq, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("mosaic.jpg", bbox_inches='tight', pad_inches = 0)

# XOR process

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ img_msq[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)

plt.savefig("mosaic-processed.jpg", bbox_inches='tight', pad_inches = 0)

# XOR reverse

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ img_msq[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("mosaic-retrieval.jpg", bbox_inches='tight', pad_inches = 0)

# =============================================================================
# 3.hide with other (gray) picture
# =============================================================================
image_oip = Image.open('dragon-238931_1280.jpg').convert('L')
img_oip = np.array(image_oip)
img_oip = img_oip.astype(float)
img_oip = img_oip.clip(0, 255).astype(int)
[h_oip, w_oip] = img_oip.shape

plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_oip, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("picture_gray.jpg", bbox_inches='tight', pad_inches = 0)

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ img_oip[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("picture_process.jpg", bbox_inches='tight', pad_inches = 0)

# reverse

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ img_oip[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("picture_retrieval.jpg", bbox_inches='tight', pad_inches = 0)


# =============================================================================
# hide with special image/water mark:special picture
# =============================================================================
# 2D
# mrk = np.zeros((h, w,))
# mrk.astype(float)
# mrk = mrk.clip(0, 255).astype(int)
# for y in range(h):
#     for x in range(w):
#         if( y==x or x==(w/2) or y==(w-x) or (h-y)==x or (h-y)==(w-x)):
#             mrk[y,x] = 128

# 3D
mrk = np.zeros((h, w))
mrk.astype(float)
mrk = mrk.clip(0, 255).astype(int)

for y in range(h):
    for x in range(w):
        if( abs(y-x)<5 or abs(x-(w/2))<5 or abs(y-(w-x))<5 or abs((h-y)-x)<5 or abs((h-y)-(w-x))<5):
            mrk[y,x] = 255
        if( (abs(y-(h/2))<30 and abs(y-(h/2))>10) and (abs(x-(w/2))<30 and abs(x-(w/2))>10) ):
            mrk[y,x] = 255
            # mrk[y,x,0] = mrk[y,x,1] = mrk[y,x,2] = img_oip[y,x]
        if( abs(y-h/2)<5 or abs(y-h/3)<5 or abs(y-2*h/3)<5):
            mrk[y,x] = 255

plt.figure(dpi=500)
plt.axis('off')
plt.imshow(mrk, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("mark.jpg", bbox_inches='tight', pad_inches = 0)

# process/hide image(use other picture)

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ mrk[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("marked_image.jpg", bbox_inches='tight', pad_inches = 0)

# reverse

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ mrk[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("marked_retrieval.jpg", bbox_inches='tight', pad_inches = 0)


# =============================================================================
# LSB
# =============================================================================
LSB = np.zeros((h,w))
LSB.astype(float)
LSB = LSB.clip(0, 255).astype(int)

for y in range(h):
    for x in range(w):
        # if(y%2==0 and x%2!=0):
        #     LSB[y,x] = 31
        # elif(y%2!=0 and x%2==0):
        #     LSB[y,x] = 31
        if( abs(y-x)<5 or abs(x-(w/2))<5 or abs(y-(w-x))<5 or abs((h-y)-x)<5 or abs((h-y)-(w-x))<5):
            LSB[y,x] = 15
        if( (abs(y-(h/2))<30 and abs(y-(h/2))>10) and (abs(x-(w/2))<30 and abs(x-(w/2))>10) ):
            LSB[y,x] = 15
            # mrk[y,x,0] = mrk[y,x,1] = mrk[y,x,2] = img_oip[y,x]
        if( abs(y-h/2)<5 or abs(y-h/3)<5 or abs(y-2*h/3)<5):
            LSB[y,x] = 15

plt.figure(dpi=500)
plt.axis('off')
plt.imshow(LSB, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("LSB.jpg", bbox_inches='tight', pad_inches = 0)

#LSB process

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ LSB[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)

plt.savefig("LSB_image.jpg", bbox_inches='tight', pad_inches = 0)

# LSB reverse

for y in range(h):
    for x in range(w):  
        img_g[y,x] = img_g[y,x] ^ LSB[y,x]

img_g.astype(float)
img_g = img_g.clip(0, 255).astype(int)
plt.figure(dpi=500)
plt.axis('off')
plt.imshow(img_g, plt.cm.gray, vmin = 0, vmax = 255)
plt.savefig("LSB_retrieval.jpg", bbox_inches='tight', pad_inches = 0)


