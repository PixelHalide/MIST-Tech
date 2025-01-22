# Digesting Documentation

## Learning From Documentation

**/challenge/challenge --giveflag** ran as instructed

## Learning Complex Usage

since the printfile argument prints out the contents of files, i decide to cd to root, where flag is always present, and print the contents of flag with **/challenge/challenge --printfile /flag**

## Reading Manuals

**man challenge** is ran as instructed. the manual describes a flag --ohboql with which if the argument 129 is passed, prints the flag. **/challenge/challenge --ohboql 129** is executed to get the flag.

## Searching Manuals

**man challenge** is ran as instructed. i press / and type in flag to search for all instances of the word flag in the document, and press n to sift through them. one of them states that it is the right argument that outputs the flag. the flag is executed along with **/challenge/challenge** to get the flag.

## Searching For Manuals

As sifting through the manual for man in the terminal was cumbersome, i read the online manual for it at https://man7.org/linux/man-pages/man1/man.1.html. reading through the manual, i stumble across the -k flag, which allows us to search for elements inside manpages. 

i do **man -k flag**, to find all manpages with the word flag inside it. it reveals a manpage with the description "print the flag!". printing the manual for this command tells us about a flag that prints the flag when a specified argument is passed.

the flag is executed along with **/challenge/challenge** to get the flag.

## Helpful programs

**/challenge/challenge --help** is executed to show the arguements and flags that can be passed to this program. a flag named -p prints a secret key, and passing that secret key with the flag -g gives us the flag.

## Built for bulletins

i try to run help /challenge/challenge, but it doesn't work. after cd'ing into challenge then running **help challenge**, it does work and prints out documentation. it gives me a secret key, and passing that as an argument to a flag mentioned in the documentation, --secret with challenge gives us the flag.