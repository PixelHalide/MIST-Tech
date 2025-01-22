# Untangling Users

## Becoming root with su

we start with running su to get root access. it asks for a password and i input the given password. now that we have root shell, we can simply cat the flag out.

## Other users with su

we pass the argument of the user that we want to switch to, in this case zardus with **su zardus**. after inputting the given password, we run /challenge/run to get the flag.

## Cracking passwords

i originally try to run /challenge/shadow-leak, but i get permission denied. i try a couple times, and then realised it's probably not an executable. i perform an ls -l, and i see that i have permissions to read the file, not execute it.

i cat out the file and see that hashed password of zardus is indeed present here:

$6$CUQIbVwuwsvsZ2hU$qMPbPB3s62Jue8myHmp0a0VFMUA0gS9kjNYhoNlsQPjlOGm.t3FQ2wGJ2.tVg1Ldtk9QBvegsN4DVOjPegwWI1

i run the password cracker, john the ripper on /challenge/shadow-leak with **john /challenge/shadow-leak**, and see the decrypted password.

now we su back into zardus with this password and run /challenge/run to get the flag.

## Using sudo

since we can run commands with root access with sudo, we do a **sudo cat /flag** and get the flag.

