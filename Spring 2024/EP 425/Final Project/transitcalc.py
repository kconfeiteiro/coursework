import math
from datetime import datetime, timezone

import numpy as np


def jd_to_calendar(jd_time, base_jdtime=1721424.5, date_format="%m/%d/%Y %H:%M:%S"):
    date = datetime.fromordinal(math.floor(jd_time - base_jdtime))
    return date.strftime(date_format)


def transit_jd_date(
    transit_number, transit_time=5.551497500, time_since_last_transit=2458895.773170
):
    """
    Determines the JD date of the next transit based on the time (in hours) for a transit along with the JD for the time of the last recorded transit.

    Parameters
    ----------
    transit_number : float
        the number of the transit (i.e., like the 241st transit)
    transit_time : float, optional
        the time (in hours) of the transit, by default 5.551497500 (hours)
    time_since_last_transit : float, optional
        JD time of the last recorded transit, by default 2458895.773170

    Returns
    -------
    float
        JD time of the next transit (based on the transit number)
    """
    return (transit_time * transit_number) + time_since_last_transit


# calculate the UTC in hours
utc_time = datetime.now(timezone.utc)
UTC_IN_HRS = float((utc_time.day * 24) + (utc_time.hour + (utc_time.minute / 60)))


def calc_JD_time(year, month, day, utc1=UTC_IN_HRS):
    """
    Calculates the JD date from a calendar date.

    Parameters
    ----------
    year : integer
        _description_
    month : integer
        _description_
    day : integer
        _description_
    utc1 : float, optional
        the reference JD date, by default UTC_IN_HRS

    Returns
    -------
    _type_
        _description_
    """
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
