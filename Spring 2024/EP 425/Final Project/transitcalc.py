import math
from datetime import datetime, timezone

import numpy as np


def jd_to_calendar(jd_time, base_jdtime=1721424.5, date_format="%m/%d/%Y %H:%M:%S"):
    date = datetime.fromordinal(math.floor(jd_time - base_jdtime))
    return date.strftime(date_format)


def transit_jd_date(transit_number):
    return (5.551497500 * transit_number) + 2458895.773170


# calculate the UTC in hours
utc_time = datetime.now(timezone.utc)
UTC_IN_HRS = float((utc_time.day * 24) + (utc_time.hour + (utc_time.minute / 60)))


def calc_JD_time(year, month, day, utc1=UTC_IN_HRS):
    print("UTC in hours: ", utc1)
    return (
        (367 * year)
        - ((7 * (year + ((month + 9) / 12))) / 4)
        + ((275 * month) / 9)
        + day
        + (utc1 / 24)
        - 0.5 * np.sign(100 * year + month - 190002.5)
        + 0.5
    )


trial1 = (2024, 2, 21)
print("Trial 1 (YYYY, M, D): ", trial1)

trial1_JD = calc_JD_time(*trial1)
print("Calculated JD time: ", trial1_JD)
