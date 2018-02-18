# Day 20: Sorting

### Objective

Today, we're discussing a simple sorting algorithm called _Bubble Sort_.
Checkout the [Tutorial](https://www.hackerrank.com/challenges/30-sorting/topics)
tab for learning materials and an instructional video!

Consider the following version of Bubble Sort:
```java
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;

    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }

    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
```
### Task

Given an array, _a_, of size _n_ distinct elements,
sort the array in _ascending_ order using the _Bubble Sort_ algorithm above.
Once sorted, print the following 3 lines:

1. `Array is sorted in numSwaps swaps.`
where _numSwaps_ is the number of swaps that took place.
2. `First Element: firstElement`
where _firstElement_ is the _first_ element in the sorted array.
3. `Last Element: lastElement`
where _lastElement_ is the _last_ element in the sorted array.

**Hint:** To complete this challenge, you will need to add a variable that keeps a running tally of _all_ swaps that occur during execution.

### Input Format

The first line contains an integer, _n_, denoting the number of elements in array _a_.
The second line contains _n_ space-separated integers describing the respective values of elements of _a_.

### Constraints

* 2 ≤ _n_ ≤ 600
* 1 ≤ _a_\[_i_\] ≤ 1,000,000, where 0 ≤ _i_ ≤ _n_

### Output Format

Print the following 3 lines of output:

1. `Array is sorted in numSwaps swaps.`
where _numSwaps_ is the number of swaps that took place.
2. `First Element: firstElement`
where _firstElement_ is the _first_ element in the sorted array.
3. `Last Element: lastElement`
where _lastElement_ is the _last_ element in the sorted array.

### Sample Input 0
```
3
1 2 3
```
### Sample Output 0
```
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
```
### Sample Input 1
```
3
3 2 1
```
### Sample Output 1
```
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
```