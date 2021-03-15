import sys
import matplotlib.pyplot as plt


class Coord:
    def __init__(self, lat, long, rx, best_unit):
        self.lat = lat
        self.long = long
        self.rx = rx
        self.best_unit = best_unit


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

    # Until the end of the file
    while True:
        # Structure: Latitude	Longitude	Rx(dB)	Best unit
        current_line = f.readline()
        cl_s = current_line.split("	")

        # End of file
        if current_line == "":
            break

        # Increments frequency_best_units list
        best_unit_index = int(cl_s[3])
        frequency_best_units[best_unit_index] = frequency_best_units[best_unit_index] + 1

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

    # setting the ranges and no. of intervals
    range_x = (plot_min_rx, plot_max_rx)
    bins = plot_number_bins

    # plotting a histogram
    plt.hist(all_rx_values, bins, range_x, color='green',
             histtype='bar', rwidth=0.8)

    # x-axis label
    plt.xlabel('Rx(dB)')
    # frequency label
    plt.ylabel('Number of Entries')
    # plot title
    plt.title('Frequency of Rx Values')

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
