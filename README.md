# Hill_Cipher_Project

This code is a Python implementation of the Hill cipher, which is a classical symmetric encryption technique based on linear algebra. The Hill cipher operates on blocks of characters, where each block is represented as a vector and multiplied by a key matrix to produce the ciphertext vector. To decrypt, the ciphertext vector is multiplied by the inverse of the key matrix.

Let's go through the code step by step:

1. The code defines several functions for various operations required in the Hill cipher:

- `getDetA(A,dim)`: This function calculates the determinant of a square matrix `A` of dimension `dim`. It specifically handles cases for 2x2 and 3x3 matrices.

- `getAdjA(A,dim)`: This function calculates the adjugate (also known as the adjoint) of a square matrix `A` of dimension `dim`. It is used to find the inverse of the matrix.

- `getTransposeA(A,dim)`: This function calculates the transpose of a square matrix `A` of dimension `dim`.

- `modInverse(a, m)`: This function calculates the modular multiplicative inverse of `a` modulo `m`. It is used to find the inverse of the determinant.

- `mod(a, b)`: This function computes the modulo operation, handling negative numbers correctly.

- `getAinv(A,dim)`: This function calculates the inverse of the key matrix `A` of dimension `dim` using the determinant and adjugate.

- `multiply_matrix_vec_encrypt(A, vec, dim)`: This function multiplies the key matrix `A` with a vector `vec` for encryption purposes.

- `multiply_matrix_vec_decrypt(A, vec, dim)`: This function multiplies the inverse of the key matrix `A` with a vector `vec` for decryption purposes.

- `encryption(msg, A, dim)`: This function takes a plaintext `msg`, pads it if needed to form complete blocks, and encrypts it using the Hill cipher.

- `decryption(A, dim, cipher_list)`: This function takes a list of ciphertext blocks `cipher_list` and decrypts them using the Hill cipher.

2. The code then prompts the user to enter the dimension and values of the key matrix `A`. It checks if the determinant is invertible and handles cases where it is not.

3. The user is asked to choose between encryption and decryption based on their input.

- If the user selects encryption, they are asked to input the plaintext message, and the code encrypts it using the Hill cipher with the provided key matrix `A`. The ciphertext is then displayed.

- If the user selects decryption, they are asked to input the ciphertext message, and the code decrypts it using the Hill cipher with the provided key matrix `A`. The plaintext is then displayed.

Note: The Hill cipher requires the key matrix to have an inverse, and the dimension of the key matrix should be either 2x2 or 3x3. Also, the plaintext and ciphertext are assumed to consist of uppercase alphabetic characters (A-Z). Any additional characters or spaces in the input will be ignored or padded as required to form complete blocks.
