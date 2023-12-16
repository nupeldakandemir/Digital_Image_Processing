import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.use('tkagg')

img=cv2.imread('x.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ=cv2.equalizeHist(img)
hist=cv2.calcHist([equ],[0],None,[256],[0,256])

plt.plot(hist)
plt.title('Equalized Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()


cv2.imwrite("eqfile.jpeg",equ)
