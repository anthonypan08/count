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

    cv2.imshow('window',image)
    if (np.sum(image) > 500):
        return [True, time.time()]
    else:
        return [False, time.time()]

def detectGray(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = tes.image_to_string(image, boxes = True)



start = False
while(True):
    start_time = 0
    printscreen_pil =  ImageGrab.grab(bbox = (958, 787, 1096, 932))
    printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))

    detectGray(printscreen_numpy)

    printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2RGB)
    cv2.imshow('window2',printscreen_numpy )




    if keyboard.is_pressed(' '):
        if start == False:
            start_time = time.time()
            start = True
            print (start_time)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
