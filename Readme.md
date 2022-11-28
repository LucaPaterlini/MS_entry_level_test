# Fun Coding Python

## Intro

Those problems where part of the first stage interview at Microsoft UK

## Problem A

Given a string containing only 'a' and 'b' characters find the most efficient way 
to calculate how many characters needed to be added to have a balanced length
of the subsections of homogeneous characters.

example
```
f('aaabb') = > 1
f('abab') => 0
```

## Problem B

Given 3 strings of the same length containing only english lowercase letters
return a tuple with the 3 indexes where the character is the same,
if 2 solutions are valid pick the one with lower index values.

example
```
f(['abc', 'bca', 'dbe']) => (1,0,1)
f(['ba', 'za', 'ca']) => (1,1,1)
```