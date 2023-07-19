import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def histogram(image):

    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    color = ('b', 'g', 'r')
    
    for i, col in enumerate(color):
        histr = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])

def single_color(image):
    
    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Only show hue
    hue_channel = hsv_img[:,:,0]

    plt.plot(hue_channel, color='k')  # Use 'k' for black color
    plt.plot(hue_channel)

def remove_pixels(image):

    # Create a boolean mask for pixels above the threshold
    mask = (image[:, :, 0] > 50) & (image[:, :, 1] > 50) & (image[:, :, 2] > 50)

    # Set the masked pixels to [0, 0, 0]
    image[mask] = [255, 255, 255]
    plt.imshow(image)

if __name__ == "__main__":
    
    image = cv.imread('data_set/356777545_765326948673161_153020440471471569_n.jpg')
    remove_pixels(image)
    plt.show()