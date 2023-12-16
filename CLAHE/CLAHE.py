import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../x.jpg', 0)  # Read the image in grayscale
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl_img = clahe.apply(img)

# Visualize the images and their histograms
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

plt.subplot(122)
plt.title('CLAHE Applied Image')
plt.imshow(cl_img, cmap='gray')

plt.show()
