# HTTP - IP restriction bypass

Dear colleagues,

We’re now managing connections to the intranet using private IP addresses, so it’s no longer necessary to login with a username / password when you are already connected to the internal company network.

Regards,

The network admin

## Solution

As the page says, we will bypass the login page if we are accessing it from the internal intranet.

So we have to use burp suite and append X-forwarded-for to our network request, as it tells the browser where our request is coming from.

Reading the rfc file attached, we see that 10.0.0.0 is an address reserved for private internets. Using that addresses, We are able to access the flag.

