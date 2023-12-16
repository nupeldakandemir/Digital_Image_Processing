import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

image=cv2.imread("x.jpg",cv2.IMREAD_GRAYSCALE)
hist=cv2.calcHist([image],[0],None,[256],[0,256])

plt.plot(hist)
plt.title('Image histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

