import numpy as np
import cv2


def edge_detection(image):
    dummy_value = float(image[0][0])
    dummy_array = np.zeros((10, 5))
    # Performs edge detection on the image in horizontal direction.
    # TODO: implement edge detection
    # NOTE: you may look at the relevant parts of the script in the ./doc subfolder!
    # NOTE: You may implement the simplest applicable algorithm for horizontal edge detection!
    edges = np.zeros_like(image)
    sobel = ([-1, 0, 1])

    for i in range(image.shape[0]):
        for j in range(1, image.shape[1] - 1):
            a = image[i, j - 1] * sobel[0]
            b = image[i, j] * sobel[1]
            c = image[i, j + 1] * sobel[2]

            edges[i, j] = np.abs(a + b + c)


    # NOTE: Coding a working edge detection is most important here,
    # but we also want to consider an edge with -200 the same as an edge with +200
    return edges


def blue_edges(image, edges: np.ndarray):
    image_size_y = image.shape[0]
    image_size_x = image.shape[1]
    # TODO: Overwrites the values of image in the blue color channel by the values in edges.
    # All other color channels of the image are set to zero.
    image[:, :, 0] = edges
    image[:, :, 1] = 0
    image[:, :, 2] = 0



    return image


def save_final_image(image):
    filename = 'hopefully_blue_edges.png'
    # TODO: Use opencv to save the image
    img = image.copy()
    cv2.imwrite(filename=filename, img=img)



def edge_detection222(image):
    dummy_value = float(image[0][0])
    dummy_array = np.zeros((10, 5))
    # Performs edge detection on the image in horizontal direction.
    # TODO: implement edge detection
    # NOTE: you may look at the relevant parts of the script in the ./doc subfolder!
    # NOTE: You may implement the simplest applicable algorithm for horizontal edge detection!
    # NOTE: Coding a working edge detection is most important here,
    # but we also want to consider an edge with -200 the same as an edge with +200

    #2d Filter
    filtered_image = image.copy()
    stencil = [{-1, 0,1}, {-2, 0, 2}, {-1, 0, 1}]

    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            a = stencil[0][0] * image[i-j, j-i]
            b = stencil[0][1] * image[i, i-j]
            c = stencil[0][2] * image[i-i, j+i]
            d = stencil[1][0] * image[i, j-i]
            e = stencil[1][1] * image[i, j]
            f = stencil[1][2] * image[i, i+j]
            g = stencil[2][0] * image[i+j, j-i]
            h = stencil[2][1] * image[i+i, j]
            k = stencil[2][2] * image[i+i, j+j]

            filtered_image[i,j] = np.abs(a+b+c+d+e+f+g+h+k)

    image_path = 'edges_input.jpeg'

    edge_detection(image_path)

''' image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Führe die Kantenentdeckung mit dem Canny-Operator durch
    edges = cv2.Canny(image, 50, 150)  # Die Schwellenwerte können je nach Bild angepasst werden

    # Zeige das Originalbild und das Ergebnis der Kantenentdeckung an
    cv2.imshow('Originalbild', image)
    cv2.imshow('Kantenentdeckung mit Canny', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''

'''color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    sobelx = cv2.Sobel(color_image, cv2.CV_64F, 1, 0, ksize=5)
    sobelx = np.abs(sobelx)

    edges = np.uint8(255 * sobelx / np.max(sobelx))

    edges = edges[:, :, 0]

    return edges'''




def save_final_image2222(image):
    filename = 'hopefully_blue_edges.png'
    # TODO: Use opencv to save the image
    cv2.imwrite(filename, image)