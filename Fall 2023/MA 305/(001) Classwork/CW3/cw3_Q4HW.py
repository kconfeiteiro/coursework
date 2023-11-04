#!/usr/bin/env python3
"""
Krystian Confeiteiro
Dr. Sam
MA 305 - 06DB
Classwork 3 - Homework (Q4)
10/11/2023
"""


# define function for hailstone sequence
def collatz_conjecture(n_int):
    hs = [n_int]
    while True:
        if (n_int == 1) or (n_int not in range(1, 100)):
            break
        elif n_int % 2 == 0:
            n_int = n_int // 2
        else:
            n_int = (3 * n_int) + 1

        hs.append(n_int)

    return hs, len(hs)


print("MA 305 - Classwork 3, Question 4 (HW)")
print("-------------------------------------")
input_q4 = int(input("Enter value for n: "))
hs_q4, len_q4 = collatz_conjecture(input_q4)
