# Day 4: Class vs. Instance

### Objective

In this challenge, we're going to learn about the difference between a _class_ and an _instance;
because this is an _Object Oriented_ concept, it's only enabled in certain languages.
Check out the [Tutorial](https://www.hackerrank.com/challenges/30-class-vs-instance/tutorial)
tab for learning materials and an instructional video!

### Task

Write a _Person_ class with an instance variable, _age_,
and a constructor that takes an integer, _initialAge_,
as a parameter.
The constructor must assign _initialAge_ to _age_
after confirming the argument passed as _initialAge_ is non negative;
if a negative argument is passed as _initial_Age,
the constructor should set _age_ to 0
and print `Age is not valid, setting age to 0.`.
In addition, you must write the following instance methods:

1. _yearPasses()_ should increase the _age_ instance variable by 1.
2. _amIOld()_ should perform the following conditional actions:
   * If _age_ < 13, print `You are young.`
   * If _age_ ≥ 13 and _age < 18, print `You are a teenager.`
   * Otherwise, print `You are old.`

### Input Format

The first line contains an integer, _T_,
and the _T_ subsequent lines each contain an integer denoting the _age_ of a Person instance

### Constraints

* 1 ≤ _T_ ≤ 4
* -5 ≤ _age_ ≤ 30

### Output Format

Complete the method definitions to meet the specifications outlined above.
If your methods are implemented correctly, each test case will print 2 or 3 lines
(depending on whether or not a valid _initialAge_ was passed to the constructor).

### Sample Input
```
4
-1
10
16
18
```
### Sample Output
```
Age is not valid, setting age to 0.
You are young.
You are young.

You are young.
You are a teenager.

You are a teenager.
You are old.

You are old.
You are old.
```
