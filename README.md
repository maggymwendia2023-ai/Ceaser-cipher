# Caesar Cipher

A Python program that encrypts and decrypts text using the Caesar cipher,
a substitution cipher that shifts each letter by a fixed number of places.

## Features
- Encrypt a message with a chosen shift
- Decrypt a message with the same shift
- Keeps spaces, numbers, and punctuation unchanged

## How to run
python caesar.py

## Example
Input:  Hello, World!
Shift:  3
Output: Khoor, Zruog!

## How it works
Each letter moves forward in the alphabet by the shift value.
With a shift of 3, A becomes D, B becomes E, and Z wraps around to C.
Decryption shifts backward by the same amount.

## Security note
The Caesar cipher is not secure. With only 25 possible shifts,
it can be broken by trying every one (brute force). It's for learning
only.

## Author
Margaret 
