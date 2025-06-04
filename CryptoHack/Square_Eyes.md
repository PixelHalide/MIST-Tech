# Square Eyes

It was taking forever to get a 2048 bit prime, so I just generated one and used it twice.

# Solution

We are given n, e and c. The challenge states that one prime is used twice, which means p = q.

This makes things very easy for us.

For decrypting, it's:

c^d % n

and d = e^-1 % (p-1)(q-1)

however, we know here that p = q, and that the square root of n is equal to p. so we will then get access to every answer and hence, they flag.

here's the program i made to solve it:

```
from Crypto.Util.number import long_to_bytes
import math

p_square = 535860808044009550029177135708168016201451343....
e = 65537
ct = 2225028859741824295009483898405634...

# N is a perfect square

# Totient will be (p-1)^2

p = math.isqrt(p_square)

totient = (p-1)**2

d = pow(e, -1, totient)

m = pow(ct, d, p_square)


ans = long_to_bytes(m)

print(ans)
```

I had to use math.isqrt because **0.5 couldn't handle such large numbers. Anyways, I tried this and it actually didn't work. I tried more for a bit, and remembered the hint given in the qn again:

**If you're stuck, look again at the formula for Euler's totient.**

turns out, euler's totient has a different formula if p = q. it's p(p-1). changing it to this gives us the flag.

# flag

crypto{squar3_r00t_i5_f4st3r_th4n_f4ct0r1ng!}


