from __future__ import print_function
import cv2 as cv
import numpy as np

src = cv.imread('C:\\Users\\spadm\\OneDrive\\Desktop\\test.png')

# Decrease the size of image by half

srcTri = np.array( [[0, 0], [src.shape[1] - 1, 0], [0, src.shape[0] - 1]] ).astype(np.float32)                #src.shape[1] specifically refers to the Width of the image.
dstTri = np.array( [[0, 0], [(src.shape[1] - 1)*0.5, 0], [0, (src.shape[0] - 1)*0.5]] ).astype(np.float32)

warp_mat = cv.getAffineTransform(srcTri, dstTri)

warp_dst = cv.warpAffine(src, warp_mat, (src.shape[1], src.shape[0]))

# Rotating the image after Warp
 
center = (warp_dst.shape[1]//2, warp_dst.shape[0]//2)
angle = 30
scale = 1
 
rot_mat = cv.getRotationMatrix2D( center, angle, scale )

warp_rotate_dst = cv.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))

# Moving the image 5 pixels to left & bottom

srcTri2 = np.array( [[0, 0], [src.shape[1] - 1, 0], [0, src.shape[0] - 1]] ).astype(np.float32)                
dstTri2 = np.array( [[0+5, 0+5], [(src.shape[1]*0.5)+5, 0+5], [0+5, ((src.shape[0] - 1)*0.5)+5]] ).astype(np.float32)

warp_mat2 = cv.getAffineTransform(srcTri2, dstTri2)

warp_dst2 = cv.warpAffine(src, warp_mat2, (src.shape[1], src.shape[0]))

cv.imshow('Source image', src)
cv.imshow('Warp', warp_dst)
cv.imshow('Warp + Rotate', warp_rotate_dst)
cv.imshow('Warp - 5pixels left & bottom', warp_dst2)
cv.waitKey()
