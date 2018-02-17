# Day 16: Exceptions - String to Integer

### Objective

Today, we're getting started with _Exceptions_ by learning how to parse an integer from a string
and print a custom error message.
Check out the [Tutorial](https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/tutorial)
tab for learning materials and an instructional video!

### Task
Read a string, _S_, and print its integer value;
if _S_ cannot be converted to an integer, print `Bad String`.

**Note:** You _must_ use the String-to_integer and exception handling constructs built into your submission language.

### Input Format

A single string, _S_.

### Constraints

* 1 ≤ |_S_| ≤ 6, where |_S_| is the length of string _S_.
* _S_ is composed of either lower case letters (a-z) or decimal digits (0-9).

### Output Format

Print the parsed integer value of _S_, or `Bad String` if _S_ cannot be converted to an integer.

### Sample Input 0
```
3
```
### Sample Output 0
```
3
```
### Sample Input 1
```
za
```
### Sample Output 1
```
Bad String
```
