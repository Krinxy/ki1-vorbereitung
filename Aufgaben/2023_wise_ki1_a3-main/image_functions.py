from copy import copy
import numpy as np


def count_pixels_with_color(image, color):
    x_size = image.shape[0]
    y_size = image.shape[1]
    count = 0
    blue = color[0]
    green = color[1]
    red = color[2]

    for i in range(x_size):
        for j in range(y_size):
            if image[i][j][0] == blue and image[i][j][1] == green and image[i][j][2] == red:
                count += 1

    return count


def convert_img(image):
    factor = 32
    big_img = np.zeros((image.shape[0] * factor, image.shape[1] * factor, 3), np.uint8)
    for i in range(image.shape[0] * factor):
        for j in range(image.shape[1] * factor):
            big_img[i][j] = image[i // factor][j // factor]
    return big_img


def get_pixel_color_by_colorindex(image, x: int, y: int, color_index: int):
    # Check if the requested color is in the defined "color range" [0,1,2] for [blue, green, red]
    if color_index > 2 or color_index < 0:
        return None

    x_size = image.shape[0]
    y_size = image.shape[1]
    # Check if the requested pixel is within the image
    if x > x_size or x < 0:
        return None
    if y > y_size or y < 0:
        return None

    return image[x, y, color_index]
    # For the pixel at location [x][y], you have a list/array of three values.
    # TODO: return the value of the requested color for the pixel (optimal: add one line of code here with return)


def get_pixel_color_by_colorname(image, x: int, y: int, color: str = "r"):
    color = color.lower()
    img = image[x, y]
    if color == "b":
        color_index = 0
        b, _, _ = img
        return b
    
    elif color == "g":
        color_index = 1
        _, g, _ = img
        return g
    elif color == "r":
        color_index = 2
        _, _, r = img
        return r
    else:
        return None

    # For the pixel at location [x][y], you have a list/array of three values.
    # TODO: return the value of the requested color for the pixel (optimal: add one line of code here with return)
    # Hint: you may use other functions


def get_highest_intensity(image):
    # This function checks all pixels in the image, sums over the three color channels and finds the maximum.
    # You do not need to edit this function. It is here as an example how you can operate on the image
    highest_intensity = 0.0
    x_size = image.shape[0]
    y_size = image.shape[1]
    for i in range(x_size):
        for j in range(y_size):
            pixel_rgb_colors = image[i][j]
            intensity = sum(pixel_rgb_colors)
            if intensity > highest_intensity:
                highest_intensity = intensity
    return highest_intensity


def convert_grayscale(image):
    gray = copy(image)  # copy the image to not change the original image

    # Convert the image from color to grayscale.
    # When using displaying a grayscale image, we only need one value for each pixel to represent the brightness
    x_size = image.shape[0]
    y_size = image.shape[1]
    # TODO: Implement the conversion from color to grayscale
    # Hint: look at get_highest_intensity function
    for i in range(x_size):
        for j in range(y_size):
            grayscale = (sum(image[i, j]) / 3)
            gray[i, j] = grayscale
    return gray
