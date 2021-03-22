### Syntax:
--------------
#### itertools.combinations(iterable, r)
--------------------------------------

This tool returns the *r* length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

**Sample Code:**
`
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
`

<br/>

[Python Code](https://github.com/noviicee/basic_python_modules/blob/main/Itertools/Itertools%20Combination/itertools_combination.py)
<br/>
[Exception:SpaceComplexity](https://github.com/noviicee/basic_python_modules/blob/main/Itertools/Itertools%20Combination/itertools_combination_exp.py)
