# Level 5

we go into the specified directory, and i notice that all file names start with "-". i cat out all the files, finding the human readable one with the password.

this is not the optimal solution, and i knew it. i read through the documentation of the commands given as hints, and find that the file command outputs the file type. i do a file ./* to output the type of all files in the current (./) directory, with the asterisk globbing for all files. this tells us that file07 has ascii data. we output the contents of that and get the password.