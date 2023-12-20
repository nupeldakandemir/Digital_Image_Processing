import cv2
import numpy as np

def add_noise(image, noise_type='gaussian', intensity=50):
    """
    image: Giriş görüntü
    noise_type: 'gaussian' veya 'salt-and-pepper'
    intensity: Gürültü yoğunluğu
    """
    if noise_type == 'gaussian':
        row, col, ch = image.shape
        mean = 0
        var = intensity
        sigma = var**0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        noisy = np.clip(image + gauss, 0, 255)
        return noisy.astype(np.uint8)
    elif noise_type == 'salt-and-pepper':
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = intensity / 100.0
        noisy = np.copy(image)

        # Salt noise
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        noisy[coords] = 1

        # Pepper noise
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        noisy[coords] = 0

        return noisy.astype(np.uint8)

# Örnek kullanım
image_path = 'hann.jpg'
original_image = cv2.imread('hann.jpg')

# Gaussian gürültü ekleme
noisy_image_gaussian = add_noise(original_image, noise_type='gaussian', intensity=500)

# Salt-and-pepper gürültü ekleme
noisy_image_sp = add_noise(original_image, noise_type='salt-and-pepper', intensity=50)

# Görüntüleri gösterme
cv2.imshow('Original Image', original_image)
cv2.imshow('Noisy Image (Gaussian)', noisy_image_gaussian)
cv2.imshow('Noisy Image (Salt-and-Pepper)', noisy_image_sp)
cv2.waitKey(0)
cv2.destroyAllWindows()
