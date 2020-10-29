import numpy as np
import matplotlib.pyplot as plt
import cv2
import os           #os.system('Pause') 로 잠시 멈출 일 있었음

def showVideo():
    try:
        print('Ready Camera')
        cap = cv2.VideoCapture(0)
    except:
        print('False Camera')
        return

    cap.set(3,480)
    cap.set(4,320)
    while cap.isOpened():
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('video',gray)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def writeVideo():
    try:
        print('Ready to Record')
        cap = cv2.VideoCapture(0)
    except:
        print('False Ready to Record')
        return

    fcc = cv2.VideoWriter_fourcc('D','I','V','X')
    fps = 20.0
    width = int(cap.get(3))
    height = int(cap.get(4))
    out = cv2.VideoWriter('mycam.avi',fcc,fps,(width,height))
    print('Start Record')

    while cap.isOpened():
        ret, frame = cap.read()
        
        cv2.imshow('video',frame)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('Finish Record')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    start = int(input())
    if start == 1:
        showVideo()
    elif start == 2:
        writeVideo()