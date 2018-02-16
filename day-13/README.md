# Day 13: Abstract Class
### Objective
Today, we're taking what we learned yesterday about _Inheritance_ and extending it to _Abstract Classes_.
Check out the [Tutorial](https://www.hackerrank.com/challenges/30-abstract-classes/tutorial)
tab for learning materials and an instructional video.
### Task
Given a _Book_ class and a _Solution_ class, write a _MyBook_ class that does the following:
* Inherits from a _Book_
* Has a parameterized constructor taking these 3 parameters:
  1. string _title_
  2. string _author_
  3. int _price_
* Implements the _Book_ class' abstract _display()_ method so it prints these 3 lines:
  1. `Title:`, a space, and then the current instance's _title_.
  2. `Author:`, a space, and then the current instance's _author_.
  3. `Price:`, a space, and then the current instance's _price_.

### Input Format
The _Solution_ class creates a _Book_ object and calls the _MyBook_ class constructor.
It then calls the _display_ method on the _Book_ object.
### Output Format
The _display()_ method should print and label the respective _title_, _author_, and _price_ of the _MyBook_ object's instance like so:
```
Title: $title
Author: $author
Price: $price
```
### Sample Input
```
The Alchemist
Paulo Coelho
248
```
### Sample Output
```
Title: The Alchemist
Author: Paulo Coelho
Price: 248
```
