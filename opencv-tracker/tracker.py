# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 02:15:06 2019

@author: ZZ
"""

import cv2
def resize(img):
    fra=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)),interpolation=cv2.INTER_AREA)
    return fra
tracker1=cv2.TrackerTLD_create()
tracker2=cv2.TrackerBoosting_create()
tracker3=cv2.TrackerMIL_create()
tracker4=cv2.TrackerKCF_create()
tracker5=cv2.TrackerMedianFlow_create()
tracker6=cv2.TrackerCSRT_create()
tracker=tracker6
cap=cv2.VideoCapture("d:/pics/konsen/kosen/output11.avi")
wid=cap.get(3)
height=cap.get(4)
ret,fra=cap.read()
fra=resize(fra)
roi=cv2.selectROI(fra,False)
ret=tracker.init(fra,roi)
while True:
    ret,fra=cap.read()
    if ret:
        fra=resize(fra)
        success,roi=tracker.update(fra)
        (x,y,w,h)=tuple(map(int,roi))
        if success:
            p1=(x,y)
            p2=(x+w,y+h)
            cv2.rectangle(fra,p1,p2,(0,255,0),3)
        else:
            cv2.putText(fra,"Tracking Failed",(int(wid/8),int(height/8)),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),3)
        cv2.imshow("img",fra)
        k=cv2.waitKey(1)
        if k==27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
    
