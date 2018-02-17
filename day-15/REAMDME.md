# Day 15: Linked List

### Objective

Today we're working with _Linked Lists_.
Check out the [Tutorial](https://www.hackerrank.com/challenges/30-linked-list/tutorial)
tab for learning materials and an instructional video!

A _Node_ class is provided for you in the editor.
A _Node_ obect has an integer data field, _data_, and a _Node_ instance pointer, _next_, pointing to another node.

A _Node_ _insert_ function is also declared in your editor.
It has two parameters: a pointer, _head_, pointing to the first node of a linked list,
and an integer _data_ value that must be added to the end of the list as a new _Node_ object.

Complete the _insert_ function in your editor so that it creates a new _Node_
(pass _data_ as the _Node_ constructor argument)
and inserts it at the tail of the linked list reference by the _head_ parameters.
Once the new node is added, return the reference to the _head_ node.

**Note:** If the _head_ argument passed to the _insert_ function is _null_,
then the initial list is empty.

### Input Format

The _insert_ function has 2 parameters: a pointer to a _Node_ hamed _head,
and an integer value, _data_.
The constructor for _node_ has 1 parameter: an integer value for the _data_ field.

### Output Format

Your _insert_ function should return a reference to the _head_ node of the linked list.

### Sample Input

The first line contains _T_, the number of test cases.
The _T_ subsequent lines of test cases each contain an integer to be inserted at the list's tail.

```
4
2
3
4
1
```

### Sample Output

Print the ordered data values for each element in your list as a single line of space separated integers:

```
2 3 4 1
```
