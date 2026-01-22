#Image compression using SVD
import cv2 as cv
import numpy as np

src1 = cv.imread("C:\\Users\\spadm\\OneDrive\\Desktop\\test.jpg")
print(src1.shape)
src = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)

U, S, Vh = np.linalg.svd(src, full_matrices=False)
k = 25
compressed_img = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vh[:k, :]))
compressed_img = np.uint8(np.clip(compressed_img, 0, 255))

cv.imshow('Original', src)
cv.imshow('Compressed (k=50)', compressed_img)
cv.waitKey(0)
cv.destroyAllWindows()


