<img width="725" height="517" alt="image" src="https://github.com/user-attachments/assets/4015461d-249b-41a5-88f9-ffe54440cf39" />

<img width="725" height="508" alt="image" src="https://github.com/user-attachments/assets/b04b666b-dc53-41db-b8a8-9e9b80607406" />

<img width="940" height="546" alt="image" src="https://github.com/user-attachments/assets/1daf7dd2-6a4a-4dda-bfe0-80bf2f9cc666" />

<img width="940" height="524" alt="image" src="https://github.com/user-attachments/assets/418b02b0-578b-4e17-b66c-b9514e857f98" />

<img width="940" height="561" alt="image" src="https://github.com/user-attachments/assets/148dc35b-e410-4633-b8f9-f0545c91cfd0" />

# 1. Computer-Vision---Affine Transformation
Affine Transformation OpenCV implementation

<img width="940" height="531" alt="image" src="https://github.com/user-attachments/assets/f38f3a02-55f9-4de7-aa3c-1dd997ed8ab8" />

<img width="940" height="978" alt="image" src="https://github.com/user-attachments/assets/86a973ee-769f-461e-b0e4-1af7c2eed097" />

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

# 2. Computer-Vision---Image Filtering

<img width="940" height="488" alt="image" src="https://github.com/user-attachments/assets/2d7b0a2c-3044-4502-80a5-049de5685a7c" />

<img width="940" height="483" alt="image" src="https://github.com/user-attachments/assets/16a18117-df2f-46a9-8678-585ff5ecdfe1" />

<img width="940" height="568" alt="image" src="https://github.com/user-attachments/assets/aca6ccd4-fb12-4d36-a0fd-48272f1868fb" />

<img width="940" height="477" alt="image" src="https://github.com/user-attachments/assets/582d40d9-58e2-4860-9beb-9b45b0d96a09" />

<img width="940" height="515" alt="image" src="https://github.com/user-attachments/assets/31f7d08d-1bf5-4e40-94f9-9945548e6821" />

<img width="940" height="511" alt="image" src="https://github.com/user-attachments/assets/ac7e79d8-0fea-44e8-818b-0b98a62c134f" />


# 3. Computer-Vision---Gaussian Filter

<img width="940" height="488" alt="image" src="https://github.com/user-attachments/assets/952d29f6-9e03-4e7d-aedd-0ac97a4b033a" />

<img width="940" height="511" alt="image" src="https://github.com/user-attachments/assets/c3db711d-16df-426d-948e-eb5a67ab046c" />

Filter types
1. Mean filter (box)
2. Weighted mean
3. Gaussian

<img width="940" height="497" alt="image" src="https://github.com/user-attachments/assets/7b56a838-193b-4be9-ae0c-c365b28979f7" />

# 4. Computer-Vision---Image compression using SVD math function
compressed_img = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vh[:k, :]))

<img width="596" height="401" alt="image" src="https://github.com/user-attachments/assets/059d6c48-d2a0-4303-a816-7456dd163e07" />

# 5. Computer-Vision---Edge Detection

<img width="940" height="484" alt="image" src="https://github.com/user-attachments/assets/fa3f0826-00a7-4268-b7f2-3a37d3b0b594" />

<img width="940" height="472" alt="image" src="https://github.com/user-attachments/assets/92ddc227-b7de-4381-88c8-a529a5783365" />

<img width="940" height="502" alt="image" src="https://github.com/user-attachments/assets/5bdf1b72-7083-4d7b-932b-7929d487da10" />

<img width="940" height="536" alt="image" src="https://github.com/user-attachments/assets/4474aeff-a234-4bf7-8db1-bd7ce5725832" />

<img width="940" height="485" alt="image" src="https://github.com/user-attachments/assets/3b0f4db7-d4ea-41b3-8d61-947b32f0a4d9" />

<img width="940" height="495" alt="image" src="https://github.com/user-attachments/assets/72bc3b0e-69f9-4088-a494-e72f431b9267" />

<img width="940" height="506" alt="image" src="https://github.com/user-attachments/assets/b8aa21b4-61c1-4d03-965d-8e20e7858491" />

<img width="940" height="471" alt="image" src="https://github.com/user-attachments/assets/773aacfa-3346-48d3-b4dc-3c962a39080c" />

<img width="940" height="456" alt="image" src="https://github.com/user-attachments/assets/b2ec1623-a383-47e0-bd5c-d256b1ab813d" />

<img width="940" height="503" alt="image" src="https://github.com/user-attachments/assets/51d7c629-41cf-4561-80d4-45012d1bdb08" />

<img width="940" height="532" alt="image" src="https://github.com/user-attachments/assets/a0686f90-7669-4fa4-b802-52124bfaab66" />

<img width="940" height="535" alt="image" src="https://github.com/user-attachments/assets/e7eb0472-c406-427a-a4d6-9499109377f1" />

<img width="940" height="524" alt="image" src="https://github.com/user-attachments/assets/863072f4-314d-465b-94c2-d45eb15d5637" />

<img width="940" height="491" alt="image" src="https://github.com/user-attachments/assets/b0063f57-01f4-45bc-bbf1-cc14edc49044" />

<img width="940" height="482" alt="image" src="https://github.com/user-attachments/assets/c1ccee73-4995-4468-a86e-164b06597fa9" />

<img width="9540" height="533" alt="image" src="https://github.com/user-attachments/assets/d7321d1f-fdbb-4a1a-8bf5-0a05bc6a62b2" />
