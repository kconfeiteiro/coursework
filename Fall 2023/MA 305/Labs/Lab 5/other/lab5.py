#!/usr/bin/env python3
"""
========================================================================
MA305 - Lab 5: Antonio Cascio - 11/3/2023
Purpose: Inedxing and Searching Lists to help figure out interesting
information from given Temperature-Humidity data
========================================================================
"""
#import pandas for reading file
import pandas as pd

#define constants
horizontal_line = "==============="

#define functions for calculations of average and mapping
map_func = lambda func, array: list(map(func, array))
average = lambda array: sum(array) / len(array)

# define function to calculate heat index
def heat_index(T, H):
    if T > 55:
        return -42.379 + 2.04901523*T + 10.14333127*H - 0.22475541*T*H - 6.83783e-3*T*T - 5.481717e-2*H*H + 1.22874e-3*T*T*H + 8.5282e-4*T*H*H - 1.99e-6*T*T*H*H
    else:
        return T

#define function to decode the data
def get_date(date):
    return "{}/{}/{}".format(int((date / 100) % 100), int(date % 100), int(date / 10000))

#define function to determine all the needed statistical values of the columns
def calcualte_col_stats(data, *columns):
    final_results = []
    for column in columns:
        DATA = list(data[column])
        col_max = max(DATA)
        col_min = min(DATA)

        final_results.append({
            "average": average(DATA),
            "maximum": col_max,
            "max index": DATA.index(col_max),
            "minimum": col_min,
            "min index": DATA.index(col_min),
        })

    return tuple(final_results)

#read data with pandas
file = "../lab5.txt"
data_read = pd.read_csv(
    file,
    delim_whitespace=True,
    comment="#",
    header=[1],
    on_bad_lines="skip",
)

#set new column valuse to the calculated heat index
data_read["HI"] = pd.DataFrame(
    list(map(heat_index, data_read["T"], data_read.H))
)

#set another new column to the decoded calendar dates
data_read["Real Date"] = pd.DataFrame(list(map(get_date, data_read.Date)))
data_read = data_read[["Date", "Real Date", "T", "H", "HI"]]
temperatures, humidities, heat_indecies = calcualte_col_stats(data_read, "T", "H", "HI")

# calculate needed values for temp, hum, and HI
max_temp, min_temp = temperatures["maximum"], temperatures["minimum"]
max_hum, min_hum = humidities["maximum"], humidities["minimum"]
max_hi, min_hi = heat_indecies["maximum"], heat_indecies["minimum"]

# determine the rows for maximum and minimum temperatures
max_temp_row = data_read.loc[data_read["T"] == max_temp]
min_temp_row = data_read.loc[data_read["T"] == min_temp]

# determine the rows for maximum and minimum humidities
max_humidity_row = data_read.loc[data_read["HI"] == max_hum]
max_humidity_row = data_read.loc[data_read["HI"] == min_hum]

# determine the rows for maximum and heat index
max_heat_index_row = data_read.loc[data_read["HI"] == max_hi]
min_heat_index_row = data_read.loc[data_read["HI"] == min_hi]

# determine the rows for days below freezing and above average temperatures
days_below_freezing = data_read.loc[data_read["T"] < 32]
days_above_avg_temp = data_read.loc[data_read["T"] > temperatures["average"]]

#number of days below freezing temperatures
days_below_freezing = len(days_below_freezing.index)
#number of days above average temperatures

ndays_above_average = len(days_above_avg_temp.index)

#print part c, d, and e from step (1)
print("\n {0} Part C: {0}\n".format(horizontal_line))
header = f"{'Stat':10} {'Value':<15}"
header_lines = "{0:10} {0:<15}".format("------")
types = "Temprature, Humidity, Heat Index".split(",")
for results, dtype in zip([temperatures, humidities, heat_indecies], types):
    print(f"FOR: {dtype}")
    print(header)
    print(header_lines)

    for key, val in results.items():
        print(f"{key:10} {val:<12}")
    print("\n\n")

#print values for below freezing and above average temperatures
print("\n {0} Part D and E: {0}".format(horizontal_line))
print(f"\nNumber of day above below freezing: {days_below_freezing}")
print(f"Days above average temperature: {ndays_above_average}")

#print values for average temperature
print("\nDates above average temperature:")
print(days_above_avg_temp)

#print values for freezing temperature
print("\nDates below freezing temperature:")
print(days_below_freezing)

#print number of days greater than 50 degrees
print("\n {0} STEP 3: {0}".format(horizontal_line))
print("\nNumber of days greater than 50 degrees:")
n_days_50 = data_read.loc[data_read["T"] > 50]
print(n_days_50)

#print number of days between 0 and 50 degrees
print("\n\nNumber of days between 0 and 50 degrees:")
n_days_0to50 = data_read.loc[(data_read["T"] > 0) & (data_read["T"] < 50)][
    ["Real Date", "T"]
]
print(n_days_0to50)
