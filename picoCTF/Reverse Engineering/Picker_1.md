# Picker 1

## Challenge

This service can provide you with a random number, but can it do anything else?

Additional details will be available after launching your challenge instance.

## Solving

We are give the following python file:

```

import sys

def getRandomNumber():
  print(4)  # Chosen by fair die roll.
            # Guaranteed to be random.
            # (See XKCD)

def exit():
  sys.exit(0)

def esoteric1():
  esoteric = \
  '''
  int query_apm_bios(void)
{
	struct biosregs ireg, oreg;

	/* APM BIOS installation check */
	initregs(&ireg);
	ireg.ah = 0x53;

  ...
}
  '''
  print(esoteric)


def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)


def esoteric2():
  esoteric = \
  '''
#include "boot.h"

#define MAX_8042_LOOPS	100000
#define MAX_8042_FF	32

static int empty_8042(void)
{
	u8 status;
	int loops = MAX_8042_LOOPS;
	int ffs   = MAX_8042_FF;
...
}
  '''
  print(esoteric)


while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
  except Exception as e:
    print(e)
    break
```

Upon connecting to the instance, It asks us to enter "getRandomNumber". Entering it prints out 4. I take a look at the source code, and notice getRandomNumber is a function in the code, and that it the program uses eval to run the function. eval is slightly dangerous, as it can execute python code based on our input.

i look at the other functions, and notice **win()**, which prints out the flag. i input **win()** and it prints out the flag in hex, which i translate into ascii and get the final flag.

Lesson? Don't use eval with user input.