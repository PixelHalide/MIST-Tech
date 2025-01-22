# Pondering PATH

## The PATH Variable

as done in the example, i blank out the path variable but running rm instead of ls before this time.

```
rm
ssh-entrypoint: rm: No such file or directory
PATH=""
```

this breaks rm, and we can just run /challenge/run to get the flag as c.

## Setting PATH

We set the PATH as the folder win is in, that is in /challenge/more_commands. we do this by doing **PATH="/challenge/more_commands/"**, then we can run /challenge/run which invokes win in /challenge/more_commands/ and gets us the flag.

## Adding commands

we first start by creating a shell script to print out the flag with this command: **echo "cat /flag" > win**. then we make it executable with **chmod +x win**, and find the location where cat is located with with **which cat**. since we're gonna change the path, we need to define the program to use the absolute program of cat. we do it with this: **echo "/run/workspace/bin/cat /flag" >> win**. we then set our path to the current directory and the location of cat with **PATH="$HOME:/bin"** and run /challenge/run to get the flag.

## Hijacking Commands

we first make a shell script named rm and have the contents print out flag with this command: **echo "cat /flag" > rm**, then make it executable with **chmod +x rm**. we then set the path location for the current home directory for rm, and bin for cat with **PATH="$HOME:/bin"**, then run /challenge/run to get the flag.