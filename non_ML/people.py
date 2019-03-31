# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 23:53:38 2019

@author: ZZ
"""

import cv2
import numpy as np
cap=cv2.VideoCapture("d:/pics/camera1.avi")
count=0
frame=0
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
while frame<4000:
    if(frame%10!=0):
        ret,fra=cap.read()
        frame+=1
    if(frame%10==0):
        frame+=1
        ret,fra=cap.read()
        gray = cv2.cvtColor(fra,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,
        1.3,
        5
        )
        if(len(faces)!=0):
            for (x,y,w,h) in faces:
                refine=np.zeros((w,h,3))
                for m in range(w):
                        for j in range(h):
                            for k in range(3):
                                refine[m][j][k]=fra[y+j][x+m][k]
                cv2.imwrite("d:/pics/faces/{}.jpg".format(count),refine)
                count+=1
        else:
            continue
 