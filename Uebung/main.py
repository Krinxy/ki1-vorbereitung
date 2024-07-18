import numpy as np
import cv2


image = cv2.imread('wolf.webp')
image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow('Leonardo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

gray = grayscale(image)
cv2.imshow('Grau', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

def sobel_edge1D(image):
    edges = np.zeros_like(image, dtype=np.float32)
    sobel = ([-1, 0, 1])
    
    for i in range(image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            a = sobel[0] * image[i, j-1]
            b = sobel[1] * image[i, j]
            c = sobel[2] * image[i, j+1]
        
            edges[i, j] = np.abs(a + b + c)

    return edges

sobeln = sobel_edge1D(gray)
cv2.imshow('Sobel', sobeln)
cv2.waitKey(0)
cv2.destroyAllWindows()

def sobel_edge2D(image):
    edges = np.zeros_like(image)
    sobel = [[-1, 0, 1], [-2, 0 , 2], [-1, 0, 1]]

    for i in range(image.shape[0] - 1):
        for j in range(image.shape[1] -1):
            a = sobel[0][0] * image[i-1, j-1]
            b = sobel[0][1] * image[i-1, j]
            c = sobel[0][2] * image[i-1, j+1]
            d = sobel[1][0] * image[i, j-1]
            e = sobel[1][1] * image[i, j]
            f = sobel[1][2] * image[i, j+1]
            g = sobel[2][0] * image[i+1, j-1]
            h = sobel[2][1] * image[i+1, j]
            k = sobel[2][2] * image[i+1, j+1]

            edges[i, j] = np.abs(a + b + c + d + e + f + g + h + k)
    
    return edges

sobeln2d = sobel_edge2D(gray)
cv2.imshow('Sobel2D', sobeln2d)
cv2.waitKey(0)
cv2.destroyAllWindows()

def blue_edges(image, edges):
    image[:,:,0] = edges
    image[:,:,1] = 0
    image[:,:,2] = 0

    return image

blau= blue_edges(image, sobeln2d)
cv2.imshow('Blaue Kanten', blau)
cv2.waitKey(0)
cv2.destroyAllWindows()
