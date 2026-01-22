# 1. Computer-Vision---Affine Transformation
Affine Transformation OpenCV implementation

Code to perform these operations:
(1) Get the input image.
(2) Decrease its size by half
(3) Rotate 30 degrees
(4) Translate 5 pixels towards the left and to the bottom
(5) Save the result.

What is an Affine Transformation?
A transformation that can be expressed in the form of a matrix multiplication (linear transformation) followed by a vector addition (translation).

From the above, we can use an Affine Transformation to express:
1. Rotations (linear transformation)
2. Translations (vector addition)
3. Scale operations (linear transformation)

you can see that, in essence, an Affine Transformation represents a relation between two images.

# 2. Computer-Vision---Gaussian Filter
Filter types
1. Mean filter (box)
2. Weighted mean
3. Gaussian

<img width="701" height="369" alt="image" src="https://github.com/user-attachments/assets/1807597a-bf1e-4b09-b572-f9cedde72ef0" />

# 3. Computer-Vision---Image compression using SVD math function
U, S, Vh = np.linalg.svd(src, full_matrices=False)
k = 25
compressed_img = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vh[:k, :]))
<img width="596" height="401" alt="image" src="https://github.com/user-attachments/assets/059d6c48-d2a0-4303-a816-7456dd163e07" />
