import cv2
from image_functions import get_pixel_color_by_colorindex, get_highest_intensity, get_pixel_color_by_colorname, convert_grayscale, convert_img, count_pixels_with_color


# Hinweis: Falls bei   pip install -r requirements.txt   mit opencv etwas schief läuft,
# einfach eine andere Version mit   pip install opencv-python   installieren

# Aufgabe 1
# Read RGB image
img = cv2.imread('yellow_mouse.png')

# Output image (convert_img is a helper function to make the image bigger)
cv2.imshow('RGB Image', convert_img(img))
# Maintain all windows untill a key is pressed
cv2.waitKey(0)
# Destroying present windows on screen
cv2.destroyAllWindows()

# TODO: print the shape of the image and describe each dimension (what does each dimension represent?)
print(img.shape[0])     # X-Dimension; Zeile von oben nach unten
print(img.shape[1])     # Y-Dimension; Zeile von links nach rechts

# TODO: add code to print the BGR values of the pixel at (0, 1), and check if the result is correct by looking at the picture
print(img[0][1])        # Pixel ist schwarz; BGR ist dementsprechend 0 0 0 
print(img[0, 1])

# TODO: check the red value of the pixel at (4, 3) and compare with the picture
print(img[4][3])        # Einziger roter Pixel
print(img[4, 3])

# TODO: change the pikachus cheek to green (red pixel to green pixel)
img[4][3] = (0, 255,0)
cv2.imshow('Red to Green', convert_img(img))
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: try to understand the function count_pixels_with_color and write adequate comments
print("Anzahl der Pixel mit Farbe (232,162,0): ", count_pixels_with_color(image=img, color=(232, 162, 0)))
# So oft ist ein Pixel mit der Farbe (232, 162, 0) im Bild vorgekommen

# TODO: Discuss your results in groups of 2-4 students

# Aufgabe 2
# Read new RGB image
img2 = cv2.imread('a_bar_somewhere.jpg')

# TODO: print the shape of the image and describe each dimension (what does each dimension represent?)
print(img2.shape[0])
print(img2.shape[1])

# TODO: implement the functions (get_pixel_color_by_colorindex and get_pixel_color_by_colorname) in image_functions.py
some_pixel_red_value = get_pixel_color_by_colorname(image=img2, x=0, y=0, color="r")
print("Rotwert", some_pixel_red_value)
some_pixel_blue_value = get_pixel_color_by_colorindex(image=img2, x=0, y=0, color_index=0)
print("Blauwert", some_pixel_blue_value)
some_pixel_blue_value = get_pixel_color_by_colorname(image=img2, x=0, y=0, color="g")
print("Grünwert", get_pixel_color_by_colorname)

# TODO: ZUSATZ für Aufgabe 1: change all yellow pixels to orange pixels (first check the color of the yellow and orange pixels)

print("Höchster Wert über alle Farbkanäle aufsummiert: ", get_highest_intensity(image=img2))

# Output image
cv2.imshow('RGB Image', img2)

# convert rgb image to grayscale ("Schwarz-Weiß") using the opencv library function
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)

# convert rgb image to grayscale using own implementation
# TODO: implement the function convert_grayscale in image_functions.py
gray2 = convert_grayscale(image=img2)
cv2.imshow('Grayscale own implementation ', gray2)

print("Close the Windows by pressing any key")
# Maintain all windows untill a key is pressed
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()
