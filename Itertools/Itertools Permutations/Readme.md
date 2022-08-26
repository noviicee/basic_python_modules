# Using itertools 

`itertools.permutation()` function falls under the [Combinatoric Generators](#combinatoric-generators).
<br>“Permutation” refers to all the possible combinations in which a set or string can be ordered or arranged. Similarly here `itertool.permutations()` method provides us with all the possible arrangements that can be there for an iterator and all elements are assumed to be unique on the basis of their position and not by there value or category.

All these permutations are provided in lexicographical order. The function itertool.permutations() takes an iterator and ‘r’ (length of permutation needed) as input and assumes ‘r’ as default length of iterator if not mentioned and returns all possible permutations of length ‘r’ each.

Syntax: <br>
`Permutations(iterator, r)`
 
_[Python code to demonstrate to find all permutation of a given string](permutations.py)_
 
 _For more: [follow](https://www.geeksforgeeks.org/python-itertools-permutations/)_

 ----------------------------------------

### Combinatoric Generators
> The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian products are called combinatoric iterators.
