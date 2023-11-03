import pandas as pd


def heat_index(temp, humidity):
    if temp > 55:
        heat_index = (
            -42.379
            + 2.04901523 * temp
            + 10.14333127 * humidity
            - 0.22475541 * temp * humidity
            - 6.83783e-3 * (temp**2)
            - 5.481717e-2 * (humidity**2)
            + 1.22874e-3 * humidity * (temp**2)
            + 8.5282e-4 * temp * (humidity**2)
            - 1.99e-6 * (temp**2) * (humidity**2)
        )
    else:
        heat_index = temp

    return round(heat_index, 3)

def find_indx(col, condition):
    return col.index(condition)

def calc_avg(data):
    return sum(data) / len(data)


def read_date(date):
    day = date % 100
    month = (date / 100) % 100
    year = date / 10000

    return "{}/{}/{}".format(*to_int(month, day, year))


def print_stats(stats):
    for key, val in stats.items():
        print(f"{key:10} {val:<12}")


def stats(data, *columns):
    dictionaries = []
    for column in columns:
        DATA = list(data[column])
        col_max, col_min = max(DATA), min(DATA)

        dictionaries.append(
            {
                "average": calc_avg(DATA),
                "maximum": col_max,
                "max index": find_indx(DATA, col_max),
                "minimum": col_min,
                "min index": find_indx(DATA, col_min),
            }
        )

    return tuple(dictionaries)


DATA = pd.read_csv(
    "lab5.txt",
    delim_whitespace=True,
    comment="#",
    header=[1],
    on_bad_lines="skip",
)

DATA = DATA.rename(columns={"T": "Temperature", "H": "Humidity"})
DATA["Heat Index"] = pd.DataFrame(
    list(map(heat_index, DATA.Temperature, DATA.Humidity))
)

DATA["Std. Date"] = pd.DataFrame(list(map(read_date, DATA.Date)))
DATA = DATA[["Date", "Std. Date", "Temperature", "Humidity", "Heat Index"]]
TEMP, HUMIDITY, HEAT_INDEX = stats(DATA, "Temperature", "Humidity", "Heat Index")
RESULTS = (TEMP, HUMIDITY, HEAT_INDEX)

max_temp_row = DATA.loc[DATA.Temperature == TEMP.get("maximum")]
min_temp_row = DATA.loc[DATA.Temperature == TEMP.get("minimum")]
max_humidity_row = DATA.loc[DATA["Heat Index"] == HUMIDITY.get("maximum")]
max_humidity_row = DATA.loc[DATA["Heat Index"] == HUMIDITY.get("minimum")]
max_heat_index_row = DATA.loc[DATA["Heat Index"] == HEAT_INDEX.get("maximum")]
min_heat_index_row = DATA.loc[DATA["Heat Index"] == HEAT_INDEX.get("minimum")]
days_below_freezing = DATA.loc[DATA.Temperature < 32]
days_above_avg_temp = DATA.loc[DATA.Temperature > TEMP.get("average")]

num_days_below_freezing = len(days_below_freezing.index)
num_days_above_avg = len(days_above_avg_temp.index)

# for key, row in finals.items():
#     prompt = key.replace("_", " ")
#     print(f"{prompt.title()}\n", "-" * 15)
#     print(row.iloc[0, :], "\n")

hline = "=" * 15

print("\n {0} PART C: {0}\n".format(hline))
_prompt = f"{'Stat':10} {'Value':<15}"
_prompt1 = "{0:10} {0:<15}".format("------")
types = "Temprature, Humidity, Heat Index".split(",")
for results, dtype in zip(RESULTS, types):
    print(f"FOR: {dtype}")
    print(_prompt)
    print(_prompt1)
    print_stats(results)
    print("\n\n")

print("\n {0} PART D & E: {0}".format(hline))
print(f"\nNumber of day above below freezing: {num_days_below_freezing}")
print(f"Days above average temperature: {num_days_above_avg}")

print("\nDates above average temperature:")
print(FINALS.get("days_above_avg_temp")[["Std. Date", "Temperature"]])

print("\nDates below freezing temperature:")
print(FINALS.get("days_below_freezing")[["Std. Date", "Temperature"]])

print("\n {0} STEP 3: {0}".format(hline))
print("\nNumber of days greater than 50 degrees:")
n_days_50 = DATA.loc[DATA.Temperature > 50][["Std. Date", "Temperature"]]
print(n_days_50)

print("\n\nNumber of days between 0 and 50 degrees:")
n_days_0to50 = DATA.loc[(DATA.Temperature > 0) & (DATA.Temperature < 50)][
    ["Std. Date", "Temperature"]
]
print(n_days_0to50)
