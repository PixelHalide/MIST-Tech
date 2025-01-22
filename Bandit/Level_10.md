# Level 10

The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

we already know how to use the strings command from the previous challenge. now, we have to search the output of that for words with "=" preceeding them.

it's simple file globbing. we first pipe the output from strings and glob it. i construct my query as **strings data.txt | grep ===\***, which searches for human readable text in data.txt, and finds text which starts with atleast 3 = (arbitrarily chosen since they said several). this is our output:

}========== the
3JprD========== passwordi
~fDV3========== is
D9========== (password)

and we successfully get the password.