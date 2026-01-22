#Gaussian filter for smoothing the image
import cv2 as cv

src = cv.imread("C:\\Users\\spadm\\OneDrive\\Desktop\\test.jpg")

img = cv.GaussianBlur(src,(5,5),10)

cv.imshow('Source image before Gaussian Filter', src)
cv.imshow('Source image after Gaussian Filter', img)
cv.waitKey(0)




