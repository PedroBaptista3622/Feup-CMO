class Coord:
    def __init__(self, lat, long, rx, best_unit):
        self.lat = lat
        self.long = long
        self.rx = rx
        self.best_unit = best_unit


def parse(file_name):
    f = open("CoverageResults/" + file_name, "r")

    # Range Read
    range_line = f.readline()
    range_line_info = range_line.replace(",", ".").split("	")
    max_rx = float(range_line_info[1][:-2])
    # range / 10 + 1 -> for greater than max_rx
    rx_interval = [0 for i in range(int(round(max_rx / 10)))]

    # Units Read
    units = []  # list of tuples: (id, name)
    best_units = [0]

    unit_line = f.readline()
    unit_line_split = unit_line.split("	")

    # while line != "Latitude	Longitude	Rx(dB)	Best unit"
    while len(unit_line_split) != 4:
        # Adds a tuple with unit id and name to the units list
        units.append((unit_line_split[1], unit_line_split[2]))
        best_units.append(0)

        unit_line = f.readline()
        unit_line_split = unit_line.split("	")

    # Coords read
    # coords = []  # list of Coords objects

    # Number rx above max
    rx_above_max = 0

    # Number rx below zero
    rx_below_zero = 0

    # Contains all rx values
    rx_values = []

    # Until the end of the file
    while True:
        # Structure: Latitude	Longitude	Rx(dB)	Best unit
        current_line = f.readline()
        cl_s = current_line.split("	")

        # End of file
        if current_line == "":
            break

        # Saves coords for future use
        # coords.append(Coord(cl_s[0], cl_s[1], cl_s[2], cl_s[3]))

        # Best_units update
        # Increments best units list
        best_unit_index = int(cl_s[3])
        best_units[best_unit_index] = best_units[best_unit_index] + 1

        # Rx_interval update
        rx_int = float(cl_s[2].replace(",", "."))
        rx_values.append(rx_int)

        if rx_int >= max_rx:
            # Values above max are separated
            rx_above_max = rx_above_max + 1
        elif rx_int < 0:
            # Negative values are separated
            rx_below_zero = rx_below_zero + 1
        else:
            # Values in bounds
            index = int(rx_int // 10)
            rx_interval[index] = rx_interval[index] + 1

    # Prints results
    print("Max Rx:" + str(max_rx))

    print("Number rx below 0: " + str(rx_below_zero))
    print("RX Interval: ")
    print(rx_interval)
    print("Number rx above max: " + str(rx_above_max))

    print("UNITS")
    print(units)
    print("Best Units: ")
    print(best_units)

    # print("Some coords")
    # print(coords[0:10])


if __name__ == "__main__":
    parse("All3.txt")
