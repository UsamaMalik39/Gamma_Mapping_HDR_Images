# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:52:39 2020

@author: Malik Usama
"""

import cv2 as cv
import numpy as np


hdr1=cv.imread('C:/EME/7th sem/dip/assignment/#1/handout/data/hw1_atrium.hdr')
hdr2=cv.imread('C:/EME/7th sem/dip/assignment/#1/handout/data/hw1_memorial.hdr')
"""cv.imshow("orignal-1",cv.rotate(hdr1, cv.ROTATE_90_CLOCKWISE))"""
cv.imshow("orignal-1",cv.rotate(hdr1, cv.ROTATE_90_CLOCKWISE))
cv.waitKey(0)

cv.imshow("orignal-2",hdr2)
cv.waitKey(0)

""" images are in bgr format and they are fine  """


"""b,g,r=cv.split(hdr1)
converted=cv.merge([r,g,b])
cv.imshow("converted",converted)
cv.waitKey(0)"""


gray_scaled_1=cv.cvtColor(hdr1,cv.COLOR_BGR2GRAY)
cv.imshow("grayscaled-1",cv.rotate(gray_scaled_1, cv.ROTATE_90_CLOCKWISE))
cv.waitKey(0)
gray_scaled_2=cv.cvtColor(hdr2,cv.COLOR_BGR2GRAY)
cv.imshow("grayscaled-2",gray_scaled_2)
cv.waitKey(0)






gamma_1=0.9
gamma_2=0.9
c=1

"size of hdr1 is (1016,760)"
ldr1=np.zeros((1016,760),np.uint8)
for i in range(0,1016,1):
    for j in range(0,760,1):
        ldr1[i][j]=c*gray_scaled_1[i][j]**gamma_1
        
"size of hdr2 is (768,512)"
ldr2=np.zeros((768,512),np.uint8)
for i in range(0,768,1):
    for j in range(0,512,1):
        ldr2[i][j]=c*gray_scaled_2[i][j]**gamma_2

"""print(np.shape(ldr))
print(gray_scaled_1)
print(ldr)"""


cv.imshow("ldr_1",np.array(ldr1))
cv.waitKey(0)
cv.imshow("ldr_2",np.array(ldr2))
cv.waitKey(0)

"""
c=0.3 gamma=1.2
c=0.5 gamma=1.1
c=1   gamma=0.9

"""



"""
Task C
"""

c=1
gamma_forall=0.9
gamma_forb=0.9
gamma_forg=0.8
gamma_forr=0.7

"for same gamma hdr 1 k liye"

b,g,r=cv.split(hdr1)
b=c*b**gamma_forall
g=c*g**gamma_forall
r=c*r**gamma_forall
same_gamma_hdr1=cv.merge((b,g,r))
"abhi data type change krni ha from float64 to uint8"
same_gamma_hdr1=same_gamma_hdr1.astype(np.uint8)
        
"for different gamma hdr 1 "


b,g,r=cv.split(hdr1)
b=c*b**gamma_forb
g=c*g**gamma_forg
r=c*r**gamma_forr
different_gamma_hdr1=cv.merge((b,g,r))
"abhi data type change krni ha from float64 to uint8"
different_gamma_hdr1=different_gamma_hdr1.astype(np.uint8)




cv.imshow("Same Gamma Img 1",cv.rotate(same_gamma_hdr1, cv.ROTATE_90_CLOCKWISE))
cv.waitKey(0)
cv.imshow("Different Gamma Img 1",cv.rotate(np.array(different_gamma_hdr1), cv.ROTATE_90_CLOCKWISE))
cv.waitKey(0)


"for same gamma hdr 2  "
b,g,r=cv.split(hdr2)
b=c*b**gamma_forall
g=c*g**gamma_forall
r=c*r**gamma_forall
same_gamma_hdr2=cv.merge((b,g,r))
"abhi data type change krni ha from float64 to uint8"
same_gamma_hdr2=same_gamma_hdr2.astype(np.uint8)
        
"for different gamma hdr 2  "


b,g,r=cv.split(hdr2)
b=c*b**gamma_forb
g=c*g**gamma_forg
r=c*r**gamma_forr
different_gamma_hdr2=cv.merge((b,g,r))
"abhi data type change krni ha from float64 to uint8"
different_gamma_hdr2=different_gamma_hdr2.astype(np.uint8)




cv.imshow("Same Gamma Img 2",same_gamma_hdr2)
cv.waitKey(0)
cv.imshow("Different Gamma Img 2",np.array(different_gamma_hdr2))
cv.waitKey(0)









