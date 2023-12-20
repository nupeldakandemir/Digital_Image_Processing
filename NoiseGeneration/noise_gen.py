import random
import cv2
import matplotlib
matplotlib.use('tkagg')

def add_noise(img):
    row,col=img.shape

    number_of_pixels = random.randint(500,10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0,row-1)
        x_coord= random.randint(0,col-1)
        img[y_coord][x_coord] = 255

    number_of_pixels=random.randint(500,10000)
    for i in range(number_of_pixels):
        y_coord=random.randint(0,row-1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 0

    return img

img = cv2.imread('y.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imwrite('salt_and_pepper_image.jpg',add_noise(img))

