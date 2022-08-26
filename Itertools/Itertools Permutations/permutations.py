# Python code to demonstrate
# to find all permutation of
# a given string
 
from itertools import permutations
 
# Initialising string
ini_str = "abc"
 
# Printing initial string
print("Initial string:", ini_str)
 
# Finding all permutation
permutation = [''.join(p) for p in permutations(ini_str)]
# Printing result
print("Resultant List:", str(permutation))

"""
Output: 
Initial string abc
Resultant List ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"""
