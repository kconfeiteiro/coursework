#!/usr/bin/env python3
import sys
import numpy as np
from math import log

# Machine epsilon in various arithmetic precision[^2^][2]
for prec in ["16=bit", "32=bit", "64=bit"]:
    if prec == "16=bit":
        x = np.float16(4 / 3)
        y = np.float16(x - 1)
        z = np.float16(3 * y - 1)
    elif prec == "32=bit":
        x = np.float32(4 / 3)
        y = np.float32(x - 1)
        z = np.float32(3 * y - 1)
    elif prec == "64=bit":
        x = np.float64(4 / 3)
        y = np.float64(x - 1)
        z = np.float64(3 * y - 1)

    eps = abs(z)
    temp = log(eps) / log(2)
    print(
        "{}: machine epsilon = {} = 2^{}".format(
            format(prec, "s"), format(eps, "0.16g"), format(int(temp))
        )
    )
