# HTTP - Open redirect

Find a way to make a redirection to a domain other than those showed on the web page.

## Solution

On clicking one of the three links presented, we get this request in burp:

```
GET /web-serveur/ch52/?url=https://twitter.com&h=be8b09f7f1f66235a9c91986952483f0 HTTP/1.1
Host: challenge01.root-me.org
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://challenge01.root-me.org/web-serveur/ch52/?url=https://facebook.com&h=a023cfbf5f1c39bdf8407f28b60cd134
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

We can see twitter.com in the get request, And I changed it to google.com. However, this yielded the error "Incorrect hash" on the website. I looked at the get request again:

GET /web-serveur/ch52/?url=https://twitter.com&h=be8b09f7f1f66235a9c91986952483f0 HTTP/1.1

and noticed the h tag, probably standing for hash. i googled **be8b09f7f1f66235a9c91986952483f0** and found out that it was an md5 hash for twitter.com. i did an md5 hash of google.com and replaced the old hash, and successfully got the answer.
