# Processes and Jobs

## Listing Processes

We learn about the ps command, Which lists all active processes. It doesn't actually list all process though, Only the processes running in the current terminal. ps -ef displays ALL the processes running on the machine, with the e part showing all the processes, and the f giving additional information such as UID.

i start by trying **ps** to see if the challenge file is running in the terminal. it's not. so i try **ps -ef**, and the challenge file is indeed running in the background. it's running as **/challenge/28369-run-24163**. i run this file in the shell and it yields me the flag.

## Killing Processes

using the kill command with the PID as an argument kills the process, simple enough. we run a **ps -ef** to find the PID of challenge/dont_run, to find and kill it. the -f is important, as it provides additional information such as the PID. we kill the process and run /challenge/run to get the flag.

## Interrupting Processes

i've used ctrl-c a lot of times to interrupt processes, nothing new. it differs from kill by making the program cleanly exit. we run /challenge/flag and then interrupt it with ctrl-c to get the flag.

## Suspending Processes

we run /challenge/run and then suspend the process (pause it) by doing ctrl-z to get the flag.

## Resuming Processes

We run and suspend the same process again, with ctrl-z. then we resume the previous process by doing fg to yield us the key.

## Background Processes

We run the program and suspend it. we can then resume and allow it to run in the background by using the bg command. since it's running in the background, we can still use our terminal and run /challenge/run again to get the flag.

## Foreground Processes

We run /challenge/run, and it starts up the file. we have to pause and suspend it first by doing ctrl-z. we are then supposed to put it in the background, THEN bring it into the foreground to get the flag. we do this by first doing **bg** to resume the process in the background.

our terminal's still usable, so now we bring it into the foreground with **fg**. it yields us the flag.

## Starting Backgrounded Processes

We can use the & command to run a command in the background from the get-go. so we just do **/challenge/run &** to run the program in the background and get the flag.

## Process Exit Codes

running a command, and then running echo $? returns the exit code of the last command. there was some confusion initially, since i tried to perform this operation on /challenge/run, but then i realised that the question actually states to do it on /challenge/get-code. i ran that, and then did echo $? which yields us the flag. 