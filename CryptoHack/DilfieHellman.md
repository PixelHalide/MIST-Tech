# Starter

## Working with Fields

The set of integers modulo NN, together with the operations of both addition and multiplication forms a ring Z/NZZ/NZ. Fundamentally, this means that adding or multiplying any two elements in the set returns another element in the set.

When the modulus is prime: N=pN=p, we are additionally guaranteed a multiplicative inverse of every element in the set, and so the ring is promoted to a field. In particular, we refer to this field as a finite field denoted FpFp​.

The Diffie-Hellman protocol works with elements of some finite field FpFp​, where the prime modulus is typically very large (thousands of bits), but for the following challenges we will keep numbers smaller for compactness.

Given the prime p=991p=991, and the element g=209g=209, find the inverse element d=g−1d=g−1 such that g⋅dmod  991=1g⋅dmod991=1.

### Solution

We are given the following equation:

209d mod(991) = 1

And are told to find d.

In modular exponentiation, we know that:

a mod b = c

is the same as:

c mod b = a

Hence, we can write this as:

1 mod(991) = 209d

Then take the inverse with:

209^-1 mod(991)

We can easily compute this by doing:

pow(209,-1,991)

Which yields us the number **569**.

## Computing Public Values

For a given g, p, a, Compute g^a mod(p)

### Solving

We simply use the pow function in python. the code below returns the number that we need:

```
ans = pow(g,a,p)
print(ans)
```

## Computing Shared Secrets

This problem is an application of the Diffie-Hellman key exchange.

### Solving

We are given the original public base and modulus. Alice uses her private integer as an exponent to the public base, and sends the result of the modulus to us.

We then use our private integer to exponent the public base, and send that to alice so she can get the shared private key.

Anyways, To get the share private key, We simply have to raise the integer given to us by Alice by our private integer and modulus it. We do that like this:

```
p= 24103124...
A= 702499432...
b= 1201923325...
ans = pow(A,b,p)

print(ans)
```

This yields us the answer, the shared private key.

## Deriving Symmetric Keys

### Solving

The problem is almost exactly same as the last question. We're given the public base and modulus, Alice's shared integer, and our private integer. We use this to calcuulate the shared private key.

Then I open the file given to us for the AES decryption. It has 3 empty variables:

```
shared_secret =
iv =
ciphertext =
```

I input the value for all of these and run the program, yielding us the flag.

**crypto{sh4r1ng_s3cret5_w1th_fr13nd5}**