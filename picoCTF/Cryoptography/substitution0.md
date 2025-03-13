# substitution0

## Challenge

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?

## Solving

we are greeted with a big wall of jumbled text. the challenge description states it's a subsitution cypher, so we have that major hint already.
i see this sentence with brackets like this:

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}

this is obvoiusly the flag, and we know the flag format, being picoCTF{}. i map ruseSWX to picoCTF, and the rest of the words can be easily figured out. but i used an online tool to solve the cypher:

[text](https://www.guballa.de/substitution-solver)

## Flag

picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}