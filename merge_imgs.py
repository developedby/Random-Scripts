"""Script that merges all the images in a given folder
Will fail if the images don't have the same shape
Author: Nicolas Abril
"""

import os
import numpy as np
import cv2

FOLDER = ''
VERBOSE = True
OUT_FILE = 'merge.bmp'

imgs = []
files = os.listdir(FOLDER)
if VERBOSE:
    for filename in files:
        print(filename)

if OUT_FILE in files:
    print(f"The output image {OUT_FILE} already exists! Exiting for safety")
    exit()

for filename in os.listdir(FOLDER):
    if os.path.isfile(FOLDER+filename):
        img = cv2.imread(FOLDER+filename, 0).astype(np.float)
        if img is not None:
            imgs.append(img)
merge = np.rint(sum(imgs) / len(imgs)).astype(np.uint8)
cv2.imwrite(FOLDER+OUT_FILE, merge)
