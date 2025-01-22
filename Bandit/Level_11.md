# Level 11

The password for the next level is stored in the file data.txt, which contains base64 encoded data

Since the file contains Base64 data, i look at the manpage for base64. there's a simple -d flag to decode files. i do **base64 -d data.txt** and we get the password in plaintext.