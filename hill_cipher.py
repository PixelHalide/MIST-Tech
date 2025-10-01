import sys
import numpy as np
import math

def encrypt():
    text = input("Input text: ")
    key = input("Input Key: ")

    text = text.upper()
    key = key.upper()

    n = int(math.sqrt(len(key)))
    if n * n != len(key):
        print("Key length must be a perfect square")
        sys.exit()

    if len(text) % n != 0:
        print("Text length must be a multiple of", n)
        sys.exit()

    text_arr = np.array([ord(i) - ord('A') for i in text])

    key_arr = np.array([ord(i) - ord('A') for i in key]).reshape(n, n)

    result = np.dot(key_arr, text_arr)

    result = result % 26

    for i in result:
        print(chr(i + ord('A')), end="")
    print()

def decrypt():
    cipher = input("Input Cipher: ")
    key = input("Input key: ")
    n = len(cipher)

    if len(key) != n*n:
        print("Key length must be a perfect square")
        sys.exit()

    arr = np.array([ord(i) - ord('A') for i in cipher])
    key_arr = np.array([ord(i) - ord('A') for i in key]).reshape(n, n)

    if np.linalg.det(key_arr) == 0:
        print("Invalid matrix")
        sys.exit()

    key_arr = np.linalg.inv(key_arr)
    key_arr = key_arr % 26

    result = np.dot(key_arr,arr)
    result = result % 26

    for i in result:
        print(chr(int(i) + ord('A')), end="")
    print()

while True:
    print("What would you like to do?")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force")
    print("4. Exit")
    inp = int(input("Enter selection: "))

    match inp:
        case 1:
            encrypt()
        case 2:
            decrypt()
            # NOT COMPLETE
        case 3:
            pass
        case 4:
            sys.exit()
