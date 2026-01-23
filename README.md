<img width="769" height="378" alt="image" src="https://github.com/user-attachments/assets/cff63efe-b876-4614-82f6-d792b26ded2c" />

<img width="671" height="394" alt="image" src="https://github.com/user-attachments/assets/33a00eeb-f8aa-4911-a06d-4c788ddbf604" />

<img width="730" height="397" alt="image" src="https://github.com/user-attachments/assets/2f9fd477-3f62-434d-96e6-b801d0059e4f" />

<img width="688" height="413" alt="image" src="https://github.com/user-attachments/assets/9ee4bcff-5724-4d85-8b9d-c5fa66a4e4ef" />

# 1. Computer-Vision---Affine Transformation
Affine Transformation OpenCV implementation

<img width="739" height="417" alt="image" src="https://github.com/user-attachments/assets/5197fb77-3379-4798-91ec-9ef5a0103cf6" />

<img width="422" height="438" alt="image" src="https://github.com/user-attachments/assets/34452f1c-8b56-40b4-aa5c-3d817e0f991e" />

<img width="659" height="356" alt="image" src="https://github.com/user-attachments/assets/89b92297-d4e0-4c5a-8188-f276a289b748" />

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

<img width="635" height="378" alt="image" src="https://github.com/user-attachments/assets/91d86fbd-60d6-45be-b944-7c5fa1d8264c" />

<img width="709" height="350" alt="image" src="https://github.com/user-attachments/assets/f343cccc-b934-43a9-a2b8-556156cacfe0" />

Filter types
1. Mean filter (box)
2. Weighted mean
3. Gaussian

<img width="701" height="369" alt="image" src="https://github.com/user-attachments/assets/1807597a-bf1e-4b09-b572-f9cedde72ef0" />

# 3. Computer-Vision---Image compression using SVD math function
compressed_img = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vh[:k, :]))

<img width="596" height="401" alt="image" src="https://github.com/user-attachments/assets/059d6c48-d2a0-4303-a816-7456dd163e07" />



