import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

# Read image and change color space
img = cv2.imread("x.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Visualize original color image
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Visualize grayscale image
plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap='gray')  # cmap='gray' used to display a grayscale image in correct color
plt.title('Grayscale Image')
plt.axis('off')

# show windows
plt.show()

# Waiting process (Waits until the user presses a key)
plt.waitforbuttonpress()
