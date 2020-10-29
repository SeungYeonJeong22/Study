import cv2
import matplotlib.pyplot as plt

def showImg():
    img_file = 'IndStudy/AI/img/hoodT_Img.jpg'
    img = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)
    # plt.imshow(img,cmap = 'gray',interpolation='bicubic')
    # plt.xticks([])
    # plt.yticks([])
    # plt.title('model')
    # plt.show()

    cv2.namedWindow('model',cv2.WINDOW_NORMAL)
    cv2.imshow('model',img)

    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        print('Img copy')
        cv2.imwrite('IndStudy/AI/img/img_Copy.jpg')
    cv2.destroyAllWindows()

def showVideo():
    try:
        print('Ready showVideo')
        cap = cv2.VideoCapture(0)
    except:
        print('False start showVideo')
        return
    
    cap.set(3,480)
    cap.set(4,340)

    while True:
        ret, frame = cap.read()
        if ret == False:
            print('False return')
            break
        
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('video',frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('Close frame')
            break
    
    cv2.destroyAllWindows()
    cap.release()

def writeRecord():
    try:
        print('Ready WriteRecord')
        cap = cv2.VideoCapture(0)
    except:
        print('False Ready Record')
        return

    fcc = cv2.VideoWriter_fourcc('D','I','V','X')
    fps = 20
    width = int(cap.get(3))
    height = int (cap.get(4))
    out = cv2.VideoWriter('IndStudy/AI/video/webcam2.avi',fcc,fps,(width,height))

    while True:
        ret, frame = cap.read()

        if ret == False:
            print('Return False')
            break

        cv2.imshow('video',frame)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('Close writeRecord')
            break
    
    cv2.destroyAllWindows()
    cap.release()
    out.release()

if __name__ == '__main__':
    select = int(input('select : '))
    if select == 1:
        showImg()
    elif select == 2:
        showVideo()
    elif select == 3:
        writeRecord()
