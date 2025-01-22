# Level 9

we have to find the password in a file. the password occurs only once in that file.

i don't have any idea, so i read through the manpages of the commands given below.

i find three useful commands, **uniq**, which finds unique lines, **sort**, which sorts unique lines and finally **strings**, which finds only readable text.
my plan is to first sort the text alphabetically, since unique can only filter adjacent text, then pipe the output to uniq, then finally pipe to strings.

i construct my query as sort **data.txt | uniq | strings** and execute it. there is a lot of output, and i've done something wrong. i mess about a bit and realised i've read the question wrong.

the password is the ONLY unique line. there are no duplicates of it. uniq by itself only removes the duplicates. i actually have to do uniq -u which shows only the unique lines in the file.

doing **sort data.txt | uniq -u| strings** finally yields us the password.