#!/bin/bash

echo "Which day would you like to test?"
read TEST_DIR

cd $TEST_DIR

# TODO: Test multiple test cases
ACTUAL_OUTPUT=$(cat test-input-0.txt | python3 solution.py)
TEST_DIFF=$(diff <(echo "$ACTUAL_OUTPUT") test-output-0.txt)

if [ $? -ne "0" ]; then
    echo "Test FAILED."
    echo "$TEST_DIFF"
    exit 1
else
    echo "Test PASSED."
fi