# Day 24: More Linked Lists

### Objective

Check out the [Tutorial](https://www.hackerrank.com/challenges/30-linked-list-deletion/tutorial) 
tab for learning materials and an instructional video!

### Task

A _Node_ class is provided for you in the editor. 
A _Node_ object has an integer data field, _data_, and a Node instance pointer, _next_, pointing to another node.

A _removeDuplicates_ function is declared in your editor, 
which takes a pointer to the _head_ node of a linked list as a parameter.
Complete _removeDuplicates_ so that it deletes any duplicate nodes from the list 
and returns the head of the updated list.

### Input Format

The first line contains an integer, _N_, the number of nodes to be inserted.
The _N_ subsequent lines each contain an integer describing the _data_ value of a node being inserted at the list's tail.

### Constraints

* The data elements of the linked list argument will always be in non-decreasing order.

### Output Format

Your _removeDuplicates_ function should return the head of the update linked list.
The output should be printed as a space separated list of integers on one line.
