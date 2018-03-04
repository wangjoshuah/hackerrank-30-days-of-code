# Day 26: Nested Logic

### Objective

Today's challenge put's your understanding of nested conditional statements to the test.
You already have the knowledge to complete this challenge, 
but checkout the [Tutorial](https://www.hackerrank.com/challenges/30-nested-logic/tutorial) 
tab for a video on testing!

### Task

Your local library needs your help! 
Given the expected and actual returns dates for a library book, create a program that calculates the fine (if any).
The fee structure is as follows:
1. If the book is returned on or before the expected return _day_, no fine will be charged (_fine_ = 0).
2. If the book is returned after the expected return date but still within the same calendar month and year as the expected return date,
_fine_ = 15 Hackos x (the number of days late).
3. If the book is returned after the expected return _month_ but still within the same calendar year as the expected return date, 
the _fine_ = 500 Hackos x (the number of months late).
4. If the book is returned after the calendar _year_ in which it was expected, there is a fixed fine of 10000 Hackos.

### Input Format

The first line contains 3 space-separated integers denoting the respective _day_, _month_, and _year_ on which the book was expected to be returned.

### Constraints

* 1 ≤ _D_ ≤ 31
* 1 ≤ _M_ ≤ 12
* 1 ≤ _Y_ ≤ 3000
* It is guaranteed that the dates will be valid Gregorian calendar dates.

### Output Format

Print a single integer denoting the library fine for the book received as input.

### Sample Input
```
9 6 2015
6 6 2015
```
### Sample Output
```
45
``` 
