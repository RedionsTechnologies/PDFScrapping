"""
Currently this code detects only one image inside image.

THIS CODE NEEDS TO BE RUN LINE BY LINE, LIKE JUPYTER NOTEBOOK
"""
import os
import cv2
import numpy as np

cdir = os.path.join(os.getcwd(), 'data_extraction_img')

# Load input image and convert it into gray
img1 = os.path.join(cdir, '4.png')
image = cv2.imread(img1)
# cv2.imshow('page', image)         # to view image file
# cv2.waitKey(0)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)         # convert to grey scale

# Load the template image
template = cv2.imread(os.path.join(cdir, '1.jpg'))
# tg = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
sin_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# create bounding box
top_left = max_loc
# increasing the size of bounding rectangle by 50 pixels
bottom_right = (top_left[0]+10, top_left[1]+10)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 5)

cv2.imshow('object found', image)
cv2.waitKey(0)
cv2.destroyAllWindows()