#import cv2 as cv
from cv2 import (VideoCapture, namedWindow, imshow, waitKey, destroyWindow, imwrite)

cam_port = 0

cam = VideoCapture(cam_port)

result, image = cam.read()

if result:
    imshow("Photo", image)
    imwrite("/home/coe-re/Photos/Photo.png", image)

    waitKey(0)
    destroyWindow("Photo")

else:
    print("Image not detected")

