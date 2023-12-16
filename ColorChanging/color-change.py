import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

# Resmi oku ve renk uzayını değiştir
img = cv2.imread("x.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Resmi gri tonlamaya çevir
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Orijinal renkli resmi görselleştir
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Gri tonlamalı resmi görselleştir
plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap='gray')  # cmap='gray' gri tonlamalı görüntüyü doğru renkte görüntülemek için kullanılır
plt.title('Grayscale Image')
plt.axis('off')

# Pencereleri göster
plt.show()

# Bekleme işlemi (Kullanıcı bir tuşa basana kadar bekler)
plt.waitforbuttonpress()