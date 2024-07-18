def get_pixel_color_by_colorindex(image, x: int, y: int, color_index: int):
    if color_index > 2 or color_index < 0:
        return None

    x_size = image.shape[0]
    y_size = image.shape[1]
    if x > x_size or x < 0:
        return None
    if y > y_size or y < 0:
        return None
    # For the pixel at location x and y, you have a list/array of three values.
    # return the value of the requested color for the pixel
    return image[x][y][color_index]


def get_pixel_color_by_colorname(image, x: int, y: int, color: str = "r"):
    color = color.lower()
    if color == "b":
        color_index = 0
    elif color == "g":
        color_index = 1
    elif color == "r":
        color_index = 2
    else:
        return None
    # For the pixel at location x and y, you have a list/array of three values.
    # return the value of the requested color for the pixel
    return get_pixel_color_by_colorindex(image=image, x=x, y=y, color_index=color_index)
