# Pondering Paths

## The Root

Ran /pwm as instructed to get the flag.

## Program and absolute paths

Ran the absolute path of pwm, /challenge/pwn to get the flag.

## Position thy self

Ran /challenge/pwn, Which instructs you to run the program from /usr/share/build-essential directory. 
cd into /usr/share/build-essential directory, then run /challenge/pwn again.

## Position elsewhere

Ran /challenge/pwn, Which instructs you to run the program from /etc. 
cd into /etc, then run /challenge/pwn again.

## Position yet elsewhere

Ran /challenge/pwn, Which instructs you to run the program from /var/lib/apt/lists. 
cd into /var/lib/apt/lists directory, then run /challenge/pwn again.

## implicit relative paths, from /

Ran /challenge/pwn, Which instructs you to run the program from /. 
cd'd once to go into /, the root directory
Then Ran challenge/pwn without a slash, Since it's in the current directory

## explicit relative paths, from /

Ran /challenge/pwn, Which instructs you to run the program relatively from /. 
cd'd once to go into /, the root directory
Then executed ./challenge/run as instructed in the question

## implicit relative path

cd'd into /challenge, then ran ./run to explicitly run the file

## home sweet home

we must make a file inside our home directory (~), so i make a file named "a" by doing **touch a**, to keep the file name small. then we run **/challenge/run ~/a**, which gives us the required flag.