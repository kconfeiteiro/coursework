#!/usr/bin/env python3
"""
Krystian Confeiteiro
Dr. Sam
MA 305 - 06DB
Classwork 3
10/11/2023
--
Purpose:
    Read a positive integer `n` from user input and
    generate the hailstone sequence starting at `n`.
"""


# define function for hailstone sequence
def hailstone_seq(n_int: int = None):
    hs = [n_int]
    while True:
        if n_int == 1:
            break
        elif n_int % 2 == 0:
            n_int = n_int // 2
        else:
            n_int = (3 * n_int) + 1

        hs.append(n_int)

    return hs, len(hs)


# Inputs and rest of assignment
print("Hailstone Sequence")
print("------------------")
n_user = int(input('Enter value for "n": '))
hs_user, len_user = hailstone_seq(n_user)

print(f"\nFor n = {n_user}, there are {len(hs_user)} values:")
print(hs_user, "\n------")

for val in range(25, 28):
    hs_array, hs_len = hailstone_seq(val)
    print(f"For n = {val}, there are {hs_len} values:")
    print(hs_array, "\n")
