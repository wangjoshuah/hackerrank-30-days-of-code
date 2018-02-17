# Day 14: Scope

### Objective

Today we're discussing _scope_. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-scope/tutorial)
tab for learning materials and an instructional video!

The _absolute difference_ between two integers, _a_ and _b_, is written as |_a - b_|.
The _maximum absolute difference_ between two integers in a set of positive integers, _elements_,
is the largest absolute difference between any two integers in _elements_.

The _Difference_ class is started for you in the editor.
It has a private integer array (_elements_) for storing _N_ non-negative integers,
and a public integer (_maximumDifference_) for storing the maximum absolute difference.

### Task complete teh _Difference_ class by writing the following:

* A class constructor that takes an array of integers as a parameter
and saves it tot he _elements_ instance variable.
* A _computeDifference_ method that finds the maximum absolute difference between any 2 numbers in _N_
and stores it in the _maximumDifference_ instance variable.

### Input Format

The _Solution_ class read in 2 lines of input;
the first line contains _N_,
and the second line describes the _elements_ array.

### Constraints

* 1 ≤ _N_ ≤ 10
* 1 ≤ _elements_\[_i_\]_ ≤ 100, where 0 ≤ _i_ ≤ _N_ - 1

### Output Format

The _Solution_ class will print he value of the _maximumDifference_ instance variable.

### Sample Input
```
3
1 2 5
```
### Sample Output
```
4
```
