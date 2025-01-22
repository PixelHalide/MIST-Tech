# Level 6

we have to find a file with the following attributes:

33 bytes in size
owned by user bandit7
owned by group bandit6

i do **find / -size 33c**, to search the entire server for the file. this returns a lot of files, so i must refine my search query.
i read through the manpages for find again, and find 2 flags. -gid for groupid and -user for username.

i first list all groups by doing **cat /etc/group**, and find the gid (group id) for bandit 6, being 11006. i make my query **find / -size 33c -gid 11006 -user bandit7**. this should work, but it tries to access a lot of folders it doesn't have permission to, and this clogs up my screen. i try to mitigate this by using sudo, but i don't have root access.

i then remember from linux luminarium that we can just pipe the errors away using 2>. i try to do this into a random file but i don't have permissions to make a file. i just go into a dev directory and pick a random file to pipe the errors to, that being /dev/full, and it works and i get only the file meeting my query.

**find / -size 33c -gid 11006 -user bandit7 2> /dev/full**

i cat the file and get the password.
