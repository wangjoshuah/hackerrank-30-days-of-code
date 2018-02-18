# Day 17: More Exceptions

### Objective

Yesterday's challenge taught you to manage exceptional situtations by using _try_ and _catch_ blocks.
In today's challenge, you're going to practice throwing and propogating an exception.
Check out the [Tutorial](https://www.hackerrank.com/challenges/30-more-exceptions/tutorial)
tab for learning materials and an instructional video!

### Task

Write a _Calculator_ class with a single method: _int power(int, int)_.
The _power_ method takes two integers, _n_ and _p_, as parameters and returns the integer result of _n^p_.
If either _n_ or _p_ is negative,
then the method must throw an exception must throw an exception with the message:
`n and p should be non-negative`.

### Input Format

The first line contains an integer, _T_, the number of test cases.
Each of the _T_ subsequent lines describes a test case in 2 space-separated integers denoting _n_ and _p_ respectively.

### Constraints

* No test case will result in overflow for correctly written code.

### Output Format

There are _T_ lines of output,
where each line contains the result of _n^p_ as calculated by your _Calculator_ class' _power_ method.

### Sample Input
```
4
3 5
2 4
-1 -2
-1 3
```
### Sample Output
```
243
16
n and p should be non-negative
n and p should be non-negative
```