"""
Code Explanation:

2D Convolution - Averaging -

As in one-dimensional signals, images also can be filtered with various low-pass filters(LPF), high-pass filters(HPF) etc. 
LPF helps in removing noises, blurring the images etc. HPF filters helps in finding edges in the images.

Behind the code, the function creates a 5x5 matrix where every element is 1/25. This ensures the sum of all elements in the kernel is 1, 
maintaining the image brightness.

This performs a 2D Convolution. The 5x5 kernel slides over the image. 
For every pixel, it takes the average of the 5x5 neighborhood (25 pixels) and replaces the center pixel with this average value.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('test.jpg')
 
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

# can use this function also  blur = cv2.blur(img,(5,5))

print("2D Convolution ( Image Filtering )")
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('2D Convolution - Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

"""
Weighted Mean (Gaussian-style) Kernel -

A weighted mean filter is a spatial filtering technique where pixels in a neighborhood are averaged, but unlike a standard "box" blur, 
some pixels are given more "influence" (weight) than others.

In most cases, the center pixel (the one being processed) is given the highest weight, and the weights decrease as you move further away 
toward the edges of the neighborhood.

"""

blur = cv2.GaussianBlur(img,(5,5),0)    #GaussianBlur function, kernel (5,5) with the best sigma calculated based on the kernel size
print("")
print("Gaussian Blurring")
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Gaussian Blurring')
plt.xticks([]), plt.yticks([])
plt.show()


