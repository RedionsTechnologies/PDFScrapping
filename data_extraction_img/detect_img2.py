"""
sequencial script for detecting data on pdf
"""
# reading png file using PILLOW library
# cause cv2 library failing to load some png files
# then we will convert it into cv2 image
import os
cdir = os.path.join(os.getcwd(), 'tst_papper')

from PIL import Image
import numpy as np
pil_image = Image.open(os.path.join(cdir, "g.png")).convert("RGB")

img_cv = np.array(pil_image)
img_cv = img_cv[:, :, ::-1].copy()          # Convert RGB to BGR

import cv2
image = cv2.imread(os.path.join(cdir, "2.png"))

result = cv2.matchTemplate(image, img_cv, cv2.TM_CCOEFF_NORMED)
sin_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(cv2.minMaxLoc(result))
top_left = max_loc
bottom_right = (top_left[0]+pil_image.size[0], top_left[1]+pil_image.size[1])
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 5)

cv2.imshow('object found', image)
cv2.waitKey(20)
