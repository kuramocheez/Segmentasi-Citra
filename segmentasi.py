from skimage import data
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('img/thomas.jpg')
gray_img = rgb2gray(img)

plt.figure(figsize=(15, 15))

binarized_gray = (gray_img > 6*0.1)*1
plt.subplot(5,2,6+1)

plt.title("Threshold: >"+str(round(6*0.1,1)))

plt.imshow(binarized_gray, cmap = 'gray')

plt.tight_layout()
