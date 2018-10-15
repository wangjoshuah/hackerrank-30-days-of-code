#!/bin/python3

import re

if __name__ == '__main__':
    N = int(input())

    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)
    firstNames = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if regex.search(emailID):
            firstNames.append(firstName)

    firstNames.sort()

    for name in firstNames:
        print(name)
