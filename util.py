import cv2
import numpy as np 
import sys

def img_read(filename):
    args_num = len(sys.argv)
    if args_num < 2:
        print("Usage: %s imagefile" %sys.argv[0])
        sys.exit(1)
    img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    return img 