import cv2
from cv2 import HOUGH_GRADIENT
import numpy as np
from matplotlib import pyplot as plt



def readImage():
    imgSrc = cv2.imread('coins.png')

    img = cv2.cvtColor(imgSrc, cv2.COLOR_RGB2GRAY)

    img = cv2.medianBlur(img,3)

    return img



def paramSweep(img):
    rows = img.shape[0]

    # Parametersweep to determine par1 and par2
    for i in range(200,400):
        par1 = int(i)
        for j in range (10,60):
            par2 = int(j)
            circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 16,param1=par1, param2=par2, minRadius=10, maxRadius=80)
            anzahl = circles.shape[1]
            print ("Circles: " + str(anzahl) + " Par1:" + str(par1) + " Par2:" + str(par2))

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break


def getCoins(img):
    cv2.namedWindow('image')
    rows = img.shape[0]
    
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, rows / 16,param1=250, param2=20, minRadius=10, maxRadius=80)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle outline
            radius = i[2]
            cv2.circle(img, center, radius, (255,0,125), 4)
    cv2.imshow('image',img)

    return ("The image shows " + str(circles.shape[1]) + " Coins!" ) 

image = readImage()
print (getCoins(image))


cv2.waitKey(0)
cv2.destroyAllWindows()
