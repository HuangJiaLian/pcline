#!/usr/bin/python2.7
# A QR decoder used the method of PCLines
# Python Version: 2.7
# Author: Huang Jie
# Email: jackhuang719668276@163.com

import cv2
import numpy as np 
import sys
import util

args_num = len(sys.argv)
if args_num < 2:
    print("Usage: %s imagefile" %sys.argv[0])
    sys.exit(1)

# img = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
img = util.img_read(sys.argv[1])

cv2.imshow("The original image",img)
cv2.waitKey()

