#!/bin/bash

echo "Which day would you like to test?"
read TEST_DIR

cd $TEST_DIR

ACTUAL_OUTPUT=$(cat test-input.txt | python3 solution.py)
TEST_DIFF=$(diff <(echo "$ACTUAL_OUTPUT") test-output.txt)

if [ $? -ne "0" ]; then
    echo "Test FAILED."
    echo "$TEST_DIFF"
    exit 1
else
    echo "Test PASSED."
fi