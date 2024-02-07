# Karatsuba Method
[Karatsuba](https://en.wikipedia.org/wiki/Karatsuba_algorithm) Method for fast multiplication using divide and conquer algorithm.
This method was discovered by [Anatoly Karatsuba](https://en.wikipedia.org/wiki/Anatoly_Karatsuba) in 1960 and published in 1962.
![Karatsuba multiplication of az+b and cz+d (boxed), and 1234 and 567.](https://en.wikipedia.org/wiki/File:Karatsuba_multiplication.svg)
[Karatsuba explained under a minute.](https://www.youtube.com/watch?v=LCY4dnm88oI)

It is a **divide & conquer** algorithm that reduces the multiplication of two n-digit numbers to three multiplications of n/2-digit numbers and by repeating this reduction, to at most n^1.59 single digit multiplications.
It is therefor **asymptotically faster** than the **traditional algorithm**, which performs n^2 single-digit products.

For example, to multiply two 1024-digit numbers (n = 1024 = 2^10), the traditional algorithm requires 1,048,576 single-digit multiplications, whereas the Karatsuba algorithm requires 59,049 thus being ~17.758 times faster.

## Recursive Application
If _n_ is four or more, the three multiplications in Karatsuba's basic step involve operands with fewer than _n_ digits.
Therefore, those products can be computed by recursive calls of the Karatsuba algorithm.
The recursion can be applied until the numbers are so small that they can (or must) be computed directly.

## Karatsuba Time Complexity Analysis
Karatsuba's basic step works for any base _B_ and any _m_, but the recursive algorithm is most efficient when _m_ is equal to _n_/2, rounded up.
In particular, if _n_ is 2^k, for some integer _k_, and the recursion stops only when _n_ is 1, then the number of single-digit multiplications is 3^k, which is _n_^c where _c_ = log(base2) 3.

Since the additions, subtractions, and digit shifts (multiplications by powers of _B_) in Karatsuba's basic step take time proportional to _n_, their cost becomes negligible as _n_ increases.
More precisely, if _t_(_n_) denotes the total number of elementary operations that the algorithm performs when multiplying two _n_-digit numbers, then:
T(_n_) = 3T(\[n/2]) + cn + d

Normal Multiplication Time Complexity:     O(n^2)
Karatsuba Multiplication Time Complexity: O(n^1.59)
Karatsuba Multiplication Auxiliary Space:    O(n)

## Pseudo-Code for Karatsuba Method
'''
function karatsuba(num1, num2)
	if (num1 < 10 or num2 < 10)
		return num1 x num2 
		// fall back to traditional multiplication
   m = max(size_base10(num1), size_base10(num2))
   m2 = floor(m/2) 
   // or m2 = ceil(m/2) will also work
   
   // split the digit sequence in the middle
   high1, low1 = split_at(num1, m2)
   high2, low2 = split_at(num2, m2)

   // 3 recursive calls made to numbers approximately half the size.
   z0 = karatsuba(low1, low2)
   z1 = karatsuba(low1 + high1, low2 + high2)
   z2 = karatsuba(high1, high2)
   return (z2 x 10^(m2 x 2)) + ((z1 - z2 - z0) x 10^m2) + z0
'''

## External links
+ ["Karatsuba Multiplication"](https://mathworld.wolfram.com/KaratsubaMultiplication.html)
+ [Karatsuba's Algorithm for Polynomial Multiplication](http://www.cs.pitt.edu/~kirk/cs1501/animations/Karatsuba.html)