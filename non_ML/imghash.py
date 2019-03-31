# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 03:40:21 2019

@author: ZZ
"""

import cv2
 
def ahash(image):
    image =  cv2.resize(image, (8,8), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    s = 0
    ahash_str = ''
    for i in range(8):
        for j in range(8):
            s = s+gray[i, j]
    avg = s/64
    ahash_str  = ''
    for i in range(8):
        for j in range(8):
            if gray[i,j]>avg:
                ahash_str = ahash_str + '1'
            else:
                ahash_str = ahash_str + '0'
    result = ''
    for i in range(0, 64, 4):
        result += ''.join('%x' % int(ahash_str[i: i + 4], 2))
    return result
 
def dhash(image):
    image = cv2.resize(image,(9,8),interpolation=cv2.INTER_CUBIC )
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    dhash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i,j]>gray[i, j+1]:
                dhash_str = dhash_str + '1'
            else:
                dhash_str = dhash_str + '0'
    result = ''
    for i in range(0, 64, 4):
        result += ''.join('%x'%int(dhash_str[i: i+4],2))
    return result
 
def campHash(hash1, hash2):
    n = 0
    if len(hash1) != len(hash2):
        return -1
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n+1
    return n
for i in range(4):
    for j in range(4):
        img1 = cv2.imread("d:/pics/faces/{}.jpg".format(i+1))
        img2 = cv2.imread("d:/pics/faces/{}_.jpg".format(j+1))
        hash1 = ahash(img1)
        print('img1 ahash',hash1)
        hash2= dhash(img1)
        print('img1 dhash',hash2)
        hash3= ahash(img2)
        print('img2 ahash',hash3)
        hash4= dhash(img2)
        print('img2 dhash',hash4)
        camphash1 = campHash(hash1, hash3)
        camphash2= campHash(hash2, hash4)
        print(i+1,j+1,"ahash：",camphash1)
        print(i+1,j+1,"dhash：",camphash2)
