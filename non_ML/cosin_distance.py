# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 01:13:15 2019

@author: ZZ
"""

from PIL import Image
from numpy import average, dot, linalg
import time
 
def get_thum(image, size=(64,64), greyscale=False):
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        image = image.convert('L')
    return image
def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thum(image1)
    image2 = get_thum(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    res = dot(a / a_norm, b / b_norm)
    return res
start=time.time() 
for i in range(4):
    for j in range(4):
        image1 = Image.open("d:/pics/faces/{}.jpg".format(i+1))
        image2 = Image.open("d:/pics/faces/{}_.jpg".format(j+1))
        cosin = image_similarity_vectors_via_numpy(image1, image2)
        print(i+1,j+1,'Cosine similarity ',cosin)
