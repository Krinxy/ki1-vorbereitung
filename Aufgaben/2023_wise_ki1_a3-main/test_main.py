import os
import cv2
import image_functions as src


# def test_execution():
#     ret = os.system('python3 main.py')
#     exitcode = os.WEXITSTATUS(ret)
#     print(exitcode)
#     assert(exitcode == 0)


def test_color_by_colorindex_100_red():
    img = cv2.imread('a_bar_somewhere.jpg')
    some_pixel_red_value = src.get_pixel_color_by_colorname(image=img, x=100, y=100, color="r")
    assert (some_pixel_red_value == 27)


def test_color_by_colorindex_40_30_red():
    img = cv2.imread('a_bar_somewhere.jpg')
    some_pixel_red_value = src.get_pixel_color_by_colorname(image=img, x=40, y=30, color="r")
    assert (some_pixel_red_value == 60)


def test_color_by_colorname_100_blue():
    img = cv2.imread('a_bar_somewhere.jpg')
    some_pixel_blue_value = src.get_pixel_color_by_colorindex(image=img, x=100, y=100, color_index=0)
    assert (some_pixel_blue_value == 27)


def test_color_by_colorname_40_30_blue():
    img = cv2.imread('a_bar_somewhere.jpg')
    some_pixel_blue_value = src.get_pixel_color_by_colorindex(image=img, x=40, y=30, color_index=0)
    assert (some_pixel_blue_value == 42)


def test_color_by_colorindex_20_30_green():
    img = cv2.imread('a_bar_somewhere.jpg')
    some_pixel_green_value = src.get_pixel_color_by_colorname(image=img, x=20, y=30, color="g")
    assert (some_pixel_green_value == 189)


def test_color_by_colorname_120_green():
    img = cv2.imread('a_bar_somewhere.jpg')
    some_pixel_green_value = src.get_pixel_color_by_colorindex(image=img, x=120, y=120, color_index=1)
    assert (some_pixel_green_value == 28)


def test_image_intensity():
    img = cv2.imread('a_bar_somewhere.jpg')
    max_int = src.get_highest_intensity(image=img)
    assert (max_int == 765)


def test_grayscale_intensity():
    img = cv2.imread('a_bar_somewhere.jpg')
    max_int1 = src.get_highest_intensity(image=img)
    gray = src.convert_grayscale(image=img)
    max_int2 = src.get_highest_intensity(image=gray)
    assert (max_int2 == max_int1)
