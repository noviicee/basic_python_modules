"""
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints:
0<k<=len(S)

The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines.
"""

from itertools import combinations
s,n=input().split()
for x in range(1,int(n)+1):
    l=list(combinations(sorted(s),x))
    for i in l:
        print(''.join(i))
