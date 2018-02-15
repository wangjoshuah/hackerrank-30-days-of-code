# Day 11: 2D Arrays
### Objective
Today, we're building on our knowledge of Arrays by adding another dimension.
Check out the [Tutorial](https://www.hackerrank.com/challenges/30-2d-arrays/tutorial)
tab for learning materials and an instructional video!
### Context
Given a 6x6 _2D Array, A_:
```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
We define an hourglass in _A_ to be a subset of values with indices falling in this pattern in A's graphical representation:
```
a b c
  d
e f g
```
There are 16 hourglasses in _A_,
and an _hourglass sum_ is the sum of an hourglass' values.
### Task
Calculate the hourglass sum for every hourglass in _A_,
then print the maximum hourglass sum.
### Input Format
There are 6 lines of input, where each line contains 6 space separated integers describing _2D Array *A*_;
every value in _*A*_ will be in the inclusive range of -9 to 9.
### Constraints
* -9≤A\[i]\[j]≤9
* 0≤i,j≤5
### Output Format
Print the largest (maximum) hourglass sum found in _*A*_.
### Sample Input
```
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```
### Sample Output
```
19
```
### Explanation
_*A*_ contains the following hourglasses:
```
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
```
The hourglass with the maximum sum (19) is:
```
2 4 4
  2
1 2 4
```
