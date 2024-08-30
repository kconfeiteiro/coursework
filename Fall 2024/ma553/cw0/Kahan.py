#!/usr/bin/env python3
"""
MA 553 - Classwork 0: Krystian Confeiteiro - 08/30/2024
Purpose: To implement W. Kahan's example of finite precision arithmetic failings from C. Van Loan, Intro. to Computational Science, 1995; p. xxiv

QUESTIONS
---------
- Questions 4
    - The values for x and y agree with my exactly, while the others do not. For the most part, all of the languages agree with the general calculations, even if they are off.
- Questions 6
    - It seems that Python is the most accurate of the languages tested today. I believe this is due to the automated use of the double precision that was mentioned in the assignment outline. Another idea, is that Python is being interpreted by C, in which there are things that can be done between the two languages that can make the results more precise.
- Questions 8
    - The results between the double precision calculations and the standard calculations seem to be the same. I am not sure why this could be.
- Questions 9
    - I added that line to the end of `Kahan.py` and got a result of `z:  2.220446049250313e-16`
"""

h = 1 / 2
x = (2 / 3) - h
y = (3 / 5) - h
u = (x + x + x) - h
v = (y + y + y + y + y) - h
q = u / v

print("x :", x)
print("y :", y)
print("u :", u)
print("v :", v)
print("q :", q)
print()

z = abs(3 * (4 / 3 - 1) - 1)
print("z: ", z)
