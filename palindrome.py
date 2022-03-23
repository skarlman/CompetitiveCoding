# Google kickstart 2022 Round A - Palindrome Free Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e

# Recursive backtracking solution that passed all test sets

import sys


def check_string(S, i):
    if i > 3:
        # check 5 last for odd palindrome
        if all([S[i - x] == S[i - 4 + x] for x in range(2)]):
            return False

        if i > 4:
            # check last 6 for even palindrome
            if all([S[i - x] == S[i - 5 + x] for x in range(3)]):
                return False

    if i == len(S) - 1:
        return True

    i += 1

    if S[i] == '?':
        S[i] = '1'
        test1 = check_string(S, i)
        if not test1:
            S[i] = '0'
            test0 = check_string(S, i)
            if not test0:
                S[i] = '?'
                return False
            else:
                return True
        else:
            return True
    else:
        return check_string(S, i)


if __name__ == '__main__':
    sys.setrecursionlimit(64000)
    t = int(input())

    for test_case in range(1, t + 1):
        tmp = input()
        S = [c for c in input().strip()]

        result = check_string(S, -1)
        resultstr = "POSSIBLE" if result else "IMPOSSIBLE"
        print("Case #" + str(test_case) + ": " + resultstr)
