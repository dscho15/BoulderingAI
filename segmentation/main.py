import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def histogram():
    img = cv.imread('data_set/img1.jpg')

    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)


    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])

    plt.savefig('test_data/histogram_hsv.jpg')

def single_color():
    img = cv.imread('data_set/img1.jpg')
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Only show hue
    hue_channel = hsv_img[:,:,0]

    plt.plot(hue_channel, color='k')  # Use 'k' for black color

    plt.plot(hue_channel)

    plt.savefig('test_data/single_color.jpg')

def remove_pixels():
    img = cv.imread('data_set/img1.jpg')

    # Create a boolean mask for pixels above the threshold
    mask = (img[:, :, 0] > 50) & (img[:, :, 1] > 50) & (img[:, :, 2] > 50)

    # Set the masked pixels to [0, 0, 0]
    img[mask] = [255, 255, 255]

    cv.imwrite('test_data/remove_pixels.jpg', img)


remove_pixels()