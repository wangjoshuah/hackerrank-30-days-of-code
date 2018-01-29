#!/bin/bash
set -e

echo "Which day would you like to test?"
read TEST_DIR

cd $TEST_DIR

TEST_CASES=$(find testcase-*-input.txt)

# TODO: loop over all test cases
ACTUAL_OUTPUT=$(cat testcase-0-input.txt | python3 solution.py)
TEST_DIFF=(diff <(echo "$ACTUAL_OUTPUT") testcase-0-output.txt)

if [ $? -ne "0" ]; then
    echo "Test Case 0 FAILED."
    echo "$TEST_DIFF"
    exit 1
else
    echo "Test Case 0 PASSED."
fi