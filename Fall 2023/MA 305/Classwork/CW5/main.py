"""
Krystian Confeteiro
Dr. Sam
MA 305 - 06DB
Classwork 5
Purpose: Reading and arrays from a file and calculate the average.
"""


def average_and_maximum(_list):
    # obtain average of list
    average = sum(_list) / len(_list)

    # obtain maximum value from list
    length, maximum = len(_list), _list[0]
    for i in range(1, length):
        if _list[i] > maximum:
            maximum = _list[i]
            loc_maximum = i

    return (average, maximum, loc_maximum)


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

    print("\t")
    [print(f"\t{xval:-5.2f}\t{yval:-5.2f}") for xval, yval, in zip(xcol, ycol)]

    x_avg, xmax, xmax_loc = average_and_maximum(xcol)
    y_avg, ymax, ymax_loc = average_and_maximum(ycol)
