import cv2
import matplotlib.pyplot as plt

img = cv2.imread('x.jpg', 0)  # Read the image in grayscale
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl_img = clahe.apply(img)

# Visualize the images and their histograms
plt.figure(figsize=(12, 12))

# Original Image
plt.subplot(221)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

# Histogram - Original Image
plt.subplot(222)
plt.title('Histogram - Original Image')
plt.hist(img.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

# CLAHE Applied Image
plt.subplot(223)
plt.title('CLAHE Applied Image')
plt.imshow(cl_img, cmap='gray')

# Histogram - CLAHE Applied Image
plt.subplot(224)
plt.title('Histogram - CLAHE Applied Image')
plt.hist(cl_img.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

plt.show()
