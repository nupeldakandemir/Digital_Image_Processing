import sys
import cv2

def main(src):
    ddepth = cv2.CV_16S
    kernel_size = 3
    window_name = "Laplace Filter Demo"

    src = cv2.GaussianBlur(src, (3, 3), 0)

    # Check if the image is grayscale before converting
    if len(src.shape) == 3:  # If the image has 3 channels, it is not grayscale
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    else:
        src_gray = src

    dst = cv2.Laplacian(src_gray, ddepth, ksize=kernel_size)
    abs_dst = cv2.convertScaleAbs(dst)

    cv2.imwrite('abstlaplace.jpg', abs_dst)
    cv2.imwrite('dstlaplace.jpg', dst)
img = cv2.imread('hann.jpg', cv2.IMREAD_GRAYSCALE)
main(img)