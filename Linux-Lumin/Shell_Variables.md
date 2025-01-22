# Shell Variables

## Printing Variables

FLAG is the name of our variable, and we have to print it. I do ***echo $FLAG*** 
to reveal the flag, using $ to indicate the variable status of FLAG.

## Setting Variables

I run **PWN=COLLEGE**, to set the value of the variable PWN as COLLEGE.

## Multi-word Variables

As taught, I run **PWN="COLLEGE YEAH"**, with apostrophes due to the space in the command.

## Exporting Variables

We have to export the variable PWN, But not COLLEGE. First, I set the value of PWN as COLLEGE by doing **PWN=COLLEGE**, then set the value of COLLEGE as PWN with **COLLEGE=PWN**. I then export PWN by doing **export PWN** and then get the flag with **/challenge/run PWN**.

## Printing Exported Variables

I first run env as instructed, But then see a huge body of text that i'd have to look through for the flag. as we learnt earlier, the grep command allows us to search files and outputs for various this. i pipe the output of env to grep to get the flag with **env | grep "pwn"**.

## Storing Command Output

We first store the output of /challenge/run into PWN with the command**PWN=$(/challenge/run)**. We can then print out PWN with **cat $PWN** to get the flag.

## Reading Input

We prompt the user to input PWN with the command **read -p "Input PWN: " PWN**, Input COLLEGE to set the value of PWN as COLLEGE. We can then output the value of PWN with **echo $PWN** to get the flag.

## Reading files

We return to the < and > operators, which we use to redirect the outputs of our code to somewhere else. We have to input the output of /challenge/run into the variable PWN in order to get the flag. We can do this with the command: **read PWN < /challenge/run**