"""
Krystian Confeiteiro
Dr. Sam
MA305-06DB: Introduction to Scienfific Computing
09/13/2023
"""

h = 1 / 2
x = 2 / 3 - h
y = 3 / 5 - h
u = (x + x + x) - h
v = (y + y + y + y + y) - h
q = u / v

print("\nLab ZERO | Results")
print("h: {}".format(h))
print("x: {}".format(x))
print("y: {}".format(y))
print("u: {}".format(u))
print("v: {}".format(v))
print("q: {}\n".format(q))
