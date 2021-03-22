"""
Given an array of size N, find the number of distinct pairs {a[i], a[j]} (i != j) in the array with their sum greater than 0.

Example 1:

Input: N = 3, a[] = {3, -2, 1}
Output: 2
Explanation: {3, -2}, {3, 1} are two 
possible pairs.


Example 2:

Input: N = 4, a[] = {-1, -1, -1, 0}
Output: 0
Explanation: There are no possible pairs.

Your Task:  
Complete the function ValidPair() which takes the array a[ ] and size of array N as input parameters and returns the count of such pairs.

Expected Time Complexity: O(N * Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105 
-104  ≤ a[i] ≤ 104

Take from: https://www.geeksforgeeks.org/
"""

def ValidPair(a, n): 
    	# Your code goes here
    	
    	res=0
    	from itertools import combinations
    	t=list(combinations(a,2))
    	for i in t:
    	    if sum(i)>0:
    	        res+=1
    	return res

# Driver Code:
if __name__=="__main__":
	t=int(input()) # test-cases
	for x in range(t):
		n=int(input())
		array=list(map(int, input().strip().split()))
		ans=ValidPair(array,n)
		print(ans)

"""
For very large list, it will give memory error since the Expected Auxiliary Space is O(1)
"""

