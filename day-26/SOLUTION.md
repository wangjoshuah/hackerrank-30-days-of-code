# Day 26: Nested Logic

## Objective
Today we're being challenged on nested conditional statements. Check out day 3's video if you aren't familiar with conditional statements.

## Task

Our task today is to help calculate the late return fines for a library. When a book is returned, we will calculate the return cost based on the following structure:

1. If the book is returned on or before the expected return date, no fine will be charged. (fine = 0).
2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, _fine = 15 Hackos x (the number of days late)_. 
3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the _fine = 500 Hackos x (the number of months late)_.
4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of _10000 Hackos_. 

### Input Format

The first line will contain 3 space-separated integers denoting the respective _day_, _month_, and _year_ on which the book was actually returned.
The second line contains the 3 space-separated integers denoting the respective _day_, _month_, and _year_ on which the book was expected to be returned (due date).

Dates will be valid Gregorian calendar dates
1 <= D <= 31
1 <= M <= 12
1 <= Y <= 3000

### Output Format

Print a single integer denoting the library fine for the book received as input.

## Solution

We have 4 states we could be in. There is no due date, the book is a few days late, the book is months late, or the book is a year late. There are also 3 categories we are checking based on--year, month, and date. We are going to nest our conditional statements since a year contains months and a month contains days. 

We will first check if the book is returned in a previous year, the same year, or a later year. If the book was returned in a previous year than the due year, then we do not need to pay a fine. If the book was returned in the same year as the due year, we will need to check month and date. Otherwise, if the book was returned in a year after the due year, we will print 10000. 

In the case that the book was returned in the same calendar year as the due date, we need to check the month and day. First we check if the book was returned in a previous month, if so, we do not need to pay a fine. If the book was returned in the same calendar month, then we need to check the day. Otherwise the fine is the number of months behind the book was multiplied by 500. 

If the book was returned in the same year and month, we need to check for the return day. If the book was returned on or before the due date, we do not need to pay a fine so we will print 0. Otherwise we will print the number of days behind the book was multiplied by 15. 

## Implementation

First, we need to parse the input strings into variables. We will capture the first line of input, strip whitespace on the ends, and split it on spaces. We can use python list interpretation to split the array of strings into its elements, and cast them to integers, then store them in the `return_day`, `return_month` and `return_year` variables. You can read the docs [here](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions). We will do the same for the second line of input to get the due dates.

Then we will check if the return year is less than the due year. If it is, we print 0. We will also make an elif condition if the return year is the same as the due year and check months later. We also need to fill in the else case where the return year is greater than the due year and print 10000.

In the case where the return year is the same as the due year, we will check to see if the return month is before the due month. In this case, we print 0. We also need an elif condition to see if the return month is equal to the due month. We will check return date in this case. We also need to fill in the else case where the return month is greater than the due month and print 500 by the number of months late.

In the most nested case, we check the return date. If it is on or before the due date, we will print 0 since we do not need to pay a fine. Otherwise, we will print 15 by the number of days late.
