# Secret of the Polyglot

## Challenge

The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file? Download the suspicious file

## Solution

We are greeted with a PDF file which seems to contain the 2nd half of the flag. I press CTRL-A to see if there is any hidden white text, but there isn't. I see the file metadata, and nothing is there too.

I then make the file format TXT to see if there are any strings hidden. I see the binary data of the file, and see the file header is aPNG IHDR, which is the header for PNG, not for pdf. i change the file extension to PNG and get the first half of the flag.

**picoCTF{f1u3n7_1n_pn9_&_pdf_249d05c0}**