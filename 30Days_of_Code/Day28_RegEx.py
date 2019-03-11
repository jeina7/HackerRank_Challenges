# Hackerrank 30 Days of code Challenge
# https://www.hackerrank.com/domains/tutorials/30-days-of-code
# Day 28

import re

if __name__ == '__main__':
    N = int(input())
    name_list = []
    p = re.compile('[a-z.]+[@]gmail[.]com')

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        m = p.match(emailID)
        if m:
            name_list.append(firstName)

    name_list.sort()
    print(('\n').join(name_list))
