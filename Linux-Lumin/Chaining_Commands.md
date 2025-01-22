# Chaining Commands

## Chaining commands with Semicolons

we chain /challenge/pwn with /challenge/college as **/challenge/pwn;/challenge/college** as instructed to get the flag.

## Your first shell script

i first try to do **echo /challenge/run > x.sh; echo /challenge/college > x.sh**, then run it via bash x.sh, but this doesn't seem to work. then i realise that the > operator actually overwrites anything in the file, and we have to use the append (>>) operator for this. **echo /challenge/run > x.sh; echo /challenge/college >> x.sh** and then bash.sh gives us the flag. we have used echo here because we want bash to invoke the commands, not store the output of the commands into the shell script.

## Redirecting Script output

we do **/challenge/run > x.sh; /challenge/college >> x.sh; /challenge/solve < x.sh**. here, the output of /challenge/run is first stored in the shell script, then after that the output of /challenge/college. this combined output is then inputted into /challenge.solve to get the flag.

## Executable Shell Scripts

we first have to create a shell script that will invoke /challenge/solve on running. we do this by doing **echo /challenge/solve > x.sh**. we then have to make it executable to our user without using bash. as we learnt in the previous module, we do this by doing **chmod +x x.sh**, and then run it with ./x.sh to get the flag.