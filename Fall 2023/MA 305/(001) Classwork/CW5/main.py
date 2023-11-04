"""
Krystian Confeteiro
Dr. Sam
MA 305 - 06DB
Classwork 5
10/28/2023
--------
Purpose:
    Reading and arrays from a file and calculate the average.
"""


def avg_and_max(_list):
    # average of list
    average = sum(_list) / len(_list)

    # maximum value from list
    length, maximum = len(_list), _list[0]
    for i in range(1, length):
        if _list[i] > maximum:
            maximum = _list[i]
            loc_maximum = i

    return (average, maximum, loc_maximum)


def read_txt(filename, mode="r"):
    with open(filename, mode) as file:
        lines = file.readlines()
        return lines


def save_to_txt(filename, lines, mode="w"):
    leading = lambda x: "\n" + x
    with open(filename, mode):
        file.writelines(list(map(leading, lines)))


if __name__ == "__main__":
    # read lines from file
    filepath = "dat5.txt"
    with open(filepath, "r") as file:
        lines = file.readlines()

    # append x and y vals to new list
    xcol, ycol, count = [], [], 1
    while True:
        line = lines[count].split()
        print(*line)

        if int(line[0]) == 0:
            break

        xcol.append(float(line[2]))
        ycol.append(float(line[3]))
        count += 1

    # print values and caluclate averge and maximum
    print(f"\nRead {count} files from {filepath}:")

    print(f"{'x':1}{'y':>12}")
    [print(f"{xval:1}{yval:>12}") for xval, yval, in zip(xcol, ycol)]

    x_avg, xmax, xmax_loc = avg_and_max(xcol)
    y_avg, ymax, ymax_loc = avg_and_max(ycol)

    print(f"\nx-stats\n-------")
    print(f"average: {x_avg}\nMaximum xcol[{xmax_loc}]: {xmax}")
    print(f"\ny-stats\n-------")
    print(f"average: {y_avg}\nMaximum ycol[{ymax_loc}]: {ymax}")

    # read and print data from dat5a.txt
    print("\nReading data from `dat5a.txt:")
    dat5a = read_txt("dat5a.txt")
    [print(line, end="") for line in dat5a]
