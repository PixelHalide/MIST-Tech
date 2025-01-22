# Level 6

we have to find a file with the following attributes:

1033 bytes in size
human-readable (ascii)
not executable

i go through the manpages for the find command, since we have to **find** a file, and i find a flag called size. it allows us to find files by size. i do **find -size 1033c**, with the c denoting the unit as bytes. it returns the location of one file, which out cat out to get the flag.