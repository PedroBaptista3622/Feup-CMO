import sys
import matplotlib.pyplot as plt


# class Coord:
#     def __init__(self, lat, long, rx, best_unit):
#         self.lat = lat
#         self.long = long
#         self.rx = rx
#         self.best_unit = best_unit


def parse(file_name, plot_min_rx, plot_max_rx, plot_number_bins):
    f = open("CoverageResults/" + file_name, "r")

    # ========== Parsing Section

    # Range Read
    range_line = f.readline()
    range_line_info = range_line.replace(",", ".").split("	")
    max_rx = float(range_line_info[1][:-2])

    # rx_interval ==> [0, max_rx/plot_number_bins[ , (...) , [max_rx, 0[
    rx_interval = [0 for i in range(int(round(max_rx / plot_number_bins)))]

    # Units Read
    units = []  # list of tuples: (id, name)

    # frequency_best_units[2] ==> number of times unit 2 appears as the best unit in the file
    frequency_best_units = [0]

    unit_line = f.readline()
    unit_line_split = unit_line.split("	")

    # while line != "Latitude	Longitude	Rx(dB)	Best unit" AKA Start of rx values
    while len(unit_line_split) != 4:
        # Adds a tuple with unit id and name to the units list
        units.append((unit_line_split[1], unit_line_split[2]))
        frequency_best_units.append(0)

        unit_line = f.readline()
        unit_line_split = unit_line.split("	")

    # Number rx above max_rx
    rx_above_max = 0

    # Number rx below zero
    rx_below_zero = 0

    # Contains all rx values
    all_rx_values = []

    # Contains all best units
    # all_best_units = []

    # Until the end of the file
    while True:
        # Structure: Latitude	Longitude	Rx(dB)	Best unit
        current_line = f.readline()
        cl_s = current_line.split("	")

        # End of file
        if current_line == "":
            break

        # Increments frequency_best_units list
        current_best_unit = int(cl_s[3])
        frequency_best_units[current_best_unit] = frequency_best_units[current_best_unit] + 1
        # all_best_units.append(current_best_unit)

        # Rx_interval update
        rx_float = float(cl_s[2].replace(",", "."))
        all_rx_values.append(rx_float)

        if rx_float >= max_rx:
            # Values above max are separated
            rx_above_max = rx_above_max + 1
        elif rx_float < 0:
            # Negative values are separated
            rx_below_zero = rx_below_zero + 1
        else:
            # Values in bounds
            index = int(rx_float // 10)
            rx_interval[index] = rx_interval[index] + 1

    # ========== Result Printing Section

    print("Max Rx:" + str(max_rx))

    print("Number rx below 0: " + str(rx_below_zero))
    print("RX Interval: ")
    print(rx_interval)
    print("Number rx above max: " + str(rx_above_max))

    print("UNITS")
    print(units)
    print("Frequency Best Units: ")
    print(frequency_best_units)

    # ========== Plot Section

    # Rx Histogram

    # setting the ranges and no. of intervals
    range_rx = (plot_min_rx, plot_max_rx)

    # plotting a histogram
    plt.hist(all_rx_values, plot_number_bins, range_rx, color='green',
             histtype='bar', rwidth=0.8)

    # x-axis label
    plt.xlabel('Rx(dB)')
    # frequency label
    plt.ylabel('Number of Entries')
    # plot title
    plt.title('Frequency of Rx Values')

    # function to show the plot
    plt.show()

    # Best units Bar chart

    # x-coordinates of left sides of bars
    left = [1, 2, 3, 4, 5]

    # labels for bars
    tick_label = ['None']
    for unit_tuple in units:
        label = unit_tuple[0] + ": " + unit_tuple[1]
        tick_label.append(label)

    # plotting a bar chart
    plt.bar(left, frequency_best_units, tick_label=tick_label,
            width=0.8, color='green')

    # naming the x-axis
    plt.xlabel('Unit Name')
    # naming the y-axis
    plt.ylabel('Number of Entries')
    # plot title
    plt.title('Number of times each unit is the best')

    # function to show the plot
    plt.show()


if __name__ == "__main__":
    print(sys.argv)
    # Invalid number of arguments
    if len(sys.argv) != 5:
        print(
            "Usage: " + sys.argv[0] + " <file name> <plot min rx> <plot max rx> <plot number bins>")
    else:
        parse(sys.argv[1], float(sys.argv[2]),
              float(sys.argv[3]), int(sys.argv[4]))
