import cv2
from cv2 import HOUGH_GRADIENT
import numpy as np
from matplotlib import pyplot as plt

sct_img = cv2.imread('coins.png')

def nothing(x):
    pass


H = 103
S = 255
V = 255
Hl = 0
Sl = 191
Vl = 119



while True:


    hsv = cv2.cvtColor(sct_img, cv2.COLOR_RGB2HSV)

    cv2.imshow('image',hsv)

    lower_blue = np.array([Hl,Sl,Vl])
    upper_blue = np.array([H,S,V])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
  


    # Find the circle blobs on the binary mask:
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Use a list to store the center and radius of the target circles:
    detectedCircles = []
    
    for i, c in enumerate(contours):

        # Approximate the contour to a circle:
        (x, y), radius = cv2.minEnclosingCircle(c)

        # Compute the center and radius:
        center = (int(x), int(y))
        radius = int(radius)


        if radius > 20 and radius < 40:
            # Draw the circles:
            cv2.circle(sct_img, center, radius, (0, 0, 255), 2)
            cv2.rectangle(sct_img, (center[0] - 5, center[1] - 5), (center[0] + 5, center[1] + 5), (0, 128, 255), -1)

            # Store the center and radius:
            
            detectedCircles.append([center, radius])
