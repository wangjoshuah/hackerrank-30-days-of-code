#!/bin/bash

echo "Which day would you like to test?"
read TEST_DIR

cd $TEST_DIR

SOLUTION_LANGUAGE=python

# check if solution class is java or python
if [ -e Solution.java ]
then
    javac Solution.java
    SOLUTION_LANGUAGE=java
fi

TEST_INPUTS=$(find . -name "test-*-input.txt")
TEST_NUM=0
for TEST_INPUT in $TEST_INPUTS
do
    STARTTIME=$(gdate +%s.%3N)
    if [ $SOLUTION_LANGUAGE == java ]
    then
        ACTUAL_OUTPUT=$(cat $TEST_INPUT | java Solution)
    elif [ $SOLUTION_LANGUAGE == python ]
    then
        ACTUAL_OUTPUT=$(cat $TEST_INPUT | python3 solution.py)
    fi
    TEST_DIFF=$(diff -w <(echo "$ACTUAL_OUTPUT") test-$TEST_NUM-output.txt)
    ENDTIME=$(gdate +%s.%3N)

    DURATION=$(echo "$ENDTIME-$STARTTIME" | bc)

    if [ $? -ne "0" ]; then
        echo "Test $TEST_NUM FAILED in $DURATION seconds"
        echo "$TEST_DIFF"
        exit 1
    else
        echo "TEST $TEST_NUM PASSED $DURATION seconds"
    fi

    TEST_NUM=$((TEST_NUM+1))

done
