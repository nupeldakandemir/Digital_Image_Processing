import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

img=cv2.imread('x.jpg')
colors=('b','g','r') #bgr formatında okuyoruz

for i, color in enumerate(colors):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.title('Image Hıstogram RBG')
    plt.show()