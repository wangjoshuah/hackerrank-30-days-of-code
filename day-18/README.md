# Day 18: Queues and Stacks

Welcome to day 18! Today we're learning about Stacks and Queues.
Check out the [Tutorial](https://www.hackerrank.com/challenges/30-queues-stacks/tutorial)
tab for learning materials and an instructional video!

A _palindrome_ is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards.
Can you determine if a given string, _s_, is a palindrome?

To solve this challenge, we must first take each character _s_, enqueue it in a queue,
and also push that same character onto a stack.
Once that's done, we must dequeue the first character from the queue and pop the top character off the stack,
then compare the two characters to see if they are the same;
as long as the characters match,
we continue dequeueing, popping, and comparing each character until our containers are empty.

Write the following declarations and implmentations:

1. Two instance variables: one for your _stack_ and one for your _queue_.
2. A _void pushCharacter(char ch)_ method that pushes a character onto a stack.
3. A _void enqueueCharacter(char ch)_ method that enqueues a character int he _queue_ instance variable.
4. A _char popCharacter()_ method that pops and returns the character at the top of the _stack_ instance variable.
5. A _char dequeueCharacter()_ method that dqueues and returns the first character in the _queue_ instance variable.

### Input Format

Read a single line containing string _s_.
Then call the methods specified above to pass each character to your instance variables.

### Constraints

* _s_ is composed of lowercase English letters.

### Output Format

If your code is correctly written and _s_ is a palindrome,
print `The word, s, is a palindrome.`;
otherwise, print `The word, s, is not a palindrome`.

### Sample Input
```
racecar
```
### Sample Output
```
The word, racecar, is a palindrome.
```
