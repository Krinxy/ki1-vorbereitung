# You do not need to modify this file!
# Diese Datei muss nicht geändert werden!

import cv2


def read_image_in_color_and_bw():
    image = cv2.imread('edges_input.jpeg')
    assert (image is not None)
    return image, cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
