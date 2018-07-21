import cv2;
import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
import time
import keyboard
import pytesseract as tes

print(pyautogui.position())
def detectGreen(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    lower = np.array([0,205,0])
    upper = np.array([200,255,200])
    mask = image

    mask = cv2.inRange(image, lower, upper)
    image = cv2.bitwise_and(image, image, mask = mask)
    #image = cv2.bitwise_and(image, image, mask = mask2)
    #image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)

    cv2.imshow('windowGreen',image)
    if (np.sum(image) > 500):
        return ["Green", time.time()]


def detectNone(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([100,30,150])
    upper = np.array([170,90,250])
    mask = image
    image = cv2.medianBlur(image, 5)

    mask = cv2.inRange(image, lower, upper)
    image = cv2.bitwise_and(image, image, mask = mask)
    #image = cv2.bitwise_and(image, image, mask = mask2)
    image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)




    cv2.imshow('windowNone',image)
    image = image * 2


    if (np.sum(image) > 5000):
        return ["None", time.time()]


start = False
time_log = []
temp = []
while(True):
    start_time = 0
    printscreen_pil =  ImageGrab.grab(bbox = (860,818,1052,993))
    printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

    temp = detectGreen(printscreen_numpy)
    if not temp:
        temp = detectNone(printscreen_numpy)
    if not temp:
        time_log.append(["Activated", time.time()])
    else:
        time_log.append(temp)

    print (time_log[len(time_log) - 1])
    printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2RGB)
    cv2.imshow('window2',printscreen_numpy )

    """
    roi = printscreen_numpy[70:120, 10:50]
    cv2.imshow('roi',roi )

    # convert it into HSV
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    print (hsv)
    """


    if keyboard.is_pressed(' '):
        if start == False:
            start_time = time.time()
            start = True
            print (start_time)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
