# Vault Door 3

## Challenge

This vault uses for-loops and byte arrays. The source code for this vault is here:

## Solving

We are met with a Java file. I'm unfamiliar with Java, But I can still somewhat understand the code by looking at it. The Void main function takes an input, and checks it against a transformed string.

The checkPassword function transforms our inputted string via string splicing, and the output of the correct password after being transformed is **jU5t_a_sna_3lpm18gb41_u_4_mfr340**.

The first thing we should do is to work in a more comfortable environment. I translate and port over the checkPassword function into C, a language I'm more familiar in. This is what the translated code looks like:

```

#include <stdio.h>

int main() {
    int i;
    char str[35] = "jU5t_a_sna_3lpm18gb41_u_4_mfr340", buf[50];

    for (i = 0; i < 8; i++){
        buf[i] = str[i];
    }
    for (; i < 16; i++){
        buf[i] = str[23-i];
    }
    for (; i < 32; i+=2){
        buf[i] = str[46-i];
    }
    for (i = 31; i>=17; i-=2) {
        buf[i] = str[i];
        }
    buf[32] = '\0';

    puts(buf);

    return 0;
}
```

I haven't worked with Java before, But the syntax is surprisingly similar to C, Which made this entire process much easier.

Now, We begin to analyse this transformer.

str will be our inputted password, buf will be the transformed password.

1.
```
    for (int i = 0; i < 8; i++){
        buf[i] = str[i];
    }
```
This is pretty simple. The first 8 characters of string are copied over to buf.

2.
```
    for (int i = 8; i < 16; i++){
        buf[i] = str[23-i];
    }
```
Now, we must break down what happens here step by step.

```
buf[8] = str[15]
buf[9] = str[14]
...
buf[15] = str[8]
```

The 9th to 16th characters of buf become the 1tth to 9th characters of str in reverse.

3.
```
    for (int i = 16; i < 32; i+=2){
        buf[i] = str[46-i];
    }
```

```
buf[16] = str[30]
buf[18] = str[28]
...
buf[30] = str[16]
```

Here, the odd characters from the 17th to 31st character of buf turn into the odd characters from 31st to 17th character of str in reverse.

4.

```
    for (int i=31; i>=17; i-=2) {
        buf[i] = str[i];
        }
```
The same process is done as above, But with the even characters from tthe 32nd character to the 18th.
```
buf[31] = str[31]
buf[29] = str[29]
...
buf[17] = str[17]
```

Now, We must reverse engineer and invert this entire process.

Here, str is the transformed password (jU5t_a_sna_3lpm18gb41_u_4_mfr340), and buf is the original password.

The first part is the simplest.
1.
```
    for (int i = 0; i < 8; i++){
        buf[i] = str[i];
    }
```
It simply copies over the first 8 characters.

2.
We have to iterate through each character of str, so we'll keep the right side of the equation constant as str[i].

Since we have iterated through 8 characters, I'll start the next with the 9th.

If we shift the 23 to the left side of the equation as buf[23-i], it completes what we need. the iterations go like this:

```
buf[15] = str[8]
buf[14] = str[9]
...
buf[8] = str[15]
```

This neatly reverses the operation we learnt earlier. It writes the characters in reverse from the 16th to 9th char.

Our code ends up like this:

```
    for (int i = 8; i < 16; i++){
        buf[23-i] = str[i];
    }
```

I just play around a bit, And figure out this method just works for the rest of the loops aswell. Shift the integer being subtracted to the left side, and keep the right side as i.


Finally, Our code is:

```

#include <stdio.h>

int main() {
    char str[35] = "jU5t_a_sna_3lpm18gb41_u_4_mfr340", buf[50];

    for (int i = 0; i < 8; i++){
        buf[i] = str[i];
    }
    for (int i = 8; i < 16; i++){
        buf[23-i] = str[i];
    }
    for (int i = 16; i < 32; i+=2){
        buf[46-i] = str[i];
    }
    for (int i = 31; i >= 17; i-=2) {
        buf[i] = str[i];
        }
    buf[32] = '\0';

    puts(buf);

    return 0;
}
```

Running this gives us the flag **jU5t_a_s1mpl3_an4gr4m_4_u_1fb380**.