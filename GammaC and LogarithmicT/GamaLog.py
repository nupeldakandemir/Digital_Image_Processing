import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

img = cv2.imread('x.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gamma correction
gam = 1.6
img_2 = np.power(img, gam)

# Apply log transformation method
c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1e-5))  # Add a small constant to avoid divide by zero

# Visualize the images and their histograms
plt.figure(figsize=(15, 8))

# Original Image
plt.subplot(231)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.subplot(234)
plt.title('Histogram - Original Image')
plt.hist(img.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

# Gamma Corrected Image
plt.subplot(232)
plt.title('Gamma Corrected Image')
plt.imshow(img_2, cmap='gray')
plt.subplot(235)
plt.title('Histogram - Gamma Corrected Image')
plt.hist(img_2.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

# Log Transformed Image
plt.subplot(233)
plt.title('Log Transformed Image')
plt.imshow(log_image, cmap='gray')
plt.subplot(236)
plt.title('Histogram - Log Transformed Image')
plt.hist(log_image.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

plt.show()
