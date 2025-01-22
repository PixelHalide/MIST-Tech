# Level 12

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

it's a simple rot 13 cypher.

i looked through the commands given below, and stumbled upon tr. i can use it to replace text with other text.

in a rot 13 cypher, an a will be replaced with an n, and a z with an m. we have to do this to all ascii letters, upper or lowercase. our query becomes **cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'**. with 'A-Za-z' telling it to look for all characters, and 'N-ZA-Mn-za-m' meaning letters a to m will be mapped from n to z and so on. doing this yields us the flag.