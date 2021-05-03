import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage():
    imgfile = 'IndStudy/AI/img/hoodT_Img.jpg'
    img = cv2.imread(imgfile,cv2.IMREAD_GRAYSCALE)
    plt.imshow(img,cmap='gray',interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.title('model')
    plt.show()

#     cv2.namedWindow('model',cv2.WINDOW_NORMAL)
#     cv2.imshow('model',img)

#     k = cv2.waitKey(0) & 0xFF

#     if k == 27:
#         cv2.destroyAllWindows()
#     elif k == ord('c'):
#         cv2.imwrite('IndStudy/AI/img/hoodT_Img_copy.jpg',img)
#         cv2.destroyAllWindows()

showImage()