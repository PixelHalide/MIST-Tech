# Weak password

Nothing too difficult

## Solution

On inputting our user and password, we send this request:

```
GET /web-serveur/ch3/ HTTP/1.1
Host: challenge01.root-me.org
Cache-Control: max-age=0
Authorization: Basic YWVmOmFlZg==
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Cookie: _ga=GA1.1.260610508.1759325282; _ga_SRYSKX09J7=GS2.1.s1759325281$o1$g1$t1759325499$j19$l0$h0
If-None-Match: W/"61b3bb5d-110"
If-Modified-Since: Fri, 10 Dec 2021 20:41:01 GMT
Connection: keep-alive
```

looking at the authorization tag, I realise our user and password are sent in base 64 which we can change.

Since the challenge name is weak password, I immediately think of the most default password. a router usually has admin as its password and user, so inputting that gave us the answer.