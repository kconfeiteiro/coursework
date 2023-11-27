from numpy import *
from numpy.linalg import solve
from cmath import polar

R1 = R3 = R5 = 1000
R2 = R4 = R6 = 2000

C1 = 1e-6
C2 = 0.5e-6
xp = 3
omega = 1000

A = array(
    [
        [(complex(1 / R1 + 1 / R4, (omega * C1))), (complex(0, (-omega * C1))), 0],
        [
            (complex(0, (-omega * C1))),
            (complex((1 / R2 + 1 / R5), ((omega * C1) + (omega * C2)))),
            [0, complex(0, (-omega * C2)), (complex(1 / R3 + 1 / R6, (omega * C2)))],
        ],
    ],
    complex,
)


b = array([(xp / R1), (xp / R2), (xp / R3)], complex)

x = solve(A, b)


r1, theta1 = polar(x[0])
r2, theta2 = polar(x[1])
r3, theta3 = polar(x[2])


theta1 *= 180 / pi
theta2 *= 180 / pi
theta3 *= 180 / pi


print("V1 = ", r1, " phase = ", theta1)
print("V2 = ", r2, " phase = ", theta2)
print("V3 = ", r3, " phase = ", theta3)
