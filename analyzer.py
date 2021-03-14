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
    range_line_info = range_line.split("	")
    max_rx = range_line_info[1]
    # range / 10
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
    coords = []  # list of Coords objects

    # Until the end of the file
    while True:
        # Structure: Latitude	Longitude	Rx(dB)	Best unit
        current_line = f.readline()
        cl_s = current_line.split("	 ")

        # Saves coords for future use
        coords.append(Coord(cl_s[0], cl_s[1], cl_s[2], cl_s[3]))

        # Best_units update
        # Increments best units list
        best_units[cl_s[3]] = best_units[cl_s[3]] + 1

        # Rx_interval update
        rx_int = int(cl_s[2])

        # Negative values are ignored
        if rx_int >= 0:
            index = int(rx_int // 10)
            rx_interval[index] = rx_interval[index] + 1 

if __name__ == "__main__":
    parse("All3.txt")
