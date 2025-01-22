# Perceiving Permissions

## Changing File Ownership

we learn about the chown command, which takes 2 arguments, the file and user we are giving permission to. we go into root with **cd /** since the flag is stored there, then use chown hacker flag to allow the hacker user to access flag. then we can simply **cat flag** to get the flag.

## Groups and Files

we learn about the chgrp command, which functions effectively the same as chown, but changes the groups that can be accessed by the file. by doing **chgrp hacker flag** we change the permissions of the flag command to allow the hacker group to access it.

## Fun with group names

we're no longer in the hacker group, and in some other group that we don't know the name of. we can simply do **id** to get our group name. then we do a simple **chgrp (new group name) /flag** and print the flag with cat.

## Changing Permissions

we learn about chmod, which i've used a lot previously to make bash scripts executable. it tells us about the r, w, x arguments to it, which make the file readable, writable and executable. i go to / and do **chmod +rwx ./flag** (although just a +r would suffice), which gives the current user the permission to read the file. i can then get the flag from it.

## Executable files

We just have to make the /challenge/run file executable. any linux user would've done this a lot of times, we just do a simple **chmod +x /challenge/run**.

## Permission Tweaking Practice

I was originally a bit confused about how to do multiple commands at once, so i had to read some documentation(https://www.geeksforgeeks.org/chmod-command-linux/). i learnt that you can just use comma for that. we run /challenge/run and it tells us to change permissions of /challenge/pwn to what's specified. we do that with these commands in succession:

```
chmod g-r ./challenge/pwn 
chmod g+rx,a+r,u+x ./challenge/pwn
chmod u-rwx ./challenge/pwn
chmod u+rw,g+w,a+w ./challenge/pwn
chmod u-rw,g-rw ./challenge/pwn
chmod g-x ./challenge/pwn
chmod a-w ./challenge/pwn
```

after this, we can finally change flag to be readable by doing **chmod +r /flag** and print it out for the flag.

## Permissions Setting Practice

mostly the same thing, but we use = instead here, which makes it faster since we don't have to see the difference between the current and required permissions, just what the required permissions are.
```
chmod u=r,g=rw,o=x /challenge/pwn
chmod u=,g=rwx,o=rw /challenge/pwn
chmod u=w,g=rwx,o=x /challenge/pwn
chmod u=,g=w,o=wx /challenge/pwn
chmod u=wx,g=,o=r /challenge/pwn
chmod u=rwx,g=wx,o=wx /challenge/pwn
chmod u=r,g=w,o=rwx /challenge/pwn
chmod u=rw,g=wx,o=x /challenge/pwn
```

## The SUID Bit

we first set the suid bit on /challenge/getroot by doing **chmod u+s /challenge/getroot**, which sets a suid bit for the current user on getroot. then we execute /challenge/getroot, which spawns a root shell. since we have root privileges in this shell, we can simply cat out the flag.
