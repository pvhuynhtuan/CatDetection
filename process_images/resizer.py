## Bulk image resizer

# This script simply resizes all the images in a folder to one-eigth their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: place this script in a folder of images you want to shrink,
# and then run it.

import numpy as np
import cv2
import os

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".jpg"):
        image = cv2.imread(filename)
	width, height = image.shape[:2]
	if (width>960) or (height>960):
		print filename
		if width > height :
			fxx = 960.0/width
			print fxx
        		resized = cv2.resize(image,None,fx=fxx, fy=fxx, interpolation=cv2.INTER_CUBIC)
		else :
			fyy = 960.0/height
			print fyy
                        resized = cv2.resize(image,None,fx=fyy, fy=fyy, interpolation=cv2.INTER_CUBIC)
        	cv2.imwrite(filename,resized)
