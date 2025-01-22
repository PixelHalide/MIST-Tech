# File Globbing

## Matching with *

we have to cd into challenge while keeping the total wordcount under 4. since * autocompletes the words for us, we can just use that. cd /ch*, then just ./run to get the flag.

## Matching with ?

since we can't use c and l, just replace those characters in challenge with ?, since it autofills for it. **cd /?ha??enge** takes us to /challenge, where we can just do **./run** and get the flag.

## Matching with []

we cd into /challenge/files as instructed. then we have to execute run with the files file_a, file_s, file_h, file_b as an argument. we can just do /challenge/run file_[absh]* to then get the key.

## Matching paths with []

execute /challenge/run /challenge/files/file_[absh]*, with the absolute address of the file locations.

## Mixing globs

i first try to find something common amongst these three words. i break them down to their letter counts:
educational:
a-2, c-1, d-1, e-1, i-1, l-1, n-1, o-1, t-1, u-1

challenging:
a-1,c-1,e-1,g-2,h-1,i-1,l-2,n-2

pwning:
g-1,i-1,n-2,p-1,w-1

i try to do some weird combinations, such as *[ng]* or *[wn]*, but it doesn't work out. 
i think for a while, and realise those 3 words are the only words that start with e, c and p. so i just do [ecp]*, which searches for all words that start with e, c or p and autofills the rest. passing this as an argument with **/challenge/run** gives us the flag

## Exclusionary globbing

cd into /challenge/files, and just do /challenge/run [!pwn]* as instructed for the flag.

