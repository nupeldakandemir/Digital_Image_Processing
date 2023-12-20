import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('tkagg')

img = cv.imread('hann.jpg')  # Görüntü

kernel = np.ones((5, 5), np.float32) / 25  # Maske

dst = cv.filter2D(img, -1, kernel)  # Filtre

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])  # Ekseni kapat
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])  # Ekseni kapat
plt.show()